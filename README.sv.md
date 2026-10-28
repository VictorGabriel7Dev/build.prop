[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | **Svenska** | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Extrahera och distribuera hela Pixels `.prop` direkt från Googles OTA-avbilder*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Extrahera och hantera enkelt systemegenskaper från Pixels OTA-uppdateringar med denna robusta automatiseringssvit. Den extraherar den fullständiga, organiserade `.prop` för varje enhet direkt från Googles officiella OTA-avbilder och **lagrar och distribuerar sedan dessa `.prop`-filer** - både versionshanterade i arkivet och publicerade som release-tillgångar. Inga installerbara moduler: bara egenskaperna.

## 🚀 Snabbstart

### Förutsättningar

- **Unix-liknande miljö**: Linux eller macOS med Bash.
- **Grundläggande verktyg**:
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

1. **Klona arkivet**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Skapa och aktivera en virtuell miljö** (valfritt men rekommenderas):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Installera beroendena**:

    ```bash
    pip3 install payload_dumper
    ```

## Användning

### Lokalt

1. **Hämta de senaste OTA-avbilderna**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Exempel:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Enheter som stöds i önskade fabriks- eller OTA-avbilder från [Google Android Images](https://developers.google.com/android/images) eller [Beta-OTA-sidorna](https://developer.android.com/about/versions/17/download-ota).

2. **Extrahera avbilderna och samla in `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Detta gör automatiskt:
    - Extraherar partitionerna i payload.bin en i taget (låg minnesanvändning)
    - Upptäcker och hanterar **EROFS**-, **ext4**-, **sparse**- och **boot/init_boot**-avbilder
    - Bygger den fullständiga, organiserade `.prop` från varje partitions build.prop
    - Sparar den i `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

Arkivet innehåller en helt automatiserad CI-pipeline (`.github/workflows/build.yml`):

- **Schemalagda byggen**: körs varje söndag vid midnatt UTC.
- **Manuell körning**: utlös via `workflow_dispatch` med en mellanslagsseparerad enhetslista eller `all`.
- **Matrisbyggen**: varje enhet bearbetas parallellt.
- **Dubblettförebyggande**: hoppar över `.prop`-filer som redan finns i befintliga utgåvor.
- **Versionshanterade i arkivet**: nya `.prop`-filer committas under `props/<codename>/`.
- **Samlade utgåvor**: alla nya `.prop`-filer publiceras under en enda daglig tagg (`build-YYYYMMDD`).
- **Telegram-aviseringar**: skickar ett formaterat meddelande med klickbara nedladdningslänkar.

#### Nödvändiga secrets

| Secret | Beskrivning |
|--------|-------------|
| `TELEGRAM_BOT_TOKEN` | Din Telegram-bottoken från [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID för målchatten (användare, grupp eller kanal) |

## ✨ Viktiga funktioner

- **Automatiserad OTA-hämtning**: laddar ner de senaste byggena direkt från Googles officiella källor.
- **Stöd för moderna filsystem**: hanterar EROFS-, ext4-, sparse-avbilder och boot/init_boot-ramdiskar.
- **Fullständig `.prop`-generering**: bygger en enda organiserad `.prop` per enhet från varje partitions build.prop (product, vendor, odm, system, system_ext, system_dlkm med flera).
- **Minnessnål extrahering**: payload-partitioner dumpas en i taget för att undvika OOM på stora OTA:er.
- **Plattformsoberoende pakethantering**: `requirements.sh` stöder apt, pacman, dnf, yum, zypper, apk, xbps, brew och Termux.
- **Lagring och distribution**:
  - **I arkivet**: varje `.prop` committas under `props/<codename>/`, versionshanterad och utforskbar.
  - **Som release-tillgångar**: varje `.prop` publiceras under den dagliga taggen för direkt nedladdning.
- **GitHub Actions-integrering**:
  - **Schemalagda arbetsflöden**: automatiserar uppdateringar, extrahering och utgåvor enligt ett schema.
  - **Förebyggande av dubbletter av utgåvor**: undviker överflödiga utgåvor genom att kontrollera befintliga utgåvors tillgångar.
  - **Idempotenta utgåvor**: laddar upp på nytt till en befintlig daglig utgåvetagg om körningen upprepas.
  - **Telegram-aviseringar**: få aktuella uppdateringar med klickbara nedladdningslänkar.

## 📝 Riktlinjer för ansvarsfull användning

Detta projekt tillhandahålls för utbildnings- och experimentsyften. Även om det är utformat för effektivitet är det avgörande att använda detta verktyg ansvarsfullt.

- **Kodgranskning**: granska och förstå koden noggrant innan du distribuerar den i någon miljö.
- **Bästa säkerhetspraxis**: följ branschstandarder för säkerhet och rättslig efterlevnad.

Skaparna av detta projekt ansvarar inte för eventuellt missbruk eller skador som uppstår till följd av dess användning.

## Tack

Detta projekt är en fork av **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** av **[@T3SL4](https://github.com/T3SL4)**, som var först med extraktionspipelinen från OTA till prop. Här är den omformad för att lagra och distribuera `.prop`-filer i stället för installerbara moduler. All heder för det ursprungliga arbetet går till dess upphovsman.

## Kontakt

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licens

**GNU GPL-3.0-or-later** - se [LICENSE](LICENSE). Copyleft: den som distribuerar en modifierad version måste erbjuda dess källkod på samma villkor.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
