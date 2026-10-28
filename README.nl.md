[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | **Nederlands** | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Haal de volledige Pixel-`.prop` op en verspreid die rechtstreeks uit Googles OTA-images*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Haal moeiteloos systeemeigenschappen uit Pixel-OTA-updates en beheer ze met deze robuuste automatiseringssuite. Ze haalt de volledige, georganiseerde `.prop` van elk apparaat rechtstreeks uit Googles officiële OTA-images en **slaat die `.prop`-bestanden vervolgens op en verspreidt ze** - zowel geversioneerd in de repository als gepubliceerd als release-assets. Geen installeerbare modules: alleen de eigenschappen.

## 🚀 Snelstart

### Vereisten

- **Unix-achtige omgeving**: Linux of macOS met Bash.
- **Essentiële hulpprogramma's**:
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

## Installatie

1. **Kloon de repository**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Maak en activeer een virtuele omgeving** (optioneel maar aanbevolen):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Installeer de afhankelijkheden**:

    ```bash
    pip3 install payload_dumper
    ```

## Gebruik

### Lokaal

1. **Haal de nieuwste OTA-images op**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Voorbeelden:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Ondersteunde apparaten in de gewenste fabrieks- of OTA-images van [Google Android Images](https://developers.google.com/android/images) of de [Beta-OTA-pagina's](https://developer.android.com/about/versions/17/download-ota).

2. **Pak de images uit en verzamel de `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Dit doet automatisch:
    - Pakt de partities van payload.bin één voor één uit (laag geheugengebruik)
    - Detecteert en verwerkt **EROFS**-, **ext4**-, **sparse**- en **boot/init_boot**-images
    - Bouwt de volledige, georganiseerde `.prop` uit de build.prop van elke partitie
    - Slaat die op in `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

De repository bevat een volledig geautomatiseerde CI-pijplijn (`.github/workflows/build.yml`):

- **Geplande builds**: draaien elke zondag om middernacht UTC.
- **Handmatige start**: activeer via `workflow_dispatch` met een door spaties gescheiden apparaatlijst of `all`.
- **Matrixbuilds**: elk apparaat wordt parallel verwerkt.
- **Duplicaatpreventie**: slaat `.prop`-bestanden over die al in bestaande releases aanwezig zijn.
- **Geversioneerd in de repository**: nieuwe `.prop`-bestanden worden vastgelegd onder `props/<codename>/`.
- **Samengevoegde releases**: alle nieuwe `.prop`-bestanden worden onder één dagelijkse tag (`build-YYYYMMDD`) gepubliceerd.
- **Telegram-meldingen**: stuurt een opgemaakt bericht met klikbare downloadlinks.

#### Vereiste secrets

| Secret | Beschrijving |
|--------|--------------|
| `TELEGRAM_BOT_TOKEN` | Je Telegram-bottoken van [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID van de doelchat (gebruiker, groep of kanaal) |

## ✨ Belangrijkste functies

- **Geautomatiseerde OTA-acquisitie**: downloadt de nieuwste builds rechtstreeks uit de officiële bronnen van Google.
- **Ondersteuning voor moderne bestandssystemen**: verwerkt EROFS-, ext4-, sparse-images en boot/init_boot-ramdisks.
- **Volledige `.prop`-generatie**: bouwt één georganiseerde `.prop` per apparaat uit de build.prop van elke partitie (product, vendor, odm, system, system_ext, system_dlkm en meer).
- **Geheugenefficiënte extractie**: payloadpartities worden één voor één gedumpt om OOM bij grote OTA's te voorkomen.
- **Platformonafhankelijk pakketbeheer**: `requirements.sh` ondersteunt apt, pacman, dnf, yum, zypper, apk, xbps, brew en Termux.
- **Opslag en distributie**:
  - **In de repository**: elke `.prop` wordt vastgelegd onder `props/<codename>/`, geversioneerd en doorzoekbaar.
  - **Als release-assets**: elke `.prop` wordt onder de dagelijkse tag gepubliceerd voor directe download.
- **GitHub Actions-integratie**:
  - **Geplande workflows**: automatiseren updates, extractie en releases volgens een schema.
  - **Preventie van dubbele releases**: voorkomt overbodige releases door bestaande release-assets te controleren.
  - **Idempotente releases**: uploadt opnieuw naar een bestaande dagelijkse release-tag bij een nieuwe trigger.
  - **Telegram-meldingen**: ontvang tijdige updates met klikbare downloadlinks.

## 📝 Richtlijnen voor verantwoord gebruik

Dit project wordt aangeboden voor educatieve en experimentele doeleinden. Hoewel het is ontworpen voor efficiëntie, is het cruciaal om dit hulpmiddel verantwoord te gebruiken.

- **Codebeoordeling**: beoordeel en begrijp de code grondig voordat je deze in een omgeving inzet.
- **Beste beveiligingspraktijken**: houd je aan de industriestandaarden voor beveiliging en wettelijke naleving.

De makers van dit project zijn niet aansprakelijk voor enig misbruik of schade als gevolg van het gebruik ervan.

## Dankbetuigingen

Dit project is een fork van **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** van **[@T3SL4](https://github.com/T3SL4)**, die de OTA-naar-prop-extractiepijplijn heeft bedacht. Het is hier omgevormd om `.prop`-bestanden op te slaan en te verspreiden in plaats van installeerbare modules. Alle eer voor het oorspronkelijke werk gaat naar de auteur ervan.

## Contact

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licentie

**GNU GPL-3.0-or-later** - zie [LICENSE](LICENSE). Copyleft: iedereen die een gewijzigde versie verspreidt, moet de broncode onder dezelfde voorwaarden aanbieden.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
