[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | **Bahasa Indonesia** | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Ekstrak dan distribusikan `.prop` lengkap Pixel langsung dari image OTA Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Ekstrak dan kelola properti sistem dari pembaruan OTA Pixel dengan mudah menggunakan rangkaian otomatisasi yang tangguh ini. Ia mengekstrak `.prop` lengkap dan terorganisir untuk setiap perangkat langsung dari image OTA resmi Google, lalu **menyimpan dan mendistribusikan berkas `.prop` tersebut** - baik diversikan di repositori maupun diterbitkan sebagai aset rilis. Tanpa modul yang dapat dipasang: hanya propertinya.

## 🚀 Mulai Cepat

### Prasyarat

- **Lingkungan mirip Unix**: Linux atau macOS dengan Bash.
- **Utilitas inti**:
  - `zip`, `unzip`, `p7zip-full`
  - `dos2unix`, `aria2`, `curl`
  - `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`
  - `xxd`, `jq`
- **Python ≥3.8**:

    ```bash
    sudo apt-get update -y
    sudo apt-get install -y python3 python3-pip python3-venv jq xxd \
      p7zip-full e2fsprogs erofs-utils lz4 cpio dos2unix aria2 curl
    ```

## Instalasi

1. **Klona repositori**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Buat dan aktifkan lingkungan virtual** (opsional tetapi disarankan):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Pasang dependensi**:

    ```bash
    pip3 install payload_dumper
    ```

## Penggunaan

### Lokal

1. **Ambil image OTA terbaru**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Contoh:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Perangkat yang didukung pada image factory atau OTA yang diinginkan dari [Google Android Images](https://developers.google.com/android/images) atau [halaman OTA Beta](https://developer.android.com/about/versions/17/download-ota).

2. **Ekstrak image dan kumpulkan `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Ini secara otomatis:
    - Mengekstrak partisi payload.bin satu per satu (penggunaan memori rendah)
    - Mendeteksi dan menangani image **EROFS**, **ext4**, **sparse**, dan **boot/init_boot**
    - Membangun `.prop` lengkap dan terorganisir dari build.prop setiap partisi
    - Menyimpannya ke `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

Repositori ini menyertakan pipeline CI yang sepenuhnya otomatis (`.github/workflows/build.yml`):

- **Build terjadwal**: berjalan setiap Minggu tengah malam UTC.
- **Pemicu manual**: picu melalui `workflow_dispatch` dengan daftar perangkat yang dipisahkan spasi atau `all`.
- **Build matriks**: setiap perangkat diproses secara paralel.
- **Pencegahan duplikat**: melewati `.prop` yang sudah ada di rilis yang ada.
- **Diversikan di repositori**: `.prop` baru di-commit ke `props/<codename>/`.
- **Rilis teragregasi**: semua `.prop` baru diterbitkan di bawah satu tag harian (`build-YYYYMMDD`).
- **Notifikasi Telegram**: mengirim pesan terformat dengan tautan unduhan yang dapat diklik.

#### Secret yang diperlukan

| Secret | Deskripsi |
|--------|-----------|
| `TELEGRAM_BOT_TOKEN` | Token bot Telegram Anda dari [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID obrolan tujuan (pengguna, grup, atau kanal) |

## ✨ Fitur Utama

- **Akuisisi OTA otomatis**: mengunduh build terbaru langsung dari sumber resmi Google.
- **Dukungan sistem berkas modern**: menangani image EROFS, ext4, sparse, dan ramdisk boot/init_boot.
- **Pembuatan `.prop` lengkap**: membangun satu `.prop` terorganisir per perangkat dari build.prop setiap partisi (product, vendor, odm, system, system_ext, system_dlkm, dan lainnya).
- **Ekstraksi hemat memori**: partisi payload didump satu per satu untuk menghindari OOM pada OTA besar.
- **Manajemen paket lintas platform**: `requirements.sh` mendukung apt, pacman, dnf, yum, zypper, apk, xbps, brew, dan Termux.
- **Penyimpanan dan distribusi**:
  - **Di repositori**: setiap `.prop` di-commit ke `props/<codename>/`, diversikan dan dapat ditelusuri.
  - **Sebagai aset rilis**: setiap `.prop` diterbitkan di bawah tag harian untuk unduhan langsung.
- **Integrasi GitHub Actions**:
  - **Alur kerja terjadwal**: mengotomatiskan pembaruan, ekstraksi, dan rilis sesuai jadwal.
  - **Pencegahan rilis duplikat**: menghindari rilis berlebih dengan memeriksa aset rilis yang ada.
  - **Rilis idempoten**: mengunggah ulang ke tag rilis harian yang ada jika dipicu ulang.
  - **Notifikasi Telegram**: terima pembaruan tepat waktu dengan tautan unduhan yang dapat diklik.

## 📝 Pedoman Penggunaan yang Bertanggung Jawab

Proyek ini disediakan untuk tujuan edukasi dan eksperimen. Meskipun dirancang untuk efisiensi, sangat penting untuk menggunakan alat ini secara bertanggung jawab.

- **Tinjauan kode**: tinjau dan pahami kode secara menyeluruh sebelum menerapkannya di lingkungan apa pun.
- **Praktik keamanan terbaik**: patuhi standar industri untuk keamanan dan kepatuhan hukum.

Pembuat proyek ini tidak bertanggung jawab atas penyalahgunaan atau kerugian apa pun yang timbul dari penggunaannya.

## Ucapan Terima Kasih

Proyek ini adalah fork dari **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** oleh **[@T3SL4](https://github.com/T3SL4)**, yang memelopori pipeline ekstraksi OTA ke prop. Di sini ia dibentuk ulang untuk menyimpan dan mendistribusikan berkas `.prop` alih-alih modul yang dapat dipasang. Seluruh penghargaan atas karya aslinya diberikan kepada penulisnya.

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

**GNU GPL-3.0-or-later** - lihat [LICENSE](LICENSE). Copyleft: siapa pun yang mendistribusikan versi yang dimodifikasi harus menawarkan kode sumbernya dengan syarat yang sama.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
