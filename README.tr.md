[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | **Türkçe** | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Gerçek Pixel `.prop` dosyalarının, doğrudan Google'ın OTA imajlarından alınan, göz atılabilir ve otomatik güncellenen bir arşivi*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Her Pixel'in tam `build.prop` dosyasının, doğrudan Google'ın resmi OTA imajlarından çıkarılan ve otomatik olarak güncel tutulan sürümlenmiş bir arşivi. Her cihazın `.prop` dosyası depoda saklanır ve bir sürüm varlığı olarak yayımlanır; hiçbir araç gerektirmeden göz atmaya veya indirmeye hazırdır.

## 📥 Bir `.prop` edinin

İki yol, kuruluma gerek yok:

- **Depoya göz atın**: [`props/<codename>/`](props/) dizinini açın ve `<codename>_<build_id>.prop` dosyasını seçin.
- **Sürümlerden indirin**: dosyayı en son [sürümden](https://github.com/VictorGabriel7Dev/build.prop/releases) alın (`build-YYYYMMDD` etiketli).

Her `.prop`, tam olarak o cihaz ve derleme için eksiksiz, düzenlenmiş derleme özellikleri kümesidir (product, vendor, odm, system, system_ext, system_dlkm ve daha fazlası).

## 🔧 Kendiniz derleyin

Bir `.prop` dosyasını indirmek yerine yerel olarak çıkarmak için, Unix benzeri bir ortama (Bash ile Linux veya macOS) ve ayrıca `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` ve `payload_dumper` ile Python ≥3.8 sürümüne ihtiyacınız vardır. `requirements.sh` bağımlılıkları çoğu paket yöneticisinde kurar (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Desteklenen cihazlar, [Google Android Images](https://developers.google.com/android/images) ve [Beta OTA sayfalarındaki](https://developer.android.com/about/versions/17/download-ota) fabrika ve OTA imajlarıdır. Çıkarma işlemi her payload bölümünü teker teker okur (düşük bellek) ve EROFS, ext4, sparse ve boot/init_boot imajlarını işler.

## 🤖 Otomasyon

Bir GitHub Actions ardışık düzeni (`.github/workflows/build.yml`) arşivi güncel tutar:

- Haftalık olarak ve istek üzerine `workflow_dispatch` aracılığıyla boşlukla ayrılmış bir cihaz listesi veya `all` ile çalışır; her cihaz paralel olarak derlenir.
- `.prop` dosyasını çıkarır, yenilerini `props/<codename>/` altına commitler ve bunları tek bir günlük etiket (`build-YYYYMMDD`) altında varlık olarak yayımlar.
- Zaten yayımlanmış `.prop` dosyalarını atlar ve tıklanabilir indirme bağlantılarıyla Telegram'ı bilgilendirir.

Ardışık düzeni çalıştıran çatalların iki gizli değere ihtiyacı vardır: `TELEGRAM_BOT_TOKEN` ([@BotFather](https://t.me/BotFather) üzerinden) ve `TELEGRAM_CHAT_ID`.

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

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
