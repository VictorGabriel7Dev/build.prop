[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | **Deutsch** | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Extrahiere und verteile die vollständige Pixel-`.prop` direkt aus Googles OTA-Images*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Extrahiere und verwalte mühelos Systemeigenschaften aus Pixel-OTA-Updates mit dieser robusten Automatisierungs-Suite. Sie extrahiert die vollständige, organisierte `.prop` jedes Geräts direkt aus Googles offiziellen OTA-Images und **speichert und verteilt dann diese `.prop`-Dateien** - sowohl versioniert im Repository als auch als Release-Assets veröffentlicht. Keine installierbaren Module: nur die Eigenschaften.

## 🚀 Schnellstart

### Voraussetzungen

- **Unix-ähnliche Umgebung**: Linux oder macOS mit Bash.
- **Grundlegende Werkzeuge**:
  - `zip`, `unzip`, `p7zip-full`
  - `dos2unix`, `aria2`, `curl`
  - `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`
  - `xxd`, `jq`
- **Python ≥3.8**:

    ```bash
    sudo apt-get update -y
    sudo apt-get install -y python3 python3-pip python3-venv jq xxd \
      p7zip-full e2fsprogs erofs-utils lz4 cpio dos2unix aria2 curl
    ```

## Installation

1. **Klone das Repository**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Erstelle und aktiviere eine virtuelle Umgebung** (optional, aber empfohlen):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Installiere die Abhängigkeiten**:

    ```bash
    pip3 install payload_dumper
    ```

## Verwendung

### Lokal

1. **Lade die neuesten OTA-Images herunter**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Beispiele:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Unterstützte Geräte in den gewünschten Factory- oder OTA-Images von [Google Android Images](https://developers.google.com/android/images) oder den [Beta-OTA-Seiten](https://developer.android.com/about/versions/17/download-ota).

2. **Extrahiere die Images und sammle die `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Dies erledigt automatisch:
    - Extrahiert die Partitionen von payload.bin einzeln (geringer Speicherbedarf)
    - Erkennt und verarbeitet **EROFS**-, **ext4**-, **sparse**- und **boot/init_boot**-Images
    - Baut die vollständige, organisierte `.prop` aus der build.prop jeder Partition
    - Speichert sie unter `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

Das Repository enthält eine vollständig automatisierte CI-Pipeline (`.github/workflows/build.yml`):

- **Geplante Builds**: laufen jeden Sonntag um Mitternacht UTC.
- **Manueller Start**: über `workflow_dispatch` mit einer durch Leerzeichen getrennten Geräteliste oder `all` auslösen.
- **Matrix-Builds**: jedes Gerät wird parallel verarbeitet.
- **Duplikat-Vermeidung**: überspringt `.prop`-Dateien, die bereits in vorhandenen Releases enthalten sind.
- **Versioniert im Repository**: neue `.prop`-Dateien werden unter `props/<codename>/` committet.
- **Gebündelte Releases**: alle neuen `.prop`-Dateien werden unter einem einzigen täglichen Tag (`build-YYYYMMDD`) veröffentlicht.
- **Telegram-Benachrichtigungen**: sendet eine formatierte Nachricht mit anklickbaren Download-Links.

#### Erforderliche Secrets

| Secret | Beschreibung |
|--------|--------------|
| `TELEGRAM_BOT_TOKEN` | Dein Telegram-Bot-Token von [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | Ziel-Chat-ID (Benutzer, Gruppe oder Kanal) |

## ✨ Hauptfunktionen

- **Automatischer OTA-Bezug**: lädt die neuesten Builds direkt aus den offiziellen Google-Quellen herunter.
- **Unterstützung moderner Dateisysteme**: verarbeitet EROFS-, ext4-, sparse-Images sowie boot/init_boot-Ramdisks.
- **Vollständige `.prop`-Erzeugung**: baut eine einzige, organisierte `.prop` pro Gerät aus der build.prop jeder Partition (product, vendor, odm, system, system_ext, system_dlkm und mehr).
- **Speichereffiziente Extraktion**: Payload-Partitionen werden einzeln entpackt, um OOM bei großen OTAs zu vermeiden.
- **Plattformübergreifende Paketverwaltung**: `requirements.sh` unterstützt apt, pacman, dnf, yum, zypper, apk, xbps, brew und Termux.
- **Speicherung und Verteilung**:
  - **Im Repository**: jede `.prop` wird unter `props/<codename>/` committet, versioniert und durchsuchbar.
  - **Als Release-Assets**: jede `.prop` wird unter dem täglichen Tag zum direkten Download veröffentlicht.
- **GitHub-Actions-Integration**:
  - **Geplante Workflows**: automatisieren Updates, Extraktion und Releases nach Zeitplan.
  - **Vermeidung doppelter Releases**: verhindert redundante Releases durch Prüfung vorhandener Release-Assets.
  - **Idempotente Releases**: lädt erneut in ein vorhandenes tägliches Release-Tag hoch, wenn der Lauf wiederholt wird.
  - **Telegram-Benachrichtigungen**: erhalte zeitnahe Updates mit anklickbaren Download-Links.

## 📝 Richtlinien für verantwortungsvolle Nutzung

Dieses Projekt wird zu Bildungs- und Experimentierzwecken bereitgestellt. Obwohl es auf Effizienz ausgelegt ist, ist ein verantwortungsvoller Umgang mit diesem Werkzeug entscheidend.

- **Code-Überprüfung**: prüfe und verstehe den Code gründlich, bevor du ihn in einer Umgebung einsetzt.
- **Bewährte Sicherheitspraktiken**: halte dich an Branchenstandards für Sicherheit und rechtliche Konformität.

Die Ersteller dieses Projekts haften nicht für Missbrauch oder Schäden, die aus seiner Nutzung entstehen.

## Danksagungen

Dieses Projekt ist ein Fork von **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** von **[@T3SL4](https://github.com/T3SL4)**, der die OTA-zu-prop-Extraktionspipeline begründet hat. Hier wird sie umgestaltet, um `.prop`-Dateien statt installierbarer Module zu speichern und zu verteilen. Die gesamte Anerkennung für die ursprüngliche Arbeit gebührt ihrem Autor.

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

**GNU GPL-3.0-or-later** - siehe [LICENSE](LICENSE). Copyleft: Wer eine veränderte Version verteilt, muss deren Quellcode zu denselben Bedingungen anbieten.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
