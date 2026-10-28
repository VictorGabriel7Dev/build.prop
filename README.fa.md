[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | **فارسی** | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*`.prop` کامل پیکسل را مستقیماً از ایمیج‌های OTA گوگل استخراج و توزیع کنید*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

با این مجموعه‌ابزار خودکارسازی قدرتمند، ویژگی‌های سیستم را به‌سادگی از به‌روزرسانی‌های OTA پیکسل استخراج و مدیریت کنید. این ابزار `.prop` کامل و منظم هر دستگاه را مستقیماً از ایمیج‌های OTA رسمی گوگل استخراج می‌کند و سپس **آن فایل‌های `.prop` را ذخیره و توزیع می‌کند** - هم در مخزن نسخه‌بندی‌شده و هم به‌صورت دارایی‌های ریلیز منتشرشده. بدون ماژول قابل‌نصب: فقط ویژگی‌ها.

## 🚀 شروع سریع

### پیش‌نیازها

- **محیط شبه‌یونیکس**: لینوکس یا macOS همراه با Bash.
- **ابزارهای اصلی**:
  - `zip`، `unzip`، `p7zip-full`
  - `dos2unix`، `aria2`، `curl`
  - `e2fsprogs`، `erofs-utils`، `lz4`، `cpio`
  - `xxd`، `jq`
- **Python ≥3.8**:

    ```bash
    sudo apt-get update -y
    sudo apt-get install -y python3 python3-pip python3-venv jq xxd \
      p7zip-full e2fsprogs erofs-utils lz4 cpio dos2unix aria2 curl
    ```

## نصب

1. **مخزن را کلون کنید**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **یک محیط مجازی ایجاد و فعال کنید** (اختیاری اما توصیه‌شده):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **وابستگی‌ها را نصب کنید**:

    ```bash
    pip3 install payload_dumper
    ```

## استفاده

### محلی

1. **جدیدترین ایمیج‌های OTA را دریافت کنید**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    نمونه‌ها:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### دستگاه‌های پشتیبانی‌شده در ایمیج‌های کارخانه یا OTA دلخواه از [Google Android Images](https://developers.google.com/android/images) یا [صفحات OTA بتا](https://developer.android.com/about/versions/17/download-ota).

2. **ایمیج‌ها را استخراج و `.prop` را جمع‌آوری کنید**:

    ```bash
    ./extract_images.sh
    ```

    این کار به‌طور خودکار:
    - پارتیشن‌های payload.bin را یکی‌یکی استخراج می‌کند (مصرف حافظه کم)
    - ایمیج‌های **EROFS**، **ext4**، **sparse** و **boot/init_boot** را تشخیص داده و پردازش می‌کند
    - `.prop` کامل و منظم را از build.prop هر پارتیشن می‌سازد
    - آن را در `props/<codename>/<codename>_<build_id>.prop` ذخیره می‌کند

### GitHub Actions

این مخزن شامل یک خط‌لولهٔ CI کاملاً خودکار است (`.github/workflows/build.yml`):

- **ساخت‌های زمان‌بندی‌شده**: هر یکشنبه نیمه‌شب به وقت UTC اجرا می‌شوند.
- **اجرای دستی**: از طریق `workflow_dispatch` با فهرست دستگاه‌های جداشده با فاصله یا `all` اجرا کنید.
- **ساخت‌های ماتریسی**: هر دستگاه به‌صورت موازی پردازش می‌شود.
- **جلوگیری از تکرار**: فایل‌های `.prop` که از قبل در ریلیزهای موجود هستند را رد می‌کند.
- **نسخه‌بندی در مخزن**: فایل‌های `.prop` جدید در `props/<codename>/` کامیت می‌شوند.
- **ریلیزهای تجمیعی**: همهٔ فایل‌های `.prop` جدید زیر یک برچسب روزانهٔ واحد (`build-YYYYMMDD`) منتشر می‌شوند.
- **اعلان‌های تلگرام**: پیامی قالب‌بندی‌شده همراه با پیوندهای دانلود قابل‌کلیک ارسال می‌کند.

#### سیکرت‌های موردنیاز

| سیکرت | توضیح |
|-------|-------|
| `TELEGRAM_BOT_TOKEN` | توکن ربات تلگرام شما از [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | شناسهٔ چت مقصد (کاربر، گروه یا کانال) |

## ✨ ویژگی‌های کلیدی

- **دریافت خودکار OTA**: جدیدترین build‌ها را مستقیماً از منابع رسمی گوگل دانلود می‌کند.
- **پشتیبانی از سیستم‌فایل‌های امروزی**: ایمیج‌های EROFS، ext4، sparse و ramdisk‌های boot/init_boot را پردازش می‌کند.
- **تولید `.prop` کامل**: برای هر دستگاه یک `.prop` منظم واحد از build.prop هر پارتیشن می‌سازد (product، vendor، odm، system، system_ext، system_dlkm و موارد دیگر).
- **استخراج کم‌مصرف از نظر حافظه**: پارتیشن‌های payload یکی‌یکی تخلیه می‌شوند تا از OOM در OTAهای بزرگ جلوگیری شود.
- **مدیریت بسته‌های چندسکویی**: `requirements.sh` از apt، pacman، dnf، yum، zypper، apk، xbps، brew و Termux پشتیبانی می‌کند.
- **ذخیره‌سازی و توزیع**:
  - **در مخزن**: هر `.prop` در `props/<codename>/` کامیت می‌شود، نسخه‌بندی‌شده و قابل مرور.
  - **به‌عنوان دارایی ریلیز**: هر `.prop` برای دانلود مستقیم زیر برچسب روزانه منتشر می‌شود.
- **یکپارچگی با GitHub Actions**:
  - **گردش‌کارهای زمان‌بندی‌شده**: به‌روزرسانی‌ها، استخراج و ریلیزها را بر پایهٔ یک زمان‌بندی خودکار می‌کند.
  - **جلوگیری از ریلیز تکراری**: با بررسی دارایی‌های ریلیزهای موجود، از ریلیزهای زائد جلوگیری می‌کند.
  - **ریلیزهای خودتوان (idempotent)**: در صورت اجرای مجدد، دوباره در برچسب ریلیز روزانهٔ موجود بارگذاری می‌کند.
  - **اعلان‌های تلگرام**: به‌روزرسانی‌های به‌هنگام همراه با پیوندهای دانلود قابل‌کلیک دریافت کنید.

## 📝 رهنمودهای استفادهٔ مسئولانه

این پروژه برای مقاصد آموزشی و آزمایشی ارائه شده است. با وجود اینکه برای کارایی طراحی شده، استفادهٔ مسئولانه از این ابزار بسیار مهم است.

- **بازبینی کد**: پیش از به‌کارگیری در هر محیطی، کد را به‌دقت بازبینی و درک کنید.
- **بهترین شیوه‌های امنیتی**: به استانداردهای صنعتی امنیت و رعایت قانونی پایبند باشید.

سازندگان این پروژه مسئول هیچ‌گونه سوءاستفاده یا خساراتی که از کاربرد آن ناشی شود نیستند.

## قدردانی

این پروژه یک فورک از **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** ساختهٔ **[@T3SL4](https://github.com/T3SL4)** است که پیشگام خط‌لولهٔ استخراج از OTA به prop بود. در اینجا بازطراحی شده تا به‌جای ماژول‌های قابل‌نصب، فایل‌های `.prop` را ذخیره و توزیع کند. تمام اعتبار کار اصلی از آنِ نویسندهٔ آن است.

## تماس

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## مجوز

**GNU GPL-3.0-or-later** - به [LICENSE](LICENSE) مراجعه کنید. کپی‌لفت: هرکس نسخهٔ تغییریافته‌ای را توزیع کند باید کد منبع آن را با همان شرایط ارائه دهد.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
