#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B TOTAL: build.prop COMPLETO (todas as particoes) p/ os 3 canais, ultimos N de cada.

- stable  : OTA zip oficial (developers.google.com/android/ota) -> payload.bin -> payload_dumper.
- beta/canary : factory do flashstation -> image-*.zip -> *.img (ou super.img via lpunpack).
Para cada build mescla o build.prop de TODAS as particoes (~320 props), ARQUIVA os per-particao,
computa o `ro.boot.vbmeta.digest` (= verifiedBootHash) e escreve `<fork>/<cn>/<cn>[_track]_<inc>.prop`.

Uso: pixel_fullprop.py [--only cheetah,comet] [--tracks stable,beta,canary] [--per-track 4]
                       [--slice i/n] [--fork DIR] [--acervo DIR] [--tmp DIR] [--force]
                       [--lowdisk] [--workers N] [--dry-run]
"""
import sys, os, re, json, subprocess, tempfile, shutil, glob, pathlib, importlib.util, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
LIB = HERE / "pixel_factory.py"
_s = importlib.util.spec_from_file_location("pixel_factory", LIB)
pf = importlib.util.module_from_spec(_s); _s.loader.exec_module(pf)

PROFILES = HERE / "pixel_profiles.json"
# bases das particoes (super.img expande p/ estas); aceitamos <base>.img E <base>_a.img (slot A/B)
PART_BASES = ["system", "system_ext", "product", "vendor", "odm", "system_dlkm", "vendor_dlkm"]
OTA_URL = "https://developers.google.com/android/ota?partial=1"
OTA_COOKIE = "devsite_wall_acks=nexus-ota-tos"
UA = "Mozilla/5.0 (X11; Linux x86_64) pixel_fullprop/1.0"

BOX = """# ======================================================================
#  PIXEL PROP BUILDER  ::  Pixel build.prop archive
#  Extract and distribute the full Pixel build.prop from Google's OTA images.
#
#  Copyright (C) 2026  VictorGabriel7Dev
#  SPDX-License-Identifier: GPL-3.0-or-later
#  Fork of Pixel-Props/build.prop by @T3SL4.
#
#  Free software under the GNU GPL v3 or later: distribute a modified
#  version and you MUST offer its source under the same terms.
#
#  Site      : https://victorgabriel.dev
#  Source    : https://github.com/VictorGabriel7Dev/build.prop
#  GitHub    : @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
#  Telegram  : @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
#  Discord   : @VictorGabriel.dev https://discord.com/users/1481407654458036265
#  LinkedIn  : in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
#  Instagram : @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
#  WhatsApp  : @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
#  E-mail    : contato@victorgabriel.dev
# ======================================================================
"""


def _arg(flag, default=None):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default


def sh(cmd, cwd=None, timeout=1800):
    return subprocess.run(cmd, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=timeout)


def download(url, dest, cookie=None, timeout=5400):
    """Baixa url->dest. curl single-stream, RESUMIVEL (-C -), com retry.
    aria2 -x16 foi abandonado: na cauda o dl.google estrangula e os segmentos paralelos
    corrompem o zip ('data after end of archive'). 1 conexao e' lenta mas integra; o paralelismo
    vem de baixar builds DIFERENTES ao mesmo tempo (varios --slice)."""
    dest = pathlib.Path(dest)
    cmd = ["curl", "-fSL", "-C", "-", "--retry", "6", "--retry-delay", "3",
           "--retry-all-errors", "-o", str(dest)]
    if cookie:
        cmd += ["-b", cookie]
    cmd.append(url)
    return sh(cmd, timeout=timeout)


def lpunpack_cmd(raw, outdir):
    """lpunpack binario (android-tools) ou o port python unix3dgforce (lpunpack.py)."""
    b = shutil.which("lpunpack")
    if b:
        return [b, str(raw), str(outdir)]
    pyl = os.environ.get("LPUNPACK_PY") or str(HERE / "lpunpack.py")
    return ["python3", "-I", pyl, str(raw), str(outdir)]


def bp_paths(img):
    r = subprocess.run(["7z", "l", "-slt", img], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    return [ln[7:] for ln in r.stdout.splitlines()
            if ln.startswith("Path = ") and re.search(r"(^|/)build\.prop$", ln[7:])]


def partition_buildprops(img, scratch):
    """Devolve [(relpath, texto)] de cada build.prop da particao. 7z primeiro (rapido); se o 7z nao
    ler a EROFS (Pixel 11 novo: 'Method=Store/Errors') cai pro fsck.erofs --extract (universal)."""
    out = []
    img = pathlib.Path(img)
    for p in bp_paths(str(img)):
        d = pathlib.Path(tempfile.mkdtemp(dir=scratch))
        sh(["7z", "x", "-y", str(img), p, f"-o{d}"])
        src = d / p
        if src.exists():
            out.append((p, src.read_text(errors="replace")))
        shutil.rmtree(d, ignore_errors=True)
    if out:
        return out
    # fallback EROFS: extrai a FS e pega os build.prop
    if shutil.which("fsck.erofs"):
        d = pathlib.Path(tempfile.mkdtemp(dir=scratch))
        try:
            sh(["fsck.erofs", f"--extract={d}", "--overwrite", str(img)], timeout=1200)
            for bp in d.rglob("build.prop"):
                rel = str(bp.relative_to(d))
                out.append((rel, bp.read_text(errors="replace")))
        finally:
            shutil.rmtree(d, ignore_errors=True)
    return out


_OTA_CACHE = {}


def ota_builds(code, n):
    """Ultimos N builds STABLE do codename, da pagina OTA oficial (payload.bin). [{build_id,url}]."""
    if "page" not in _OTA_CACHE:
        req = urllib.request.Request(OTA_URL, headers={"User-Agent": UA, "Cookie": OTA_COOKIE})
        with urllib.request.urlopen(req, timeout=120) as r:
            _OTA_CACHE["page"] = r.read().decode("utf-8", "replace")
    pat = re.compile(r"https://dl\.google\.com/dl/android/aosp/%s-ota-([a-z0-9._]+)-[0-9a-f]+\.zip" % re.escape(code))
    seen, out = set(), []
    for m in pat.finditer(_OTA_CACHE["page"]):
        if m.group(0) not in seen:
            seen.add(m.group(0)); out.append({"build_id": m.group(1), "url": m.group(0)})
    return out[-n:]


def read_bp_from_imgs(imgdir, acdir, prod_build):
    """Le o build.prop de cada particao em imgdir (aceita super.img via lpunpack), ARQUIVA, MESCLA."""
    # super.img (Pixel 11 A16+: particoes dinamicas) -> simg2img + lpunpack
    if not any(glob.glob(str(imgdir / f"{b}*.img")) for b in PART_BASES):
        sup = imgdir / "super.img"
        if sup.exists():
            raw = imgdir / "super.raw"
            sh(["simg2img", str(sup), str(raw)])
            if not raw.exists() or raw.stat().st_size == 0:
                raw = sup                              # ja desensparsa
            sh(lpunpack_cmd(raw, imgdir), timeout=1800)
            if raw != sup:
                raw.unlink(missing_ok=True)
            sup.unlink(missing_ok=True)
    merged, got = {}, 0
    for base in PART_BASES:
        for ip in sorted(glob.glob(str(imgdir / f"{base}.img")) + glob.glob(str(imgdir / f"{base}_a.img"))):
            ip = pathlib.Path(ip)
            for rel, txt in partition_buildprops(ip, imgdir.parent):
                acdir.mkdir(parents=True, exist_ok=True)
                (acdir / f"{prod_build}--{base}--{rel.replace('/', '--')}").write_text(txt)
                for ln in txt.splitlines():
                    if ln.startswith("ro.") and "=" in ln:
                        k, v = ln.split("=", 1); merged.setdefault(k.strip(), v.strip())
                got += 1
            ip.unlink(missing_ok=True)
    return merged, got


def add_vbmeta(imgdir, merged, acdir, prod_build):
    vb = imgdir / "vbmeta.img"
    avb = HERE / "avbtool"
    if not avb.exists():
        _w = shutil.which("avbtool"); avb = pathlib.Path(_w) if _w else avb
    if vb.exists() and avb.exists():
        try:
            r = subprocess.run(["python3", str(avb), "calculate_vbmeta_digest",
                                "--image", "vbmeta.img", "--hash_algorithm", "sha256"],
                               cwd=str(imgdir), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                               text=True, timeout=120)
            dig = (r.stdout.strip().splitlines() or [""])[-1].strip()
            if re.fullmatch(r"[0-9a-f]{64}", dig):
                merged["ro.boot.vbmeta.digest"] = dig
                acdir.mkdir(parents=True, exist_ok=True)
                (acdir / f"{prod_build}--vbmeta.digest").write_text(dig + "\n")
        except Exception:
            pass


def write_prop(out, merged):
    body = "".join(f"{k}={v}\n" for k, v in sorted(merged.items()))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(BOX + "\n" + body)


def extract_factory(code, track, b, fork, acervo, tmp, force, dry, lowdisk):
    """beta/canary: factory do flashstation (image-*.zip + *.img/super.img)."""
    inc = str(b["build_id"])
    out = pathlib.Path(fork) / code / f"{code}_{track}_{inc}.prop"
    if out.exists() and not force:
        # pula so' se JA for full (~320 props); subset antigo (78-87p) re-extrai p/ full
        try:
            if sum(1 for l in out.read_text(errors="replace").splitlines()
                   if l.startswith("ro.") and "=" in l) >= 250:
                return "skip"
        except Exception:
            pass
    fac = b["url"].rsplit("/", 1)[1]
    prod_build = re.sub(r"-factory-.*", "", fac)
    if dry:
        print(f"  [dry] {code}/{out.name}  (factory {prod_build})"); return "dry"
    work = pathlib.Path(tempfile.mkdtemp(dir=tmp, prefix=f"{code}_{track}_"))
    try:
        zf = work / fac
        download(b["url"], zf)
        if not zf.exists() or zf.stat().st_size < 50_000_000:
            print(f"  ! {code} {track} {inc}: download falhou"); return "err"
        sh(["7z", "x", "-y", str(zf)], cwd=str(work)); zf.unlink()
        inner = next(iter(glob.glob(str(work / "**/image-*.zip"), recursive=True)), None)
        if not inner:
            print(f"  ! {code} {track} {inc}: image-*.zip ausente"); return "err"
        inner = pathlib.Path(inner); imgdir = inner.parent
        acdir = pathlib.Path(acervo) / prod_build
        if not lowdisk:
            sh(["7z", "x", "-y", str(inner)], cwd=str(imgdir))
        else:
            for img in [f"{b2}.img" for b2 in PART_BASES] + ["super.img", "vbmeta.img",
                        "vbmeta_system.img", "vbmeta_vendor.img"]:
                sh(["7z", "x", "-y", str(inner), img, f"-o{imgdir}"])
        merged, got = read_bp_from_imgs(imgdir, acdir, prod_build)
        if not merged:
            print(f"  ! {code} {track} {inc}: nenhum build.prop extraido"); return "err"
        add_vbmeta(imgdir, merged, acdir, prod_build)
        write_prop(out, merged)
        print(f"  + {code}/{out.name}  ({len(merged)} props, {got} particoes)")
        return "ok"
    except subprocess.TimeoutExpired:
        print(f"  ! {code} {track} {inc}: TIMEOUT"); return "err"
    finally:
        shutil.rmtree(work, ignore_errors=True)


def extract_url(code, track, build, url, fork, acervo, tmp, force, dry):
    """Extrai de uma URL de FACTORY explicita (fonte: tracker). track='' => stable (sem token).
    Nomeia por ro.build.version.incremental REAL (pos-extracao), como o extract_ota."""
    devdir = pathlib.Path(fork) / code
    tok = f"_{track}" if track and track != "stable" else ""
    bid_up = build.upper()
    if not force:
        for f in glob.glob(str(devdir / f"{code}{tok}_*.prop")):
            try:
                txt = pathlib.Path(f).read_text(errors="replace")
                if f"ro.build.id={bid_up}\n" in txt and \
                   sum(1 for l in txt.splitlines() if l.startswith("ro.") and "=" in l) >= 250:
                    return "skip"   # ja temos esse build FULL
            except Exception:
                pass
    fac = url.rsplit("/", 1)[1]
    prod_build = re.sub(r"-factory-.*", "", fac)
    if dry:
        print(f"  [dry] {code}{tok} {build}"); return "dry"
    work = pathlib.Path(tempfile.mkdtemp(dir=tmp, prefix=f"{code}_{track or 'stable'}_"))
    try:
        zf = work / fac
        download(url, zf)
        if not zf.exists() or zf.stat().st_size < 50_000_000:
            print(f"  ! {code} {track} {build}: download falhou"); return "err"
        sh(["7z", "x", "-y", str(zf)], cwd=str(work)); zf.unlink()
        inner = next(iter(glob.glob(str(work / "**/image-*.zip"), recursive=True)), None)
        if not inner:
            print(f"  ! {code} {track} {build}: image-*.zip ausente"); return "err"
        inner = pathlib.Path(inner); imgdir = inner.parent
        acdir = pathlib.Path(acervo) / prod_build
        sh(["7z", "x", "-y", str(inner)], cwd=str(imgdir))
        merged, got = read_bp_from_imgs(imgdir, acdir, prod_build)
        if not merged:
            print(f"  ! {code} {track} {build}: nenhum build.prop"); return "err"
        add_vbmeta(imgdir, merged, acdir, prod_build)
        real_inc = merged.get("ro.build.version.incremental", build)
        out = devdir / f"{code}{tok}_{real_inc}.prop"
        write_prop(out, merged)
        print(f"  + {code}/{out.name}  ({len(merged)} props, {got} particoes)")
        return "ok"
    except subprocess.TimeoutExpired:
        print(f"  ! {code} {track} {build}: TIMEOUT"); return "err"
    finally:
        shutil.rmtree(work, ignore_errors=True)


def extract_ota(code, b, fork, acervo, tmp, force, dry, workers):
    """stable: OTA zip oficial -> payload.bin -> payload_dumper -> *.img."""
    bid = b["build_id"]
    bid_up = bid.upper()
    devdir = pathlib.Path(fork) / code
    # ja temos esse stable? (ro.build.id casa) -> pula sem baixar
    if not force:
        for f in glob.glob(str(devdir / f"{code}_[0-9]*.prop")):
            try:
                if f"ro.build.id={bid_up}\n" in pathlib.Path(f).read_text(errors="replace"):
                    return "skip"
            except Exception:
                pass
    prod_build = f"{code}-{bid}"
    if dry:
        print(f"  [dry] {code} stable {bid}"); return "dry"
    work = pathlib.Path(tempfile.mkdtemp(dir=tmp, prefix=f"{code}_stable_"))
    try:
        zf = work / b["url"].rsplit("/", 1)[1]
        download(b["url"], zf, cookie=OTA_COOKIE)
        if not zf.exists() or zf.stat().st_size < 50_000_000:
            print(f"  ! {code} stable {bid}: download falhou"); return "err"
        sh(["7z", "e", "-y", str(zf), "payload.bin", f"-o{work}"]); zf.unlink()
        payload = work / "payload.bin"
        if not payload.exists():
            print(f"  ! {code} stable {bid}: payload.bin ausente"); return "err"
        imgdir = work / "out"; imgdir.mkdir()
        # FS + cadeia vbmeta: avbtool calculate_vbmeta_digest precisa de vbmeta + vbmeta_system/vendor
        # + boot/init_boot/dtbo/vendor_boot/... (senao quebra em 'boot.img' ausente). Com eles o stable
        # OTA ganha ro.boot.vbmeta.digest nativo (sem backfill).
        parts = ",".join(PART_BASES + ["vbmeta", "vbmeta_system", "vbmeta_vendor", "boot",
                                       "init_boot", "dtbo", "vendor_boot", "vendor_kernel_boot", "pvmfw"])
        sh(["payload_dumper", "--partitions", parts, "--workers", str(workers),
            "--out", str(imgdir), str(payload)], timeout=2400)
        payload.unlink(missing_ok=True)
        acdir = pathlib.Path(acervo) / prod_build
        merged, got = read_bp_from_imgs(imgdir, acdir, prod_build)
        if not merged:
            print(f"  ! {code} stable {bid}: nenhum build.prop extraido"); return "err"
        add_vbmeta(imgdir, merged, acdir, prod_build)
        real_inc = merged.get("ro.build.version.incremental", bid)
        out = devdir / f"{code}_{real_inc}.prop"
        # grava sempre: o pre-check por ro.build.id ja pulou os FULL existentes; aqui chegam builds
        # novos OU subsets antigos (sem build.id, mesmo incremental) que DEVEM virar full.
        write_prop(out, merged)
        print(f"  + {code}/{out.name}  ({len(merged)} props, {got} particoes)")
        return "ok"
    except subprocess.TimeoutExpired:
        print(f"  ! {code} stable {bid}: TIMEOUT"); return "err"
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main():
    tracks = [t for t in ("stable", "beta", "canary") if t in set(_arg("--tracks", "stable,beta,canary").split(","))]
    only = set(_arg("--only").split(",")) if "--only" in sys.argv else None
    per_track = int(_arg("--per-track", "4"))
    fork = _arg("--fork", ".")
    acervo = _arg("--acervo", str(pathlib.Path(tempfile.gettempdir()) / "buildprop-acervo"))
    tmp = _arg("--tmp", str(pathlib.Path(tempfile.gettempdir()) / "buildprop-work"))
    workers = int(_arg("--workers", "4"))
    force = "--force" in sys.argv
    lowdisk = "--lowdisk" in sys.argv
    dry = "--dry-run" in sys.argv
    os.makedirs(tmp, exist_ok=True)
    if "--from-list" in sys.argv:
        items = json.loads(pathlib.Path(_arg("--from-list")).read_text())
        if "--slice" in sys.argv:
            i, n = (int(x) for x in _arg("--slice").split("/")); items = items[i::n]
        tally = {}
        for cn, track, build, url in items:
            r = extract_url(cn, track, build, url, fork, acervo, tmp, force, dry)
            tally[r] = tally.get(r, 0) + 1; sys.stdout.flush()
        print(f"\nDONE ok:{tally.get('ok',0)} skip:{tally.get('skip',0)} err:{tally.get('err',0)} dry:{tally.get('dry',0)}")
        return
    if PROFILES.exists():
        codenames = list(json.loads(PROFILES.read_text())["pixels"].keys())
        if only:
            codenames = [c for c in codenames if c in only]
    elif only:
        codenames = list(only)   # no profile index here: the device list is the caller's --only
    else:
        print("need --only <device[,device...]> (no pixel_profiles.json present)"); return
    if "--slice" in sys.argv:
        i, n = (int(x) for x in _arg("--slice").split("/")); codenames = codenames[i::n]
    tally = {}
    for code in codenames:
        # stable: pagina OTA
        if "stable" in tracks:
            try:
                for b in ota_builds(code, per_track):
                    r = extract_ota(code, b, fork, acervo, tmp, force, dry, workers)
                    tally[r] = tally.get(r, 0) + 1; sys.stdout.flush()
            except Exception as e:
                print(f"{code}: ota ERRO {type(e).__name__}: {str(e)[:60]}")
        # beta/canary: flashstation
        if "beta" in tracks or "canary" in tracks:
            try:
                builds = pf.list_builds(f"{code}_beta")
            except Exception as e:
                print(f"{code}: list ERRO {type(e).__name__}: {str(e)[:50]}"); continue
            by = {"beta": [], "canary": []}
            for b in builds:
                t = "canary" if b.get("canary") else "beta"
                if t in tracks and len(by[t]) < per_track:
                    by[t].append(b)
            for t in ("beta", "canary"):
                if t in tracks:
                    for b in by[t]:
                        r = extract_factory(code, t, b, fork, acervo, tmp, force, dry, lowdisk)
                        tally[r] = tally.get(r, 0) + 1; sys.stdout.flush()
    print(f"\nDONE ok:{tally.get('ok',0)} skip:{tally.get('skip',0)} err:{tally.get('err',0)} dry:{tally.get('dry',0)}")


if __name__ == "__main__":
    main()
