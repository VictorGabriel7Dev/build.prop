[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | **日本語** | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Google の OTA イメージから直接取得した、本物の Pixel `.prop` ファイルを閲覧でき、自動更新されるアーカイブ*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

各 Pixel の完全な `build.prop` をバージョン管理してアーカイブしたリポジトリです。Google 公式の OTA イメージから直接抽出し、自動的に最新の状態に保たれます。各デバイスの `.prop` はリポジトリに保存され、リリースアセットとして公開されるため、ツールなしで閲覧やダウンロードができます。

## 📥 Get a `.prop`

設定不要の 2 つの方法：

- **リポジトリを閲覧する**：[`<codename>/`](.) を開いて `<codename>_<build_id>.prop` を選びます。
- **Releases からダウンロードする**：最新の[リリース](https://github.com/VictorGabriel7Dev/build.prop/releases)（`build-YYYYMMDD` でタグ付け）からファイルを取得します。

各 `.prop` は、その正確なデバイスとビルドに対応するビルドプロパティの完全で整理された一式です（product、vendor、odm、system、system_ext、system_dlkm など）。

## 🔧 Build it yourself

ダウンロードする代わりにローカルで `.prop` を抽出するには、Unix 系環境（Bash を備えた Linux または macOS）に加えて、`p7zip-full`、`e2fsprogs`、`erofs-utils`、`lz4`、`cpio`、`dos2unix`、`aria2`、`curl`、`xxd`、`jq`、そして `payload_dumper` を含む Python ≥3.8 が必要です。`requirements.sh` はほとんどのパッケージマネージャー（apt、pacman、dnf、yum、zypper、apk、xbps、brew、Termux）で依存関係をインストールします。

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

対応デバイスは、[Google Android Images](https://developers.google.com/android/images) および [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota) にあるファクトリーイメージと OTA イメージです。抽出処理は各 payload パーティションを一度に 1 つずつ読み込み（低メモリ）、EROFS、ext4、sparse、boot/init_boot イメージを扱います。

## 🤖 Automation

GitHub Actions のパイプライン（`.github/workflows/build.yml`）がアーカイブを最新に保ちます：

- 毎週実行され、スペース区切りのデバイスリストまたは `all` を指定して `workflow_dispatch` でオンデマンドにも実行できます。各デバイスは並列でビルドされます。
- `.prop` を抽出し、新しいものを `<codename>/` の下にコミットし、単一の日次タグ（`build-YYYYMMDD`）の下でアセットとして公開します。
- すでにリリース済みの `.prop` ファイルはスキップし、クリック可能なダウンロードリンクとともに Telegram へ通知します。

パイプラインを実行する fork には 2 つのシークレットが必要です：`TELEGRAM_BOT_TOKEN`（[@BotFather](https://t.me/BotFather) から取得）と `TELEGRAM_CHAT_ID`。

## Acknowledgements

このプロジェクトは、**[@T3SL4](https://github.com/T3SL4)** による **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** の fork であり、OTA から prop への抽出パイプラインを切り開いたものです。オリジナルの作品に対するすべての功績はその作者に帰します。

## 連絡先

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - [LICENSE](LICENSE) を参照してください。コピーレフト：修正版を配布する者は誰でも、同じ条件の下でそのソースを提供しなければなりません。

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
