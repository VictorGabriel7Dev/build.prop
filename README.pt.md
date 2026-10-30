[English](README.md) | **Português** | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Um acervo navegável e atualizado automaticamente de dados reais de `build.prop` de Pixel, direto das imagens oficiais do Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Um acervo versionado dos **4 últimos builds de cada canal** (stable, beta e canary) de cada Pixel recente, extraído diretamente das imagens oficiais de fábrica e OTA do Google. Cada entrada é o `build.prop` **completo**, mesclado de **todas as partições** (system, system_ext, product, vendor, odm e as imagens `_dlkm`), e traz o **`ro.boot.vbmeta.digest`** (hash do verified boot). Tudo é armazenado no repositório, indexado em um `index.json` legível por máquina e publicado como assets de release. Nenhuma ferramenta necessária.

## 📥 Obtenha os dados

Três maneiras, sem configuração necessária:

- **Navegue pelo repositório** - abra [`<codename>/`](.) e escolha um arquivo. Nomenclatura por canal:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - um manifesto legível por máquina que mapeia cada aparelho → canal → build mais recente, com `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` e `vbmeta_digest`. Ideal para automação e ferramentas.
- **Releases** - baixe todo o corpus como um único `.zip` (mais o `index.json`) da [release](https://github.com/VictorGabriel7Dev/build.prop/releases) mais recente (com a tag `build-YYYYMMDD`).

Cada `.prop` é o conjunto completo e organizado de propriedades daquele aparelho e build exatos - todas as partições, mais o `ro.boot.vbmeta.digest`.

## 🗂️ O que há dentro

- **Todo Pixel recente** (Pixel 6 e mais novos).
- **Três canais por aparelho** - stable, beta e canary, os builds mais recentes de cada (sujeito ao que o Google realmente publica; alguns aparelhos recém-lançados ainda têm só um ou dois builds no canary).
- **`build.prop` completo** por build (~300-390 propriedades), mesclado de todas as partições.
- **`vbmeta.digest`** (o hash do verified boot) armazenado junto das propriedades.

## 🔧 Compile você mesmo

Para extrair um único `.prop` localmente em vez de baixá-lo, você precisa de um ambiente Unix-like (Linux ou macOS com Bash) além de `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` e Python ≥3.8 com `payload_dumper`. O `requirements.sh` instala as dependências na maioria dos gerenciadores de pacotes (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Os aparelhos suportados são as imagens de fábrica e OTA em [Google Android Images](https://developers.google.com/android/images) e nas [páginas de OTA Beta](https://developer.android.com/about/versions/17/download-ota). A extração lê cada partição do payload uma de cada vez (baixo consumo de memória) e lida com imagens EROFS, ext4, sparse e boot/init_boot.

## 🤖 Automação

O acervo se mantém atualizado automaticamente: conforme o Google publica novos builds, eles são extraídos (completos, todas as partições, com `vbmeta.digest`), os novos `.prop` são commitados em `<codename>/`, o `index.json` é atualizado e uma release datada (`build-YYYYMMDD`) é criada para que os watchers sejam notificados a cada leva.

Um `.github/workflows/build.yml` genérico e sob demanda também está disponível (`workflow_dispatch`) como alternativa manual para compilar o `.prop` mais recente de um aparelho.

## Agradecimentos

Este projeto é um fork de **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** de **[@T3SL4](https://github.com/T3SL4)**, que foi pioneiro no pipeline de extração de OTA para prop. Todo o crédito pelo trabalho original é do seu autor.

## Contato

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licença

**GNU GPL-3.0-or-later** - veja [LICENSE](LICENSE). Copyleft: quem distribuir uma versão modificada deve oferecer o código-fonte dela sob os mesmos termos.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
