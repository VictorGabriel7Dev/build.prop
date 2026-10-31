**English** | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*A browsable, auto-updated archive of real Pixel `build.prop` data, straight from Google's official images*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

A versioned archive of the **last 4 builds of each channel** (stable, beta and canary) for every recent Pixel, extracted directly from Google's official factory and OTA images. Each entry is the **full** `build.prop`, merged across **every partition** (system, system_ext, product, vendor, odm and the `_dlkm` images), and carries the **`ro.boot.vbmeta.digest`** (verified boot hash). Everything is stored in the repository, indexed in a machine-readable `index.json`, and published as release assets. No tooling required.

## 📥 Get the data

Three ways, no setup needed:

- **Browse the repository** - open [`<codename>/`](.) and pick a file. Naming by channel:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - a machine-readable manifest mapping each device → channel → latest build, with `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` and `vbmeta_digest`. Ideal for automation and tooling.
- **Releases** - each `.prop` is attached individually (plus `index.json`) to the latest [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (tagged `build-YYYYMMDD`).

Each `.prop` is the full, organized set of properties for that exact device and build - all partitions, plus `ro.boot.vbmeta.digest`.

## 🗂️ What's inside

- **Every recent Pixel device** (Pixel 6 and newer).
- **Three channels per device** - stable, beta and canary, the latest builds of each (subject to what Google actually publishes; some brand-new devices still have only a build or two on canary).
- **Full `build.prop`** per build (~300-390 properties), merged from all partitions.
- **`vbmeta.digest`** (the verified boot hash) stored alongside the properties.

## 🔧 Build one yourself

To extract a single `.prop` locally instead of downloading it, you need a Unix-like environment (Linux or macOS with Bash) plus `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, and Python ≥3.8 with `payload_dumper`. `requirements.sh` installs the dependencies across most package managers (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Supported devices are the factory and OTA images on [Google Android Images](https://developers.google.com/android/images) and the [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Extraction reads each payload partition one at a time (low memory) and handles EROFS, ext4, sparse and boot/init_boot images.

## 🤖 Automation

The archive stays current automatically: as Google publishes new builds, they are extracted (full, all partitions, with `vbmeta.digest`), the new `.prop` are committed under `<codename>/`, `index.json` is refreshed, and a dated release (`build-YYYYMMDD`) is cut so watchers are notified of every wave.

A generic, on-demand `.github/workflows/build.yml` is also available (`workflow_dispatch`) as a manual fallback to build a device's latest `.prop`.

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
