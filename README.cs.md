[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | **Čeština** | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Procházitelný, automaticky aktualizovaný archiv skutečných dat `build.prop` pro Pixel, přímo z oficiálních obrazů Googlu*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Verzovaný archiv **posledních 4 sestavení z každého kanálu** (stable, beta a canary) pro každý současný Pixel, extrahovaný přímo z oficiálních továrních a OTA obrazů Googlu. Každá položka je **kompletní** `build.prop`, sloučený napříč **všemi oddíly** (system, system_ext, product, vendor, odm a obrazy `_dlkm`), a obsahuje **`ro.boot.vbmeta.digest`** (hash verified boot). Vše je uloženo v repozitáři, indexováno ve strojově čitelném `index.json` a publikováno jako přílohy vydání. Nejsou potřeba žádné nástroje.

## 📥 Získat data

Tři způsoby, bez nutnosti nastavení:

- **Procházet repozitář** - otevřete [`<codename>/`](.) a vyberte soubor. Pojmenování podle kanálu:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - strojově čitelný manifest mapující každé zařízení → kanál → nejnovější sestavení, s `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` a `vbmeta_digest`. Ideální pro automatizaci a nástroje.
- **Vydání** - stáhněte celý korpus jako jeden `.zip` (plus `index.json`) z nejnovějšího [vydání](https://github.com/VictorGabriel7Dev/build.prop/releases) (se značkou `build-YYYYMMDD`).

Každý `.prop` je kompletní, uspořádaná sada vlastností pro přesně dané zařízení a sestavení - všechny oddíly, plus `ro.boot.vbmeta.digest`.

## 🗂️ Co je uvnitř

- **Každé současné zařízení Pixel** (Pixel 6 a novější).
- **Tři kanály na zařízení** - stable, beta a canary, nejnovější sestavení každého z nich (podle toho, co Google skutečně publikuje; některá zcela nová zařízení mají zatím jen jedno nebo dvě sestavení na canary).
- **Kompletní `build.prop`** na každé sestavení (~300-390 vlastností), sloučený ze všech oddílů.
- **`vbmeta.digest`** (hash verified boot) uložený spolu s vlastnostmi.

## 🔧 Sestavit svépomocí

Chcete-li extrahovat jeden `.prop` lokálně místo jeho stažení, potřebujete prostředí podobné Unixu (Linux nebo macOS s Bash) plus `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` a Python ≥3.8 s `payload_dumper`. `requirements.sh` nainstaluje závislosti ve většině správců balíčků (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Podporovaná zařízení jsou tovární a OTA obrazy na [Google Android Images](https://developers.google.com/android/images) a [stránkách Beta OTA](https://developer.android.com/about/versions/17/download-ota). Extrakce čte každý oddíl payloadu po jednom (nízká spotřeba paměti) a zpracovává obrazy EROFS, ext4, sparse a boot/init_boot.

## 🤖 Automatizace

Archiv se automaticky udržuje aktuální: jakmile Google publikuje nová sestavení, jsou extrahována (kompletně, všechny oddíly, s `vbmeta.digest`), nové `.prop` jsou commitovány do `<codename>/`, `index.json` je obnoven a je vytvořeno datované vydání (`build-YYYYMMDD`), aby byli sledující upozorněni na každou vlnu.

K dispozici je také obecný `.github/workflows/build.yml` na vyžádání (`workflow_dispatch`) jako ruční záložní možnost pro sestavení nejnovějšího `.prop` zařízení.

## Poděkování

Tento projekt je fork **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** od **[@T3SL4](https://github.com/T3SL4)**, který jako první vytvořil pipeline pro extrakci prop z OTA. Veškeré uznání za původní práci patří jejímu autorovi.

## Kontakt

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licence

**GNU GPL-3.0-or-later** - viz [LICENSE](LICENSE). Copyleft: každý, kdo distribuuje upravenou verzi, musí nabídnout její zdrojový kód za stejných podmínek.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
