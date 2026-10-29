[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | **Deutsch** | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Ein durchsuchbares, automatisch aktualisiertes Archiv echter Pixel-`.prop`-Dateien, direkt aus Googles OTA-Images*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Ein versioniertes Archiv der vollständigen `build.prop` jedes Pixel, direkt aus Googles offiziellen OTA-Images extrahiert und automatisch auf dem neuesten Stand gehalten. Die `.prop` jedes Geräts wird im Repository gespeichert und als Release-Asset veröffentlicht, bereit zum Durchsuchen oder Herunterladen, ohne dass Werkzeuge erforderlich sind.

## 📥 Get a `.prop`

Zwei Wege, keine Einrichtung nötig:

- **Das Repository durchsuchen**: öffne [`<codename>/`](.) und wähle `<codename>_<build_id>.prop`.
- **Aus den Releases herunterladen**: hol dir die Datei aus dem neuesten [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (getaggt mit `build-YYYYMMDD`).

Jede `.prop` ist der vollständige, organisierte Satz der Build-Eigenschaften für genau dieses Gerät und diesen Build (product, vendor, odm, system, system_ext, system_dlkm und mehr).

## 🔧 Build it yourself

Um eine `.prop` lokal zu extrahieren, statt sie herunterzuladen, brauchst du eine Unix-ähnliche Umgebung (Linux oder macOS mit Bash) sowie `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` und Python ≥3.8 mit `payload_dumper`. `requirements.sh` installiert die Abhängigkeiten über die meisten Paketmanager hinweg (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Unterstützte Geräte sind die Factory- und OTA-Images auf [Google Android Images](https://developers.google.com/android/images) und den [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Die Extraktion liest jede Payload-Partition einzeln nacheinander (geringer Speicherbedarf) und verarbeitet EROFS-, ext4-, sparse- und boot/init_boot-Images.

## 🤖 Automation

Eine GitHub-Actions-Pipeline (`.github/workflows/build.yml`) hält das Archiv aktuell:

- Läuft wöchentlich und bei Bedarf über `workflow_dispatch` mit einer durch Leerzeichen getrennten Geräteliste oder `all`; jedes Gerät wird parallel gebaut.
- Extrahiert die `.prop`, committet neue unter `<codename>/` und veröffentlicht sie als Assets unter einem einzigen täglichen Tag (`build-YYYYMMDD`).
- Überspringt `.prop`-Dateien, die bereits veröffentlicht wurden, und benachrichtigt Telegram mit anklickbaren Download-Links.

Forks, die die Pipeline ausführen, benötigen zwei Secrets: `TELEGRAM_BOT_TOKEN` (von [@BotFather](https://t.me/BotFather)) und `TELEGRAM_CHAT_ID`.

## Acknowledgements

Dieses Projekt ist ein Fork von **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** von **[@T3SL4](https://github.com/T3SL4)**, das die OTA-zu-prop-Extraktionspipeline begründet hat. Die volle Anerkennung für die ursprüngliche Arbeit gebührt ihrem Autor.

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

**GNU GPL-3.0-or-later** - siehe [LICENSE](LICENSE). Copyleft: Wer eine modifizierte Version verteilt, muss deren Quellcode zu denselben Bedingungen anbieten.

---

`android` `pixel` `build-prop` `ota` `factory-image` `system-properties` `system-properties` `automation`
