[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | **Türkçe** | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Pixel'in tam `.prop` dosyasını doğrudan Google'ın OTA imajlarından çıkar ve dağıt*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Bu sağlam otomasyon paketiyle Pixel OTA güncellemelerinden sistem özelliklerini zahmetsizce çıkarın ve yönetin. Her cihazın tam ve düzenli `.prop` dosyasını doğrudan Google'ın resmi OTA imajlarından çıkarır, ardından **bu `.prop` dosyalarını saklar ve dağıtır** - hem depoda sürümlenmiş hem de release asset'i olarak yayımlanmış. Kurulabilir modül yok: yalnızca özellikler.

## 🚀 Hızlı Başlangıç

### Önkoşullar

- **Unix benzeri ortam**: Bash ile Linux veya macOS.
- **Temel araçlar**:
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

## Kurulum

1. **Depoyu klonlayın**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Bir sanal ortam oluşturun ve etkinleştirin** (isteğe bağlı ama önerilir):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Bağımlılıkları yükleyin**:

    ```bash
    pip3 install payload_dumper
    ```

## Kullanım

### Yerel

1. **En son OTA görüntülerini indirin**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Örnekler:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### [Google Android Images](https://developers.google.com/android/images) veya [Beta OTA sayfalarındaki](https://developer.android.com/about/versions/17/download-ota) istenen fabrika ya da OTA görüntülerinde desteklenen cihazlar.

2. **Görüntüleri çıkarın ve `.prop` dosyasını toplayın**:

    ```bash
    ./extract_images.sh
    ```

    Bu otomatik olarak:
    - payload.bin bölümlerini birer birer çıkarır (düşük bellek kullanımı)
    - **EROFS**, **ext4**, **sparse** ve **boot/init_boot** görüntülerini algılar ve işler
    - Her bölümün build.prop dosyasından tam ve düzenli `.prop` oluşturur
    - Onu `props/<codename>/<codename>_<build_id>.prop` konumuna kaydeder

### GitHub Actions

Depo, tamamen otomatik bir CI işlem hattı içerir (`.github/workflows/build.yml`):

- **Zamanlanmış derlemeler**: her Pazar gece yarısı UTC'de çalışır.
- **Manuel tetikleme**: boşlukla ayrılmış bir cihaz listesi veya `all` ile `workflow_dispatch` üzerinden tetikleyin.
- **Matris derlemeleri**: her cihaz paralel olarak işlenir.
- **Yinelenme önleme**: mevcut sürümlerde zaten bulunan `.prop` dosyalarını atlar.
- **Depoda sürümlenir**: yeni `.prop` dosyaları `props/<codename>/` altına commit'lenir.
- **Toplu sürümler**: tüm yeni `.prop` dosyaları tek bir günlük etiket (`build-YYYYMMDD`) altında yayımlanır.
- **Telegram bildirimleri**: tıklanabilir indirme bağlantıları içeren biçimlendirilmiş bir mesaj gönderir.

#### Gerekli secret'lar

| Secret | Açıklama |
|--------|----------|
| `TELEGRAM_BOT_TOKEN` | [@BotFather](https://t.me/BotFather) üzerinden alınan Telegram bot token'ınız |
| `TELEGRAM_CHAT_ID` | Hedef sohbet kimliği (kullanıcı, grup veya kanal) |

## ✨ Temel Özellikler

- **Otomatik OTA edinimi**: en son derlemeleri doğrudan Google'ın resmi kaynaklarından indirir.
- **Modern dosya sistemi desteği**: EROFS, ext4, sparse görüntülerini ve boot/init_boot ramdisk'lerini işler.
- **Tam `.prop` oluşturma**: her bölümün build.prop dosyasından cihaz başına tek, düzenli bir `.prop` oluşturur (product, vendor, odm, system, system_ext, system_dlkm ve daha fazlası).
- **Bellek açısından verimli çıkarma**: büyük OTA'larda OOM'u önlemek için payload bölümleri birer birer dökülür.
- **Çapraz platform paket yönetimi**: `requirements.sh`; apt, pacman, dnf, yum, zypper, apk, xbps, brew ve Termux'u destekler.
- **Depolama ve dağıtım**:
  - **Depoda**: her `.prop`, `props/<codename>/` altına commit'lenir, sürümlenir ve göz atılabilir.
  - **Release asset'i olarak**: her `.prop`, doğrudan indirme için günlük etiket altında yayımlanır.
- **GitHub Actions entegrasyonu**:
  - **Zamanlanmış iş akışları**: güncellemeleri, çıkarmayı ve sürümleri bir programa göre otomatikleştirir.
  - **Yinelenen sürüm önleme**: mevcut sürüm asset'lerini kontrol ederek gereksiz sürümleri önler.
  - **İdempotent sürümler**: yeniden tetiklenirse mevcut bir günlük sürüm etiketine yeniden yükler.
  - **Telegram bildirimleri**: tıklanabilir indirme bağlantılarıyla zamanında güncellemeler alın.

## 📝 Sorumlu Kullanım Yönergeleri

Bu proje eğitim ve deneysel amaçlarla sağlanmaktadır. Verimlilik için tasarlanmış olsa da bu aracı sorumlu bir şekilde kullanmak çok önemlidir.

- **Kod incelemesi**: kodu herhangi bir ortamda dağıtmadan önce iyice inceleyin ve anlayın.
- **En iyi güvenlik uygulamaları**: güvenlik ve yasal uyumluluk için sektör standartlarına uyun.

Bu projenin yaratıcıları, kötüye kullanımdan veya kullanımından doğan zararlardan sorumlu değildir.

## Teşekkürler

Bu proje, OTA'dan prop'a çıkarma işlem hattına öncülük eden **[@T3SL4](https://github.com/T3SL4)** tarafından geliştirilen **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** projesinin bir fork'udur. Burada, kurulabilir modüller yerine `.prop` dosyalarını saklamak ve dağıtmak için yeniden şekillendirilmiştir. Orijinal çalışmanın tüm kredisi yazarına aittir.

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

**GNU GPL-3.0-or-later** - bkz. [LICENSE](LICENSE). Copyleft: değiştirilmiş bir sürümü dağıtan herkes, kaynak kodunu aynı koşullarda sunmalıdır.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
