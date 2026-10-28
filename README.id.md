[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | **Bahasa Indonesia** | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Arsip file `.prop` Pixel asli yang dapat dijelajahi dan diperbarui otomatis, langsung dari image OTA Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Arsip berversi dari `build.prop` lengkap setiap Pixel, diekstrak langsung dari image OTA resmi Google dan dijaga tetap mutakhir secara otomatis. File `.prop` setiap perangkat disimpan di repositori dan dipublikasikan sebagai aset rilis, siap dijelajahi atau diunduh tanpa perlu alat apa pun.

## 📥 Dapatkan `.prop`

Dua cara, tanpa pengaturan:

- **Jelajahi repositori**: buka [`props/<codename>/`](props/) dan pilih `<codename>_<build_id>.prop`.
- **Unduh dari Releases**: ambil file dari [rilis](https://github.com/VictorGabriel7Dev/build.prop/releases) terbaru (dengan tag `build-YYYYMMDD`).

Setiap `.prop` adalah kumpulan properti build yang lengkap dan terorganisir untuk perangkat dan build persis tersebut (product, vendor, odm, system, system_ext, system_dlkm dan lainnya).

## 🔧 Bangun sendiri

Untuk mengekstrak `.prop` secara lokal alih-alih mengunduhnya, Anda memerlukan lingkungan mirip Unix (Linux atau macOS dengan Bash) ditambah `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, dan Python ≥3.8 dengan `payload_dumper`. `requirements.sh` memasang dependensi di sebagian besar manajer paket (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Perangkat yang didukung adalah image factory dan OTA di [Google Android Images](https://developers.google.com/android/images) dan [halaman Beta OTA](https://developer.android.com/about/versions/17/download-ota). Ekstraksi membaca setiap partisi payload satu per satu (memori rendah) dan menangani image EROFS, ext4, sparse dan boot/init_boot.

## 🤖 Otomatisasi

Pipeline GitHub Actions (`.github/workflows/build.yml`) menjaga arsip tetap mutakhir:

- Berjalan mingguan, dan sesuai permintaan melalui `workflow_dispatch` dengan daftar perangkat yang dipisahkan spasi atau `all`; setiap perangkat dibangun secara paralel.
- Mengekstrak `.prop`, meng-commit yang baru di bawah `props/<codename>/`, dan mempublikasikannya sebagai aset di bawah satu tag harian (`build-YYYYMMDD`).
- Melewati file `.prop` yang sudah dirilis dan memberi tahu Telegram dengan tautan unduhan yang dapat diklik.

Fork yang menjalankan pipeline memerlukan dua secret: `TELEGRAM_BOT_TOKEN` (dari [@BotFather](https://t.me/BotFather)) dan `TELEGRAM_CHAT_ID`.

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

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
