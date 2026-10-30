[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | **中文** | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*一个可浏览、自动更新的真实 Pixel `build.prop` 数据归档，直接来自 Google 的官方镜像*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

一个按版本归档的仓库，收录每台近期 Pixel **每个渠道的最近 4 个版本**（stable、beta 和 canary），直接从 Google 官方工厂镜像和 OTA 镜像中提取。每条记录都是**完整的** `build.prop`，跨**所有分区**（system、system_ext、product、vendor、odm 以及 `_dlkm` 镜像）合并而成，并带有 **`ro.boot.vbmeta.digest`**（verified boot 哈希）。所有内容都存储在仓库中，索引在机器可读的 `index.json` 里，并作为发布资源发布。无需任何工具。

## 📥 Get the data

三种方式，无需任何设置：

- **浏览仓库**：打开 [`<codename>/`](.) 并选择一个文件。按渠道命名：
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`**：一份机器可读的清单，将每台设备 → 渠道 → 最新版本映射起来，包含 `model`、`soc`、`first_api_level`、`security_patch`、`android`、`build`、`incremental` 和 `vbmeta_digest`。非常适合自动化和工具链。
- **Releases**：从最新的[发布](https://github.com/VictorGabriel7Dev/build.prop/releases)（标记为 `build-YYYYMMDD`）下载整个语料库，打包为单个 `.zip`（外加 `index.json`）。

每个 `.prop` 都是该确切设备和构建的完整、有序的属性集合 - 包含所有分区，外加 `ro.boot.vbmeta.digest`。

## 🗂️ What's inside

- **每台近期 Pixel 设备**（Pixel 6 及更新机型）。
- **每台设备三个渠道** - stable、beta 和 canary，各自的最新构建（取决于 Google 实际发布的内容；部分全新设备在 canary 上仍然只有一两个构建）。
- **完整的 `build.prop`**，每个构建约 300-390 个属性，从所有分区合并而来。
- **`vbmeta.digest`**（verified boot 哈希）与属性一同存储。

## 🔧 Build one yourself

要在本地提取单个 `.prop` 而不是下载它，你需要一个类 Unix 环境（带 Bash 的 Linux 或 macOS），外加 `p7zip-full`、`e2fsprogs`、`erofs-utils`、`lz4`、`cpio`、`dos2unix`、`aria2`、`curl`、`xxd`、`jq`，以及 Python ≥3.8 和 `payload_dumper`。`requirements.sh` 可在大多数包管理器上安装这些依赖（apt、pacman、dnf、yum、zypper、apk、xbps、brew、Termux）。

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

支持的设备是 [Google Android Images](https://developers.google.com/android/images) 以及 [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota) 上的工厂镜像和 OTA 镜像。提取过程逐个读取每个 payload 分区（低内存占用），并处理 EROFS、ext4、sparse 以及 boot/init_boot 镜像。

## 🤖 Automation

归档会自动保持最新：当 Google 发布新构建时，它们会被提取（完整、所有分区、带 `vbmeta.digest`），新的 `.prop` 会被提交到 `<codename>/` 下，`index.json` 会被刷新，并切出一个带日期的发布（`build-YYYYMMDD`），以便关注者在每一波更新时都收到通知。

还提供一个通用的、按需触发的 `.github/workflows/build.yml`（`workflow_dispatch`），作为手动构建某台设备最新 `.prop` 的后备方案。

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
