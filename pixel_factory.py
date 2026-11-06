#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Flashstation client + a read of a Pixel factory image's build.prop over HTTP Range.

The flashstation helpers (`list_builds`, `latest_build`) resolve the factory image URLs for the
beta/canary channels. The Range reader pulls build.prop out of a factory image without downloading
the whole ~4 GB zip, in seconds:

    factory.zip  ->  image-<build>.zip   (STORED inside, so its bytes are addressable)
                     |- system_dlkm.img  (~1 MB)  -> device identity + real fingerprint
                     '- system.img       (streamed, stops at the first match) -> security_patch, SDK

Both are EROFS and keep build.prop as plain text, so each member is inflated in memory and the stream
is dropped as soon as the properties appear - nothing touches disk.

Note on fingerprints: ro.system.build.fingerprint in system.img is the generic system image's
(google/generic_system_google/generic:...). The device fingerprint (google/<product>/<device>:...)
lives in ro.product.build.fingerprint (product.img, expensive) and identically in
ro.system_dlkm.build.fingerprint (~1 MB, cheap) - hence reading system_dlkm.
"""
import json
import re
import struct
import time
import urllib.request
import zlib

UA = "Mozilla/5.0 (X11; Linux x86_64) pixel_factory/1.0"
FLASH_HOME = "https://flash.android.com"
FLASH_API = "https://content-flashstation-pa.googleapis.com/v1/builds"


class FactoryError(RuntimeError):
    """Falha ao ler a factory. É lib: levanta, não chama sys.exit."""


def _noop(_msg):
    pass


# --------------------------------------------------------------------------- HTTP
def _http(url, headers=None, retries=4):
    """GET com retry. Devolve a resposta ABERTA (quem chama lê e fecha)."""
    ultimo = None
    for tentativa in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
            return urllib.request.urlopen(req, timeout=60)
        except Exception as exc:  # noqa: BLE001 - rede falha, tenta de novo
            ultimo = exc
            time.sleep(2 * (tentativa + 1))
    raise FactoryError(f"GET {url}: {ultimo}")


def _get_bytes(url, start=None, end=None, headers=None):
    headers = dict(headers or {})
    if start is not None:
        headers["Range"] = f"bytes={start}-" + ("" if end is None else str(end))
    with _http(url, headers) as resp:
        return resp.read()


def _content_length(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        if resp.headers.get("Accept-Ranges") != "bytes":
            raise FactoryError(f"o servidor não aceita Range: {url}")
        return int(resp.headers["Content-Length"])


# --------------------------------------------------------------------------- API do flashstation
def latest_build(product="comet_beta", track="canary"):
    """Build mais novo publicado para `product`. dict com build_id, name, url e track."""
    page = _http(FLASH_HOME).read().decode("utf-8", "replace")
    m = re.search(r"<body data-client-config=[^;]*;([^&\"]+)", page)
    if not m:
        raise FactoryError("não consegui ler a chave da API do flash.android.com")
    dados = json.loads(_get_bytes(f"{FLASH_API}?product={product}&key={m.group(1)}",
                                  headers={"Referer": FLASH_HOME}))   # a API exige o Referer
    builds = dados.get("flashstationBuild") or []
    if not builds:
        raise FactoryError(f"a API não devolveu build para product={product}")

    def serve(b):
        meta = b.get("previewMetadata") or {}
        if track == "canary":
            return bool(meta.get("canary"))
        if track == "beta":
            return not meta.get("canary")
        return True

    escolhidos = [b for b in builds if serve(b) and b.get("factoryImageDownloadUrl")]
    if not escolhidos:
        raise FactoryError(f"nenhum build casa com track={track} em product={product}")
    melhor = max(escolhidos, key=lambda b: int(b.get("buildId") or 0))
    return {"build_id": melhor["buildId"], "name": melhor.get("releaseCandidateName", ""),
            "url": melhor["factoryImageDownloadUrl"],
            "track": ((melhor.get("previewMetadata") or {}).get("releaseTrackVersionName") or track)}


def list_builds(product="comet_beta"):
    """TODOS os builds servidos para `product` (beta E canary), do mais novo pro mais velho.
    Lista de dicts: build_id, name, url, track, canary. Usado p/ montar o corpus dos N mais recentes."""
    page = _http(FLASH_HOME).read().decode("utf-8", "replace")
    m = re.search(r"<body data-client-config=[^;]*;([^&\"]+)", page)
    if not m:
        raise FactoryError("nao consegui ler a chave da API do flash.android.com")
    dados = json.loads(_get_bytes(f"{FLASH_API}?product={product}&key={m.group(1)}",
                                  headers={"Referer": FLASH_HOME}))
    out = []
    for b in (dados.get("flashstationBuild") or []):
        if not b.get("factoryImageDownloadUrl"):
            continue
        meta = b.get("previewMetadata") or {}
        out.append({"build_id": b["buildId"], "name": b.get("releaseCandidateName", ""),
                    "url": b["factoryImageDownloadUrl"],
                    "track": meta.get("releaseTrackVersionName") or ("canary" if meta.get("canary") else "beta"),
                    "canary": bool(meta.get("canary"))})
    out.sort(key=lambda x: int(x["build_id"] or 0), reverse=True)
    return out


# --------------------------------------------------------------------------- zip por HTTP
def _zip64_extra(extra, csz, usz, lho):
    """Troca os marcadores 0xFFFFFFFF pelos valores do campo extra zip64."""
    pos = 0
    while pos + 4 <= len(extra):
        hid, hsz = struct.unpack("<HH", extra[pos:pos + 4])
        if hid == 0x0001:
            blob, off = extra[pos + 4:pos + 4 + hsz], 0
            for nome in ("usz", "csz", "lho"):
                if (nome == "usz" and usz != 0xFFFFFFFF) or \
                   (nome == "csz" and csz != 0xFFFFFFFF) or \
                   (nome == "lho" and lho != 0xFFFFFFFF):
                    continue
                if off + 8 > len(blob):
                    break
                val = struct.unpack("<Q", blob[off:off + 8])[0]
                off += 8
                if nome == "usz":
                    usz = val
                elif nome == "csz":
                    csz = val
                else:
                    lho = val
        pos += 4 + hsz
    return csz, usz, lho


class RemoteZip:
    """Diretório central de um zip servido por HTTP, endereçado a partir de `base` (offset absoluto)."""

    def __init__(self, url, base=0, size=None):
        self.url, self.base = url, base
        self.size = size if size is not None else _content_length(url)
        self.entries = self._ler_diretorio_central()

    def _ler_diretorio_central(self):
        cauda_n = min(self.size, 66000)
        cauda = _get_bytes(self.url, self.base + self.size - cauda_n, self.base + self.size - 1)
        pos = cauda.rfind(b"PK\x05\x06")
        if pos < 0:
            raise FactoryError(f"fim do diretório central não encontrado em {self.url}")
        cd_size, cd_off = struct.unpack("<II", cauda[pos + 12:pos + 20])
        loc = cauda.rfind(b"PK\x06\x07")          # zip64, só quando o zip precisa
        if loc >= 0:
            eocd64_off = struct.unpack("<Q", cauda[loc + 8:loc + 16])[0]
            head = _get_bytes(self.url, self.base + eocd64_off, self.base + eocd64_off + 55)
            cd_size, cd_off = struct.unpack("<QQ", head[40:56])
        cd = _get_bytes(self.url, self.base + cd_off, self.base + cd_off + cd_size - 1)

        entries, pos = {}, 0
        while pos + 46 <= len(cd) and cd[pos:pos + 4] == b"PK\x01\x02":
            meth, csz, usz, nlen, elen, clen, lho = struct.unpack(
                "<H8xIIHHH8xI", cd[pos + 10:pos + 46])
            nome = cd[pos + 46:pos + 46 + nlen].decode("utf-8", "replace")
            extra = cd[pos + 46 + nlen:pos + 46 + nlen + elen]
            if 0xFFFFFFFF in (csz, usz, lho):
                csz, usz, lho = _zip64_extra(extra, csz, usz, lho)
            entries[nome] = {"method": meth, "csize": csz, "usize": usz, "lho": lho}
            pos += 46 + nlen + elen + clen
        if not entries:
            raise FactoryError(f"diretório central vazio em {self.url}")
        return entries

    def data_offset(self, nome):
        """Offset absoluto do conteúdo do membro (o cabeçalho local traz os próprios tamanhos)."""
        e = self.entries[nome]
        head = _get_bytes(self.url, self.base + e["lho"], self.base + e["lho"] + 29)
        if head[:4] != b"PK\x03\x04":
            raise FactoryError(f"cabeçalho local quebrado em {nome}")
        nlen, elen = struct.unpack("<HH", head[26:30])
        return self.base + e["lho"] + 30 + nlen + elen

    def scan_props(self, nome, agulha, window=65536, chunk=1 << 20, log=_noop):
        """Faz streaming do membro e devolve o texto do build.prop em volta do 1º acerto."""
        e = self.entries[nome]
        if e["method"] not in (0, 8):
            raise FactoryError(f"{nome}: método de compressão {e['method']} não suportado")
        inicio = self.data_offset(nome)
        dec = zlib.decompressobj(-zlib.MAX_WBITS) if e["method"] == 8 else None
        lidos, buf = 0, b""
        with _http(self.url, {"Range": f"bytes={inicio}-{inicio + e['csize'] - 1}"}) as resp:
            while lidos < e["csize"]:
                bloco = resp.read(chunk)
                if not bloco:
                    break
                lidos += len(bloco)
                buf += dec.decompress(bloco) if dec else bloco
                hit = buf.find(agulha)
                if hit < 0:
                    buf = buf[-(window + len(agulha)):]      # segura um acerto que caia na emenda
                elif len(buf) - hit >= window:
                    log(f"    {nome}: props achadas após {lidos / 1e6:.0f} MB")
                    return buf[max(0, hit - window):hit + window]
                else:
                    buf = buf[max(0, hit - window):]         # guarda o contexto e lê o resto
        hit = buf.find(agulha)
        if hit >= 0:
            log(f"    {nome}: props achadas após {lidos / 1e6:.0f} MB")
            return buf[max(0, hit - window):hit + window]
        raise FactoryError(f"{nome}: '{agulha.decode()}' não achado após {lidos / 1e6:.0f} MB")


_LINHA_PROP = re.compile(r"^[A-Za-z0-9_.\-]+=[^\x00-\x08\x0b-\x1f\x7f]*$")


def parse_props(blob, agulha):
    """Props do ÚNICO build.prop que contém `agulha` (a janela pode encostar em outros arquivos)."""
    linhas = blob.decode("utf-8", "replace").splitlines()
    ancora = next((i for i, ln in enumerate(linhas) if agulha.decode() in ln), None)
    if ancora is None:
        return {}

    def eh_prop(ln):
        return ln == "" or ln.startswith("#") or bool(_LINHA_PROP.match(ln))

    primeira = ancora
    while primeira > 0 and eh_prop(linhas[primeira - 1]):
        primeira -= 1
    ultima = ancora
    while ultima + 1 < len(linhas) and eh_prop(linhas[ultima + 1]):
        ultima += 1

    props = {}
    for linha in linhas[primeira:ultima + 1]:
        if linha.startswith("ro.") and "=" in linha:
            chave, val = linha.split("=", 1)
            props.setdefault(chave.strip(), val.strip())
    return props


def parse_all_props(blob):
    """TODAS as `ro.*=...` da janela (nao so o bloco contiguo). Para o build.prop monolitico do
    system.img de Pixel sem `system_dlkm` (P6/6a), onde identidade e versao vem num unico scan."""
    props = {}
    for linha in blob.decode("utf-8", "replace").splitlines():
        if linha.startswith("ro.") and "=" in linha and _LINHA_PROP.match(linha):
            chave, val = linha.split("=", 1)
            props.setdefault(chave.strip(), val.strip())
    return props


# the two cheapest images that answer the identity/version props, cheapest first
AGULHA_DLKM = b"ro.product.system_dlkm.brand="
AGULHA_SYSTEM = b"ro.build.version.security_patch="


def collect_props(factory_url, log=_noop):
    """Props das duas imagens mais baratas da factory. dict `ro.*` -> valor."""
    log(f"  factory (Range, sem baixar): {factory_url}")
    externo = RemoteZip(factory_url)
    interno_nome = next((n for n in externo.entries if re.search(r"/image-.*\.zip$", n)), None)
    if not interno_nome:
        raise FactoryError("image-*.zip não achado dentro da factory")
    if externo.entries[interno_nome]["method"] != 0:
        raise FactoryError(f"{interno_nome} está comprimido; não dá para endereçar por Range")
    interno = RemoteZip(factory_url, base=externo.data_offset(interno_nome),
                        size=externo.entries[interno_nome]["csize"])

    props = {}
    if "system_dlkm.img" in interno.entries:
        # Pixel 8+: identidade + FINGERPRINT + UUID no system_dlkm (~1 MB); o resto no system.img
        props.update(parse_props(interno.scan_props("system_dlkm.img", AGULHA_DLKM,
                                                    window=8192, log=log), AGULHA_DLKM))
        props.update(parse_props(interno.scan_props("system.img", AGULHA_SYSTEM, log=log),
                                 AGULHA_SYSTEM))
    else:
        # Pixel 6/6a (sem system_dlkm): o system.img e 640MB deflate (inviavel). A MESMA factory
        # oficial traz tudo em 2 membros pequenos: vendor_dlkm (~17MB: fingerprint REAL + identidade
        # + versoes/uuid/id) e vendor (security_patch + board + first_api_level).
        props.update(parse_all_props(interno.scan_props("vendor_dlkm.img",
                     b"ro.vendor_dlkm.build.fingerprint=", window=131072, log=log)))
        props.update(parse_all_props(interno.scan_props("vendor.img",
                     b"ro.vendor.build.security_patch=", window=131072, log=log)))
    return props


def como_build_prop(props):
    """Serializa as props num texto `chave=valor` - para arquivar no formato de sempre.

    Fills ro.product.build.fingerprint from ro.system_dlkm.build.fingerprint when missing: they are
    the same value, and it is the key consumers look for first.
    """
    props = dict(props)
    fp = props.get("ro.system_dlkm.build.fingerprint")
    if fp and not props.get("ro.product.build.fingerprint"):
        props["ro.product.build.fingerprint"] = fp
    cab = ("# gerado por Libs/pixel_factory.py (leitura por HTTP Range - a factory NÃO foi baixada)\n"
           "# fonte: system_dlkm.img + system.img da factory do flashstation\n")
    return cab + "".join(f"{k}={v}\n" for k, v in sorted(props.items()))
