[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | **日本語** | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Pixel の完全な `.prop` を Google の OTA イメージから直接抽出して配布*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

この堅牢な自動化スイートを使えば、Pixel の OTA アップデートからシステムプロパティを手間なく抽出・管理できます。各デバイスの完全で整理された `.prop` を Google の公式 OTA イメージから直接抽出し、**それらの `.prop` ファイルを保存して配布します** - リポジトリでバージョン管理し、リリースアセットとしても公開します。インストール可能なモジュールはありません。プロパティのみです。

## 🚀 クイックスタート

### 前提条件

- **Unix 系の環境**: Bash が使える Linux または macOS。
- **主要なユーティリティ**:
  - `zip`、`unzip`、`p7zip-full`
  - `dos2unix`、`aria2`、`curl`
  - `e2fsprogs`、`erofs-utils`、`lz4`、`cpio`
  - `xxd`、`jq`
- **Python ≥3.8**:

    ```bash
    sudo apt-get update -y
    sudo apt-get install -y python3 python3-pip python3-venv jq xxd \
      p7zip-full e2fsprogs erofs-utils lz4 cpio dos2unix aria2 curl
    ```

## インストール

1. **リポジトリをクローンする**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **仮想環境を作成して有効化する**（任意ですが推奨）:

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **依存関係をインストールする**:

    ```bash
    pip3 install payload_dumper
    ```

## 使い方

### ローカル

1. **最新の OTA イメージを取得する**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    例:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### [Google Android Images](https://developers.google.com/android/images) または [Beta OTA ページ](https://developer.android.com/about/versions/17/download-ota) で、目的の工場出荷時イメージまたは OTA イメージがサポートするデバイス。

2. **イメージを展開して `.prop` を収集する**:

    ```bash
    ./extract_images.sh
    ```

    これにより自動的に:
    - payload.bin のパーティションを 1 つずつ展開します（低メモリ使用）
    - **EROFS**、**ext4**、**sparse**、**boot/init_boot** イメージを検出して処理します
    - 各パーティションの build.prop から完全で整理された `.prop` を構築します
    - それを `props/<codename>/<codename>_<build_id>.prop` に保存します

### GitHub Actions

このリポジトリには、完全に自動化された CI パイプライン（`.github/workflows/build.yml`）が含まれています。

- **スケジュール実行のビルド**: 毎週日曜の UTC 深夜に実行されます。
- **手動実行**: スペース区切りのデバイスリストまたは `all` を指定して `workflow_dispatch` からトリガーします。
- **マトリクスビルド**: 各デバイスを並行して処理します。
- **重複防止**: 既存のリリースにすでに含まれる `.prop` ファイルはスキップします。
- **リポジトリでバージョン管理**: 新しい `.prop` ファイルは `props/<codename>/` 配下にコミットされます。
- **集約リリース**: 新しい `.prop` ファイルはすべて単一の日次タグ（`build-YYYYMMDD`）の下で公開されます。
- **Telegram 通知**: クリック可能なダウンロードリンク付きの整形済みメッセージを送信します。

#### 必要なシークレット

| シークレット | 説明 |
|------------|------|
| `TELEGRAM_BOT_TOKEN` | [@BotFather](https://t.me/BotFather) から取得した Telegram ボットのトークン |
| `TELEGRAM_CHAT_ID` | 送信先チャットの ID（ユーザー、グループ、またはチャンネル） |

## ✨ 主な機能

- **OTA の自動取得**: 最新のビルドを Google の公式ソースから直接ダウンロードします。
- **最新ファイルシステムのサポート**: EROFS、ext4、sparse イメージおよび boot/init_boot の ramdisk を処理します。
- **完全な `.prop` の生成**: 各パーティションの build.prop からデバイスごとに単一の整理された `.prop` を構築します（product、vendor、odm、system、system_ext、system_dlkm など）。
- **メモリ効率の良い抽出**: 大きな OTA で OOM を避けるため、payload のパーティションを 1 つずつダンプします。
- **クロスプラットフォームのパッケージ管理**: `requirements.sh` は apt、pacman、dnf、yum、zypper、apk、xbps、brew、Termux に対応します。
- **保存と配布**:
  - **リポジトリ内**: 各 `.prop` は `props/<codename>/` 配下にコミットされ、バージョン管理され、閲覧できます。
  - **リリースアセットとして**: 各 `.prop` は直接ダウンロード用に日次タグの下で公開されます。
- **GitHub Actions 連携**:
  - **スケジュールされたワークフロー**: 更新、抽出、リリースをスケジュールに沿って自動化します。
  - **重複リリースの防止**: 既存リリースのアセットを確認し、冗長なリリースを回避します。
  - **冪等なリリース**: 再トリガー時には既存の日次リリースタグに再アップロードします。
  - **Telegram 通知**: クリック可能なダウンロードリンク付きのタイムリーな更新を受け取ります。

## 📝 責任ある利用のガイドライン

このプロジェクトは教育および実験目的で提供されています。効率性を重視して設計されていますが、このツールを責任を持って使用することが極めて重要です。

- **コードレビュー**: どのような環境でも導入する前に、コードを十分にレビューし理解してください。
- **セキュリティのベストプラクティス**: セキュリティと法令順守に関する業界標準を遵守してください。

このプロジェクトの作成者は、その使用に起因するいかなる誤用や損害についても責任を負いません。

## 謝辞

このプロジェクトは、OTA から prop への抽出パイプラインを切り開いた **[@T3SL4](https://github.com/T3SL4)** による **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** のフォークです。ここでは、インストール可能なモジュールではなく `.prop` ファイルを保存・配布するよう再構成されています。オリジナルの作品に対するすべての功績はその作者に帰します。

## 連絡先

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## ライセンス

**GNU GPL-3.0-or-later** - [LICENSE](LICENSE) を参照してください。コピーレフト: 変更版を配布する者は、同じ条件でそのソースコードを提供しなければなりません。

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
