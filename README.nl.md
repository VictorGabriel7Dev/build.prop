[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | **Nederlands** | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Een doorzoekbaar, automatisch bijgewerkt archief van echte Pixel-`.prop`-bestanden, rechtstreeks uit Googles OTA-images*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Een geversioneerd archief van de volledige `build.prop` van elke Pixel, rechtstreeks uit Googles officiële OTA-images geëxtraheerd en automatisch up-to-date gehouden. De `.prop` van elk apparaat wordt in de repository opgeslagen en als release-asset gepubliceerd, klaar om te doorbladeren of te downloaden zonder dat er gereedschap nodig is.

## 📥 Get a `.prop`

Twee manieren, geen installatie nodig:

- **Doorzoek de repository**: open [`props/<codename>/`](props/) en kies `<codename>_<build_id>.prop`.
- **Download uit Releases**: pak het bestand uit de nieuwste [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (getagd met `build-YYYYMMDD`).

Elke `.prop` is de volledige, geordende set build-eigenschappen voor precies dat apparaat en die build (product, vendor, odm, system, system_ext, system_dlkm en meer).

## 🔧 Build it yourself

Om een `.prop` lokaal te extraheren in plaats van hem te downloaden, heb je een Unix-achtige omgeving nodig (Linux of macOS met Bash) plus `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` en Python ≥3.8 met `payload_dumper`. `requirements.sh` installeert de afhankelijkheden voor de meeste pakketbeheerders (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
pip3 install payload_dumper
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Ondersteunde apparaten zijn de factory- en OTA-images op [Google Android Images](https://developers.google.com/android/images) en de [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). De extractie leest elke payload-partitie één voor één (laag geheugengebruik) en verwerkt EROFS-, ext4-, sparse- en boot/init_boot-images.

## 🤖 Automation

Een GitHub Actions-pijplijn (`.github/workflows/build.yml`) houdt het archief actueel:

- Draait wekelijks en op aanvraag via `workflow_dispatch` met een door spaties gescheiden apparatenlijst of `all`; elk apparaat wordt parallel gebouwd.
- Extraheert de `.prop`, commit nieuwe onder `props/<codename>/` en publiceert ze als assets onder één enkele dagelijkse tag (`build-YYYYMMDD`).
- Slaat `.prop`-bestanden over die al zijn uitgebracht en stuurt een melding naar Telegram met aanklikbare downloadlinks.

Forks die de pijplijn draaien, hebben twee secrets nodig: `TELEGRAM_BOT_TOKEN` (van [@BotFather](https://t.me/BotFather)) en `TELEGRAM_CHAT_ID`.

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

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
