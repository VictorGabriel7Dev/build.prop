[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | **Deutsch** | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Ein durchsuchbares, automatisch aktualisiertes Archiv echter Pixel-`build.prop`-Daten, direkt aus Googles offiziellen Images*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Ein versioniertes Archiv der **letzten 4 Builds jedes Kanals** (stable, beta und canary) für jedes aktuelle Pixel, direkt aus Googles offiziellen Factory- und OTA-Images extrahiert. Jeder Eintrag ist die **vollständige** `build.prop`, zusammengeführt aus **allen Partitionen** (system, system_ext, product, vendor, odm und den `_dlkm`-Images), und trägt den **`ro.boot.vbmeta.digest`** (Verified-Boot-Hash). Alles wird im Repository gespeichert, in einer maschinenlesbaren `index.json` indexiert und als Release-Assets veröffentlicht. Keine Werkzeuge erforderlich.

## 📥 Die Daten holen

Drei Wege, keine Einrichtung nötig:

- **Das Repository durchsuchen** - öffne [`<codename>/`](.) und wähle eine Datei. Benennung nach Kanal:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - ein maschinenlesbares Manifest, das jedes Gerät → Kanal → neuesten Build abbildet, mit `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` und `vbmeta_digest`. Ideal für Automatisierung und Werkzeuge.
- **Releases** - jede `.prop` wird einzeln (plus `index.json`) an das neueste [release](https://github.com/VictorGabriel7Dev/build.prop/releases) angehängt (getaggt mit `build-YYYYMMDD`).

Jede `.prop` ist der vollständige, organisierte Satz der Eigenschaften für genau dieses Gerät und diesen Build - alle Partitionen, plus `ro.boot.vbmeta.digest`.

## 🗂️ Was enthalten ist

- **Jedes aktuelle Pixel-Gerät** (Pixel 6 und neuer).
- **Drei Kanäle pro Gerät** - stable, beta und canary, jeweils die neuesten Builds (abhängig davon, was Google tatsächlich veröffentlicht; manche brandneuen Geräte haben auf canary noch nur ein oder zwei Builds).
- **Vollständige `build.prop`** pro Build (~300-390 Eigenschaften), aus allen Partitionen zusammengeführt.
- **`vbmeta.digest`** (der Verified-Boot-Hash) neben den Eigenschaften gespeichert.

## 🔧 Selbst bauen

Um eine einzelne `.prop` lokal zu extrahieren, statt sie herunterzuladen, brauchst du eine Unix-ähnliche Umgebung (Linux oder macOS mit Bash) sowie `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` und Python ≥3.8 mit `payload_dumper`. `requirements.sh` installiert die Abhängigkeiten über die meisten Paketmanager hinweg (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Unterstützte Geräte sind die Factory- und OTA-Images auf [Google Android Images](https://developers.google.com/android/images) und den [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Die Extraktion liest jede Payload-Partition einzeln nacheinander (geringer Speicherbedarf) und verarbeitet EROFS-, ext4-, sparse- und boot/init_boot-Images.

## 🤖 Automatisierung

Das Archiv bleibt automatisch aktuell: sobald Google neue Builds veröffentlicht, werden sie extrahiert (vollständig, alle Partitionen, mit `vbmeta.digest`), die neuen `.prop` werden unter `<codename>/` committet, die `index.json` wird aktualisiert und ein datiertes Release (`build-YYYYMMDD`) wird erstellt, sodass Watcher bei jeder Welle benachrichtigt werden.

Eine generische, bedarfsgesteuerte `.github/workflows/build.yml` steht ebenfalls bereit (`workflow_dispatch`) als manuelle Rückfalloption, um die neueste `.prop` eines Geräts zu bauen.

## Danksagungen

Dieses Projekt ist ein Fork von **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** von **[@T3SL4](https://github.com/T3SL4)**, das die OTA-zu-prop-Extraktionspipeline begründet hat. Die volle Anerkennung für die ursprüngliche Arbeit gebührt ihrem Autor.

## Kontakt

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Lizenz

**GNU GPL-3.0-or-later** - siehe [LICENSE](LICENSE). Copyleft: Wer eine modifizierte Version verteilt, muss deren Quellcode zu denselben Bedingungen anbieten.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
