[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | **中文** | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*一个可浏览、自动更新的真实 Pixel `.prop` 文件归档，直接来自 Google 的 OTA 镜像*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

一个按版本归档的仓库，收录每台 Pixel 完整的 `build.prop`，直接从 Google 官方 OTA 镜像中提取并自动保持最新。每台设备的 `.prop` 都存储在本仓库中，并作为发布资源发布，无需任何工具即可浏览或下载。

## 📥 Get a `.prop`

两种方式，无需任何设置：

- **浏览仓库**：打开 [`<codename>/`](.) 并选择 `<codename>_<build_id>.prop`。
- **从 Releases 下载**：从最新的[发布](https://github.com/VictorGabriel7Dev/build.prop/releases)（标记为 `build-YYYYMMDD`）中获取文件。

每个 `.prop` 都是该确切设备和构建的完整、有序的构建属性集合（product、vendor、odm、system、system_ext、system_dlkm 等）。

## 🔧 Build it yourself

要在本地提取 `.prop` 而不是下载它，你需要一个类 Unix 环境（带 Bash 的 Linux 或 macOS），外加 `p7zip-full`、`e2fsprogs`、`erofs-utils`、`lz4`、`cpio`、`dos2unix`、`aria2`、`curl`、`xxd`、`jq`，以及 Python ≥3.8 和 `payload_dumper`。`requirements.sh` 可在大多数包管理器上安装这些依赖（apt、pacman、dnf、yum、zypper、apk、xbps、brew、Termux）。

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

支持的设备是 [Google Android Images](https://developers.google.com/android/images) 以及 [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota) 上的工厂镜像和 OTA 镜像。提取过程逐个读取每个 payload 分区（低内存占用），并处理 EROFS、ext4、sparse 以及 boot/init_boot 镜像。

## 🤖 Automation

一条 GitHub Actions 流水线（`.github/workflows/build.yml`）使归档保持最新：

- 每周运行，也可通过 `workflow_dispatch` 按需运行，传入以空格分隔的设备列表或 `all`；每台设备并行构建。
- 提取 `.prop`，将新文件提交到 `<codename>/` 下，并在单个每日标签（`build-YYYYMMDD`）下将它们作为资源发布。
- 跳过已发布的 `.prop` 文件，并通过 Telegram 发送带可点击下载链接的通知。

运行该流水线的 fork 需要两个密钥：`TELEGRAM_BOT_TOKEN`（来自 [@BotFather](https://t.me/BotFather)）和 `TELEGRAM_CHAT_ID`。

## Acknowledgements

本项目是 **[@T3SL4](https://github.com/T3SL4)** 的 **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** 的 fork，后者开创了从 OTA 到 prop 的提取流水线。原始作品的全部功劳归其作者所有。

## 联系方式

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - 参见 [LICENSE](LICENSE)。Copyleft：任何分发修改版本的人都必须在相同条款下提供其源代码。

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
