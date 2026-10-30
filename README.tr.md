[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | **Türkçe** | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Google'ın resmi imajlarından doğrudan alınan, gerçek Pixel `build.prop` verilerinin göz atılabilir, otomatik güncellenen bir arşivi*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Her yeni Pixel için **her kanalın son 4 derlemesinin** (stable, beta ve canary) sürümlenmiş bir arşivi; doğrudan Google'ın resmi fabrika ve OTA imajlarından çıkarılır. Her girdi, **her bölümden** (system, system_ext, product, vendor, odm ve `_dlkm` imajları) birleştirilmiş **tam** `build.prop` dosyasıdır ve **`ro.boot.vbmeta.digest`** (verified boot hash) değerini taşır. Her şey depoda saklanır, makine tarafından okunabilir bir `index.json` içinde indekslenir ve sürüm varlıkları olarak yayımlanır. Hiçbir araç gerekmez.

## 📥 Verileri edinin

Üç yol, kuruluma gerek yok:

- **Depoya göz atın** - [`<codename>/`](.) dizinini açın ve bir dosya seçin. Kanala göre adlandırma:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - her cihazı → kanalı → en son derlemeyi eşleyen, makine tarafından okunabilir bir manifesto; `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` ve `vbmeta_digest` ile. Otomasyon ve araçlar için idealdir.
- **Releases** - tüm külliyatı tek bir `.zip` olarak (artı `index.json`) en son [sürümden](https://github.com/VictorGabriel7Dev/build.prop/releases) indirin (`build-YYYYMMDD` etiketli).

Her `.prop`, tam olarak o cihaz ve derleme için eksiksiz, düzenlenmiş özellikler kümesidir - tüm bölümler, artı `ro.boot.vbmeta.digest`.

## 🗂️ İçeriği

- **Her yeni Pixel cihazı** (Pixel 6 ve sonrası).
- **Cihaz başına üç kanal** - stable, beta ve canary; her birinin en son derlemeleri (Google'ın gerçekte yayımladıklarına bağlıdır; bazı yepyeni cihazlarda canary'de hâlâ yalnızca bir veya iki derleme bulunur).
- **Tam `build.prop`** her derleme için (~300-390 özellik), tüm bölümlerden birleştirilmiş.
- **`vbmeta.digest`** (verified boot hash) özelliklerin yanında saklanır.

## 🔧 Kendiniz derleyin

Bir `.prop` dosyasını indirmek yerine yerel olarak çıkarmak için, Unix benzeri bir ortama (Bash ile Linux veya macOS) ve ayrıca `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` ve `payload_dumper` ile Python ≥3.8 sürümüne ihtiyacınız vardır. `requirements.sh` bağımlılıkları çoğu paket yöneticisinde kurar (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Desteklenen cihazlar, [Google Android Images](https://developers.google.com/android/images) ve [Beta OTA sayfalarındaki](https://developer.android.com/about/versions/17/download-ota) fabrika ve OTA imajlarıdır. Çıkarma işlemi her payload bölümünü teker teker okur (düşük bellek) ve EROFS, ext4, sparse ve boot/init_boot imajlarını işler.

## 🤖 Otomasyon

Arşiv otomatik olarak güncel kalır: Google yeni derlemeler yayımladıkça bunlar çıkarılır (tam, tüm bölümler, `vbmeta.digest` ile), yeni `.prop` dosyaları `<codename>/` altına commit edilir, `index.json` yenilenir ve tarihli bir sürüm (`build-YYYYMMDD`) oluşturulur; böylece izleyiciler her dalgadan haberdar edilir.

Ayrıca, bir cihazın en son `.prop` dosyasını derlemek için manuel bir yedek olarak genel, istek üzerine çalışan bir `.github/workflows/build.yml` de mevcuttur (`workflow_dispatch`).

## Teşekkürler

Bu proje, OTA'dan prop'a çıkarma ardışık düzenine öncülük eden **[@T3SL4](https://github.com/T3SL4)** tarafından geliştirilen **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** projesinin bir çatalıdır. Orijinal çalışmanın tüm övgüsü yazarına aittir.

## İletişim

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Lisans

**GNU GPL-3.0-or-later** - bkz. [LICENSE](LICENSE). Copyleft: değiştirilmiş bir sürümü dağıtan herkes, kaynağını aynı koşullar altında sunmak zorundadır.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
