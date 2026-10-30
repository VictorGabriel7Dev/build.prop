[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | **Nederlands** | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Een doorzoekbaar, automatisch bijgewerkt archief van echte Pixel-`build.prop`-gegevens, rechtstreeks uit Googles officiële images*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Een geversioneerd archief van de **laatste 4 builds van elk kanaal** (stable, beta en canary) voor elke recente Pixel, rechtstreeks uit Googles officiële factory- en OTA-images geëxtraheerd. Elk item is de **volledige** `build.prop`, samengevoegd over **elke partitie** (system, system_ext, product, vendor, odm en de `_dlkm`-images), en bevat de **`ro.boot.vbmeta.digest`** (verified boot-hash). Alles wordt in de repository opgeslagen, geïndexeerd in een machineleesbare `index.json` en gepubliceerd als release-assets. Geen gereedschap nodig.

## 📥 Get the data

Drie manieren, geen installatie nodig:

- **Doorzoek de repository** - open [`<codename>/`](.) en kies een bestand. Naamgeving per kanaal:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - een machineleesbaar manifest dat elk apparaat → kanaal → nieuwste build koppelt, met `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` en `vbmeta_digest`. Ideaal voor automatisering en tooling.
- **Releases** - download het hele corpus als één `.zip` (plus `index.json`) uit de nieuwste [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (getagd met `build-YYYYMMDD`).

Elke `.prop` is de volledige, geordende set eigenschappen voor precies dat apparaat en die build - alle partities, plus `ro.boot.vbmeta.digest`.

## 🗂️ What's inside

- **Elk recent Pixel-apparaat** (Pixel 6 en nieuwer).
- **Drie kanalen per apparaat** - stable, beta en canary, de nieuwste builds van elk (afhankelijk van wat Google daadwerkelijk publiceert; sommige gloednieuwe apparaten hebben voorlopig pas een build of twee op canary).
- **Volledige `build.prop`** per build (~300-390 eigenschappen), samengevoegd uit alle partities.
- **`vbmeta.digest`** (de verified boot-hash) opgeslagen naast de eigenschappen.

## 🔧 Build one yourself

Om één `.prop` lokaal te extraheren in plaats van hem te downloaden, heb je een Unix-achtige omgeving nodig (Linux of macOS met Bash) plus `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` en Python ≥3.8 met `payload_dumper`. `requirements.sh` installeert de afhankelijkheden voor de meeste pakketbeheerders (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Ondersteunde apparaten zijn de factory- en OTA-images op [Google Android Images](https://developers.google.com/android/images) en de [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). De extractie leest elke payload-partitie één voor één (laag geheugengebruik) en verwerkt EROFS-, ext4-, sparse- en boot/init_boot-images.

## 🤖 Automation

Het archief blijft automatisch actueel: zodra Google nieuwe builds publiceert, worden ze geëxtraheerd (volledig, alle partities, met `vbmeta.digest`), de nieuwe `.prop` worden vastgelegd onder `<codename>/`, `index.json` wordt vernieuwd en er wordt een gedateerde release (`build-YYYYMMDD`) uitgebracht, zodat volgers van elke golf op de hoogte worden gebracht.

Er is ook een generieke `.github/workflows/build.yml` op aanvraag beschikbaar (`workflow_dispatch`) als handmatige terugvaloptie om de nieuwste `.prop` van een apparaat te bouwen.

## Acknowledgements

Dit project is een fork van **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** door **[@T3SL4](https://github.com/T3SL4)**, die de OTA-naar-prop-extractiepijplijn als eerste ontwikkelde. Alle erkenning voor het oorspronkelijke werk gaat naar de auteur ervan.

## Contact

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - zie [LICENSE](LICENSE). Copyleft: wie een gewijzigde versie verspreidt, moet de broncode ervan onder dezelfde voorwaarden aanbieden.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
