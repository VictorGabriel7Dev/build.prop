**English** | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Extract and distribute the full Pixel `.prop` straight from Google's OTA images*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Effortlessly extract and manage system properties from Pixel OTA updates with this robust automation suite. It extracts the full, organized `.prop` for each device straight from Google's official OTA images, then **stores and distributes those `.prop` files** - both versioned in the repository and published as release assets. No installable modules: just the properties.

## 🚀 Quick Start

### Prerequisites

- **Unix-like environment**: Linux or macOS with Bash.
- **Core utilities**:
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

1. **Clone the repository**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip3 install payload_dumper
    ```

## Usage

### Local

1. **Fetch the latest OTA images**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Examples:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Supported devices at the desired factory or OTA images from [Google Android Images](https://developers.google.com/android/images) or the [Beta OTA Pages](https://developer.android.com/about/versions/17/download-ota).

2. **Extract images and collect the `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    This automatically:
    - Extracts payload.bin partitions one-at-a-time (low memory footprint)
    - Detects and handles **EROFS**, **ext4**, **sparse**, and **boot/init_boot** images
    - Builds the full, organized `.prop` from every partition's build.prop
    - Saves it to `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

The repository includes a fully automated CI pipeline (`.github/workflows/build.yml`):

- **Scheduled builds**: Runs every Sunday at midnight UTC.
- **Manual dispatch**: Trigger via `workflow_dispatch` with a space-separated device list or `all`.
- **Matrix builds**: Each device builds in parallel.
- **Duplicate prevention**: Skips `.prop` files already present in existing releases.
- **Versioned in the repo**: New `.prop` files are committed under `props/<codename>/`.
- **Aggregated releases**: All new `.prop` files are published under a single daily tag (`build-YYYYMMDD`).
- **Telegram notifications**: Sends a formatted message with clickable download links.

#### Required Secrets

| Secret | Description |
|--------|-------------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token from [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | Target chat ID (user, group, or channel) |

## ✨ Key Features

- **Automated OTA Acquisition**: Downloads the latest builds directly from Google's official sources.
- **Modern Filesystem Support**: Handles EROFS, ext4, sparse images, and boot/init_boot ramdisks.
- **Full `.prop` Generation**: Builds a single, organized `.prop` per device from every partition's build.prop (product, vendor, odm, system, system_ext, system_dlkm and more).
- **Memory-Efficient Extraction**: Payload partitions are dumped one-at-a-time to avoid OOM on large OTAs.
- **Cross-Platform Package Management**: `requirements.sh` supports apt, pacman, dnf, yum, zypper, apk, xbps, brew, and Termux.
- **Storage and Distribution**:
  - **In the repository**: each `.prop` is committed under `props/<codename>/`, versioned and browsable.
  - **As release assets**: each `.prop` is published under the daily release tag for direct download.
- **GitHub Actions Integration**:
  - **Scheduled Workflows**: Automate updates, extraction, and releases on a schedule.
  - **Duplicate Release Prevention**: Prevents redundant releases by checking existing release assets.
  - **Idempotent Releases**: Re-uploads to an existing daily release tag if re-triggered.
  - **Telegram Notifications**: Receive timely updates with clickable download links.

## 📝 Responsible Usage Guidelines

This project is provided for educational and experimental purposes. While designed for efficiency, it's crucial to use this tool responsibly.

- **Code Review**: Thoroughly review and understand the code before deploying it in any environment.
- **Security Best Practices**: Adhere to industry standards for security and legal compliance.

The creators of this project are not liable for any misuse or damages resulting from its use.

## Acknowledgements

This project is a fork of **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** by **[@T3SL4](https://github.com/T3SL4)**, which pioneered the OTA-to-prop extraction pipeline. It is reshaped here to store and distribute `.prop` files instead of installable modules. Full credit for the original work goes to its author.

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

**GNU GPL-3.0-or-later** - see [LICENSE](LICENSE). Copyleft: anyone who distributes a modified version must offer its source under the same terms.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
