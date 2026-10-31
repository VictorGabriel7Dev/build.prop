[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | **日本語** | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Google の公式イメージから直接取得した、本物の Pixel `build.prop` データを閲覧でき、自動更新されるアーカイブ*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

最近の各 Pixel について **各チャンネルの直近 4 ビルド**（stable、beta、canary）をバージョン管理してアーカイブしたリポジトリで、Google 公式のファクトリーイメージと OTA イメージから直接抽出しています。各エントリは**完全な** `build.prop` であり、**すべてのパーティション**（system、system_ext、product、vendor、odm、および `_dlkm` イメージ）を横断してマージされ、**`ro.boot.vbmeta.digest`**（verified boot ハッシュ）を含みます。すべてがリポジトリに保存され、機械可読の `index.json` にインデックスされ、リリースアセットとして公開されます。ツールは不要です。

## 📥 Get the data

セットアップ不要の 3 つの方法：

- **リポジトリを閲覧する**：[`<codename>/`](.) を開いてファイルを選びます。チャンネルごとの命名：
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`**：各デバイス → チャンネル → 最新ビルドを対応づける機械可読のマニフェストで、`model`、`soc`、`first_api_level`、`security_patch`、`android`、`build`、`incremental`、`vbmeta_digest` を含みます。自動化やツール連携に最適です。
- **Releases**：各 `.prop` は最新の[リリース](https://github.com/VictorGabriel7Dev/build.prop/releases)（`build-YYYYMMDD` でタグ付け）に個別に添付されます（`index.json` も添付）。

各 `.prop` は、その正確なデバイスとビルドに対応するプロパティの完全で整理された一式です - すべてのパーティションに加え、`ro.boot.vbmeta.digest` も含みます。

## 🗂️ What's inside

- **最近の各 Pixel デバイス**（Pixel 6 以降）。
- **デバイスごとに 3 チャンネル** - stable、beta、canary、それぞれの最新ビルド（Google が実際に公開している内容に依存します。発売直後のデバイスでは canary にまだ 1～2 ビルドしかない場合もあります）。
- **完全な `build.prop`**、ビルドごとに約 300-390 個のプロパティで、すべてのパーティションからマージされています。
- **`vbmeta.digest`**（verified boot ハッシュ）がプロパティと並んで保存されます。

## 🔧 Build one yourself

ダウンロードする代わりにローカルで単一の `.prop` を抽出するには、Unix 系環境（Bash を備えた Linux または macOS）に加えて、`p7zip-full`、`e2fsprogs`、`erofs-utils`、`lz4`、`cpio`、`dos2unix`、`aria2`、`curl`、`xxd`、`jq`、そして `payload_dumper` を含む Python ≥3.8 が必要です。`requirements.sh` はほとんどのパッケージマネージャー（apt、pacman、dnf、yum、zypper、apk、xbps、brew、Termux）で依存関係をインストールします。

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

対応デバイスは、[Google Android Images](https://developers.google.com/android/images) および [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota) にあるファクトリーイメージと OTA イメージです。抽出処理は各 payload パーティションを一度に 1 つずつ読み込み（低メモリ）、EROFS、ext4、sparse、boot/init_boot イメージを扱います。

## 🤖 Automation

アーカイブは自動的に最新に保たれます：Google が新しいビルドを公開すると、それらが抽出され（完全、全パーティション、`vbmeta.digest` 付き）、新しい `.prop` が `<codename>/` の下にコミットされ、`index.json` が更新され、日付入りのリリース（`build-YYYYMMDD`）が作成されるため、ウォッチャーは更新のたびに通知を受け取ります。

汎用でオンデマンドの `.github/workflows/build.yml`（`workflow_dispatch`）も、デバイスの最新 `.prop` を手動でビルドするためのフォールバックとして利用できます。

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
