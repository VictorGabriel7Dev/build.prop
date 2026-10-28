[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | **فارسی** | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*یک آرشیو قابل مرور و به‌روزرسانی‌شونده‌ی خودکار از فایل‌های واقعی `.prop` دستگاه‌های Pixel، مستقیماً از ایمیج‌های OTA گوگل*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

یک آرشیو نسخه‌بندی‌شده از `build.prop` کامل هر دستگاه Pixel، که مستقیماً از ایمیج‌های رسمی OTA گوگل استخراج شده و به‌صورت خودکار به‌روز نگه داشته می‌شود. فایل `.prop` هر دستگاه در مخزن ذخیره می‌شود و به‌عنوان دارایی یک release منتشر می‌گردد، آماده‌ی مرور یا دانلود بدون نیاز به هیچ ابزاری.

## 📥 Get a `.prop`

دو راه، بدون نیاز به هیچ راه‌اندازی:

- **مرور مخزن**: [`props/<codename>/`](props/) را باز کنید و `<codename>_<build_id>.prop` را انتخاب کنید.
- **دانلود از Releases**: فایل را از آخرین [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (با برچسب `build-YYYYMMDD`) بگیرید.

هر `.prop` مجموعه‌ی کامل و سازمان‌یافته‌ی ویژگی‌های build برای همان دستگاه و build دقیق است (product، vendor، odm، system، system_ext، system_dlkm و بیشتر).

## 🔧 Build it yourself

برای استخراج یک `.prop` به‌صورت محلی به‌جای دانلود آن، به یک محیط شبه‌Unix (لینوکس یا macOS با Bash) به‌همراه `p7zip-full`، `e2fsprogs`، `erofs-utils`، `lz4`، `cpio`، `dos2unix`، `aria2`، `curl`، `xxd`، `jq` و Python ≥3.8 با `payload_dumper` نیاز دارید. `requirements.sh` وابستگی‌ها را در بیشتر مدیران بسته نصب می‌کند (apt، pacman، dnf، yum، zypper، apk، xbps، brew، Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

دستگاه‌های پشتیبانی‌شده همان ایمیج‌های factory و OTA در [Google Android Images](https://developers.google.com/android/images) و [صفحات Beta OTA](https://developer.android.com/about/versions/17/download-ota) هستند. استخراج هر پارتیشن payload را یکی‌یکی می‌خواند (مصرف حافظه‌ی کم) و ایمیج‌های EROFS، ext4، sparse و boot/init_boot را مدیریت می‌کند.

## 🤖 Automation

یک خط‌لوله‌ی GitHub Actions (`.github/workflows/build.yml`) آرشیو را به‌روز نگه می‌دارد:

- به‌صورت هفتگی اجرا می‌شود و به‌صورت درخواستی از طریق `workflow_dispatch` با فهرستی از دستگاه‌ها که با فاصله جدا شده‌اند یا `all`؛ هر دستگاه به‌صورت موازی build می‌شود.
- `.prop` را استخراج می‌کند، موارد جدید را زیر `props/<codename>/` کامیت می‌کند و آن‌ها را به‌عنوان دارایی‌ها زیر یک برچسب روزانه‌ی واحد (`build-YYYYMMDD`) منتشر می‌کند.
- از فایل‌های `.prop` که قبلاً منتشر شده‌اند صرف‌نظر می‌کند و تلگرام را با لینک‌های دانلود قابل‌کلیک مطلع می‌سازد.

فورک‌هایی که این خط‌لوله را اجرا می‌کنند به دو secret نیاز دارند: `TELEGRAM_BOT_TOKEN` (از [@BotFather](https://t.me/BotFather)) و `TELEGRAM_CHAT_ID`.

## Acknowledgements

این پروژه یک فورک از **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** ساخته‌ی **[@T3SL4](https://github.com/T3SL4)** است، که خط‌لوله‌ی استخراج OTA-به-prop را پایه‌گذاری کرد. تمام اعتبار کار اصلی به نویسنده‌ی آن تعلق دارد.

## تماس

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - به [LICENSE](LICENSE) مراجعه کنید. کپی‌لفت: هر کسی که نسخه‌ای تغییریافته را توزیع می‌کند باید سورس آن را تحت همان شرایط ارائه دهد.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
