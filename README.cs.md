[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | **Čeština** | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Procházitelný, automaticky aktualizovaný archiv skutečných souborů `.prop` pro Pixel, přímo z OTA obrazů Googlu*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Verzovaný archiv kompletního `build.prop` každého Pixelu, extrahovaný přímo z oficiálních OTA obrazů Googlu a automaticky udržovaný aktuální. Soubor `.prop` každého zařízení je uložen v repozitáři a publikován jako příloha vydání, připravený k procházení nebo stažení bez jakýchkoli nástrojů.

## 📥 Získat `.prop`

Dva způsoby, bez nutnosti nastavení:

- **Procházet repozitář**: otevřete [`props/<codename>/`](props/) a vyberte `<codename>_<build_id>.prop`.
- **Stáhnout z vydání**: získejte soubor z nejnovějšího [vydání](https://github.com/VictorGabriel7Dev/build.prop/releases) (se značkou `build-YYYYMMDD`).

Každý `.prop` je kompletní, uspořádaná sada vlastností sestavení pro přesně dané zařízení a sestavení (product, vendor, odm, system, system_ext, system_dlkm a další).

## 🔧 Sestavit svépomocí

Chcete-li extrahovat `.prop` lokálně místo jeho stažení, potřebujete prostředí podobné Unixu (Linux nebo macOS s Bash) plus `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` a Python ≥3.8 s `payload_dumper`. `requirements.sh` nainstaluje závislosti ve většině správců balíčků (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
pip3 install payload_dumper
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Podporovaná zařízení jsou tovární a OTA obrazy na [Google Android Images](https://developers.google.com/android/images) a [stránkách Beta OTA](https://developer.android.com/about/versions/17/download-ota). Extrakce čte každý oddíl payloadu po jednom (nízká spotřeba paměti) a zpracovává obrazy EROFS, ext4, sparse a boot/init_boot.

## 🤖 Automatizace

Pipeline GitHub Actions (`.github/workflows/build.yml`) udržuje archiv aktuální:

- Běží týdně a na vyžádání přes `workflow_dispatch` se seznamem zařízení odděleným mezerami nebo `all`; každé zařízení se sestavuje paralelně.
- Extrahuje `.prop`, commituje nové soubory do `props/<codename>/` a publikuje je jako přílohy pod jednou denní značkou (`build-YYYYMMDD`).
- Přeskakuje soubory `.prop`, které již byly vydány, a upozorňuje Telegram s klikatelnými odkazy ke stažení.

Forky, které spouštějí pipeline, potřebují dvě tajemství: `TELEGRAM_BOT_TOKEN` (od [@BotFather](https://t.me/BotFather)) a `TELEGRAM_CHAT_ID`.

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

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
