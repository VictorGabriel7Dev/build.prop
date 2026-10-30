[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | **Bahasa Indonesia** | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Arsip data `build.prop` Pixel asli yang dapat dijelajahi dan diperbarui otomatis, langsung dari image resmi Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Arsip berversi dari **4 build terakhir setiap channel** (stable, beta dan canary) untuk setiap Pixel terbaru, diekstrak langsung dari image factory dan OTA resmi Google. Setiap entri adalah `build.prop` **lengkap**, digabungkan dari **setiap partisi** (system, system_ext, product, vendor, odm dan image `_dlkm`), serta memuat **`ro.boot.vbmeta.digest`** (verified boot hash). Semuanya disimpan di repositori, diindeks dalam `index.json` yang dapat dibaca mesin, dan dipublikasikan sebagai aset rilis. Tanpa perlu alat apa pun.

## 📥 Dapatkan data

Tiga cara, tanpa pengaturan:

- **Jelajahi repositori** - buka [`<codename>/`](.) dan pilih sebuah file. Penamaan menurut channel:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - manifes yang dapat dibaca mesin yang memetakan setiap perangkat → channel → build terbaru, dengan `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` dan `vbmeta_digest`. Ideal untuk otomatisasi dan perkakas.
- **Releases** - unduh seluruh korpus sebagai satu `.zip` (plus `index.json`) dari [rilis](https://github.com/VictorGabriel7Dev/build.prop/releases) terbaru (dengan tag `build-YYYYMMDD`).

Setiap `.prop` adalah kumpulan properti yang lengkap dan terorganisir untuk perangkat dan build persis tersebut - semua partisi, plus `ro.boot.vbmeta.digest`.

## 🗂️ Apa isinya

- **Setiap perangkat Pixel terbaru** (Pixel 6 dan yang lebih baru).
- **Tiga channel per perangkat** - stable, beta dan canary, build terbaru dari masing-masing (bergantung pada apa yang benar-benar dipublikasikan Google; beberapa perangkat yang sangat baru masih hanya memiliki satu atau dua build di canary).
- **`build.prop` lengkap** per build (~300-390 properti), digabungkan dari semua partisi.
- **`vbmeta.digest`** (verified boot hash) disimpan bersama properti.

## 🔧 Bangun sendiri

Untuk mengekstrak satu `.prop` secara lokal alih-alih mengunduhnya, Anda memerlukan lingkungan mirip Unix (Linux atau macOS dengan Bash) ditambah `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, dan Python ≥3.8 dengan `payload_dumper`. `requirements.sh` memasang dependensi di sebagian besar manajer paket (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Perangkat yang didukung adalah image factory dan OTA di [Google Android Images](https://developers.google.com/android/images) dan [halaman Beta OTA](https://developer.android.com/about/versions/17/download-ota). Ekstraksi membaca setiap partisi payload satu per satu (memori rendah) dan menangani image EROFS, ext4, sparse dan boot/init_boot.

## 🤖 Otomatisasi

Arsip tetap mutakhir secara otomatis: saat Google mempublikasikan build baru, build tersebut diekstrak (lengkap, semua partisi, dengan `vbmeta.digest`), `.prop` baru di-commit di bawah `<codename>/`, `index.json` diperbarui, dan sebuah rilis bertanggal (`build-YYYYMMDD`) dibuat sehingga para pemantau diberi tahu tentang setiap gelombang.

Sebuah `.github/workflows/build.yml` generik dan sesuai permintaan juga tersedia (`workflow_dispatch`) sebagai cadangan manual untuk membangun `.prop` terbaru sebuah perangkat.

## Ucapan Terima Kasih

Proyek ini adalah fork dari **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** oleh **[@T3SL4](https://github.com/T3SL4)**, yang memelopori pipeline ekstraksi OTA-ke-prop. Seluruh penghargaan atas karya aslinya diberikan kepada penulisnya.

## Kontak

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Lisensi

**GNU GPL-3.0-or-later** - lihat [LICENSE](LICENSE). Copyleft: siapa pun yang mendistribusikan versi yang dimodifikasi harus menawarkan sumbernya dengan ketentuan yang sama.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
