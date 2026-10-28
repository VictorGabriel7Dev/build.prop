[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | **中文** | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*直接从 Google 的 OTA 镜像提取并分发完整的 Pixel `.prop`*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

使用这套强大的自动化工具，轻松从 Pixel OTA 更新中提取并管理系统属性。它直接从 Google 官方 OTA 镜像为每台设备提取完整、组织良好的 `.prop`，然后**存储并分发这些 `.prop` 文件** - 既在仓库中进行版本管理，也作为发行版资产发布。没有可安装的模块：只有属性。

## 🚀 快速开始

### 先决条件

- **类 Unix 环境**：带 Bash 的 Linux 或 macOS。
- **核心工具**：
  - `zip`、`unzip`、`p7zip-full`
  - `dos2unix`、`aria2`、`curl`
  - `e2fsprogs`、`erofs-utils`、`lz4`、`cpio`
  - `xxd`、`jq`
- **Python ≥3.8**：

    ```bash
    sudo apt-get update -y
    sudo apt-get install -y python3 python3-pip python3-venv jq xxd \
      p7zip-full e2fsprogs erofs-utils lz4 cpio dos2unix aria2 curl
    ```

## 安装

1. **克隆仓库**：

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **创建并激活虚拟环境**（可选但推荐）：

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **安装依赖**：

    ```bash
    pip3 install payload_dumper
    ```

## 用法

### 本地

1. **获取最新的 OTA 镜像**：

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    示例：
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### 在 [Google Android Images](https://developers.google.com/android/images) 或 [Beta OTA 页面](https://developer.android.com/about/versions/17/download-ota) 上所需出厂镜像或 OTA 镜像中受支持的设备。

2. **提取镜像并收集 `.prop`**：

    ```bash
    ./extract_images.sh
    ```

    这会自动：
    - 逐个提取 payload.bin 的分区（低内存占用）
    - 检测并处理 **EROFS**、**ext4**、**sparse** 和 **boot/init_boot** 镜像
    - 从每个分区的 build.prop 构建完整、组织良好的 `.prop`
    - 将其保存到 `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

该仓库包含一个完全自动化的 CI 流水线（`.github/workflows/build.yml`）：

- **定时构建**：每周日 UTC 午夜运行。
- **手动触发**：通过 `workflow_dispatch` 使用以空格分隔的设备列表或 `all` 触发。
- **矩阵构建**：每台设备并行处理。
- **防重复**：跳过已存在于现有发行版中的 `.prop` 文件。
- **仓库中版本管理**：新的 `.prop` 文件提交到 `props/<codename>/`。
- **聚合发行版**：所有新的 `.prop` 文件都在单个每日标签（`build-YYYYMMDD`）下发布。
- **Telegram 通知**：发送带有可点击下载链接的格式化消息。

#### 所需 Secret

| Secret | 说明 |
|--------|------|
| `TELEGRAM_BOT_TOKEN` | 来自 [@BotFather](https://t.me/BotFather) 的 Telegram 机器人令牌 |
| `TELEGRAM_CHAT_ID` | 目标聊天 ID（用户、群组或频道） |

## ✨ 主要特性

- **自动获取 OTA**：直接从 Google 官方来源下载最新构建。
- **现代文件系统支持**：处理 EROFS、ext4、sparse 镜像以及 boot/init_boot ramdisk。
- **完整 `.prop` 生成**：从每个分区的 build.prop 为每台设备构建单个组织良好的 `.prop`（product、vendor、odm、system、system_ext、system_dlkm 等）。
- **内存高效提取**：payload 分区逐个转储，以避免在大型 OTA 上发生 OOM。
- **跨平台包管理**：`requirements.sh` 支持 apt、pacman、dnf、yum、zypper、apk、xbps、brew 和 Termux。
- **存储与分发**：
  - **在仓库中**：每个 `.prop` 提交到 `props/<codename>/`，进行版本管理且可浏览。
  - **作为发行版资产**：每个 `.prop` 在每日标签下发布以供直接下载。
- **GitHub Actions 集成**：
  - **定时工作流**：按计划自动执行更新、提取和发布。
  - **防止重复发行版**：通过检查现有发行版的资产来避免冗余发行。
  - **幂等发行版**：若再次触发，会重新上传到现有的每日发行标签。
  - **Telegram 通知**：及时接收带有可点击下载链接的更新。

## 📝 负责任使用准则

本项目仅用于教育和实验目的。尽管它以高效为设计目标，但负责任地使用本工具至关重要。

- **代码审查**：在任何环境中部署之前，请彻底审查并理解代码。
- **安全最佳实践**：遵守行业安全标准和法律合规要求。

对于因使用本项目而导致的任何误用或损害，本项目的创建者概不负责。

## 致谢

本项目是 **[@T3SL4](https://github.com/T3SL4)** 的 **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** 的一个分支，后者开创了从 OTA 到 prop 的提取流水线。此处将其重塑为存储和分发 `.prop` 文件而非可安装模块。原始作品的全部功劳归于其作者。

## 联系方式

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## 许可证

**GNU GPL-3.0-or-later** - 参见 [LICENSE](LICENSE)。Copyleft：任何分发修改版本的人都必须以相同条款提供其源代码。

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
