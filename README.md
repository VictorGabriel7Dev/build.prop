**English** | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*A browsable, auto-updated archive of real Pixel `.prop` files, straight from Google's OTA images*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

A versioned archive of each Pixel's full `build.prop`, extracted directly from Google's official OTA images and kept up to date automatically. Every device's `.prop` is stored in the repository and published as a release asset, ready to browse or download with no tooling required.

## 📥 Get a `.prop`

Two ways, no setup needed:

- **Browse the repository**: open [`props/<codename>/`](props/) and pick `<codename>_<build_id>.prop`.
- **Download from Releases**: grab the file from the latest [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (tagged `build-YYYYMMDD`).

Each `.prop` is the full, organized set of build properties for that exact device and build (product, vendor, odm, system, system_ext, system_dlkm and more).

## 🔧 Build it yourself

To extract a `.prop` locally instead of downloading it, you need a Unix-like environment (Linux or macOS with Bash) plus `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, and Python ≥3.8 with `payload_dumper`. `requirements.sh` installs the dependencies across most package managers (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
pip3 install payload_dumper
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Supported devices are the factory and OTA images on [Google Android Images](https://developers.google.com/android/images) and the [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Extraction reads each payload partition one at a time (low memory) and handles EROFS, ext4, sparse and boot/init_boot images.

## 🤖 Automation

A GitHub Actions pipeline (`.github/workflows/build.yml`) keeps the archive current:

- Runs weekly, and on demand via `workflow_dispatch` with a space-separated device list or `all`; each device builds in parallel.
- Extracts the `.prop`, commits new ones under `props/<codename>/`, and publishes them as assets under a single daily tag (`build-YYYYMMDD`).
- Skips `.prop` files already released and notifies Telegram with clickable download links.

Forks that run the pipeline need two secrets: `TELEGRAM_BOT_TOKEN` (from [@BotFather](https://t.me/BotFather)) and `TELEGRAM_CHAT_ID`.

## Acknowledgements

This project is a fork of **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** by **[@T3SL4](https://github.com/T3SL4)**, which pioneered the OTA-to-prop extraction pipeline. Full credit for the original work goes to its author.

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

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
