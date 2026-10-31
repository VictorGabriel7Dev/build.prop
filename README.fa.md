[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | **فارسی** | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*یک آرشیو قابل مرور و به‌روزرسانی‌شونده‌ی خودکار از داده‌های واقعی `build.prop` دستگاه‌های Pixel، مستقیماً از ایمیج‌های رسمی گوگل*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

یک آرشیو نسخه‌بندی‌شده از **۴ build آخر هر کانال** (stable، beta و canary) برای هر Pixel اخیر، که مستقیماً از ایمیج‌های رسمی factory و OTA گوگل استخراج شده است. هر مدخل، `build.prop` **کامل** است که در **همه‌ی پارتیشن‌ها** (system، system_ext، product، vendor، odm و ایمیج‌های `_dlkm`) ادغام شده و **`ro.boot.vbmeta.digest`** (هش verified boot) را به همراه دارد. همه‌چیز در مخزن ذخیره می‌شود، در یک `index.json` قابل‌خواندن توسط ماشین نمایه می‌گردد و به‌عنوان دارایی‌های release منتشر می‌شود. به هیچ ابزاری نیاز نیست.

## 📥 Get the data

سه راه، بدون نیاز به هیچ راه‌اندازی:

- **مرور مخزن**: [`<codename>/`](.) را باز کنید و یک فایل انتخاب کنید. نام‌گذاری بر اساس کانال:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`**: یک مانیفست قابل‌خواندن توسط ماشین که هر دستگاه → کانال → آخرین build را نگاشت می‌کند و شامل `model`، `soc`، `first_api_level`، `security_patch`، `android`، `build`، `incremental` و `vbmeta_digest` است. برای اتوماسیون و ابزارسازی ایده‌آل است.
- **Releases**: هر `.prop` به‌صورت جداگانه (به‌همراه `index.json`) به آخرین [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (با برچسب `build-YYYYMMDD`) پیوست می‌شود.

هر `.prop` مجموعه‌ی کامل و سازمان‌یافته‌ی ویژگی‌ها برای همان دستگاه و build دقیق است - همه‌ی پارتیشن‌ها، به‌علاوه‌ی `ro.boot.vbmeta.digest`.

## 🗂️ What's inside

- **هر دستگاه Pixel اخیر** (Pixel 6 و جدیدتر).
- **سه کانال برای هر دستگاه** - stable، beta و canary، آخرین build هر کدام (بسته به آنچه گوگل واقعاً منتشر می‌کند؛ برخی دستگاه‌های کاملاً جدید هنوز فقط یکی دو build روی canary دارند).
- **`build.prop` کامل** برای هر build (حدود ۳۰۰-۳۹۰ ویژگی)، ادغام‌شده از همه‌ی پارتیشن‌ها.
- **`vbmeta.digest`** (هش verified boot) در کنار ویژگی‌ها ذخیره می‌شود.

## 🔧 Build one yourself

برای استخراج یک `.prop` به‌صورت محلی به‌جای دانلود آن، به یک محیط شبه‌Unix (لینوکس یا macOS با Bash) به‌همراه `p7zip-full`، `e2fsprogs`، `erofs-utils`، `lz4`، `cpio`، `dos2unix`، `aria2`، `curl`، `xxd`، `jq` و Python ≥3.8 با `payload_dumper` نیاز دارید. `requirements.sh` وابستگی‌ها را در بیشتر مدیران بسته نصب می‌کند (apt، pacman، dnf، yum، zypper، apk، xbps، brew، Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

دستگاه‌های پشتیبانی‌شده همان ایمیج‌های factory و OTA در [Google Android Images](https://developers.google.com/android/images) و [صفحات Beta OTA](https://developer.android.com/about/versions/17/download-ota) هستند. استخراج هر پارتیشن payload را یکی‌یکی می‌خواند (مصرف حافظه‌ی کم) و ایمیج‌های EROFS، ext4، sparse و boot/init_boot را مدیریت می‌کند.

## 🤖 Automation

آرشیو به‌صورت خودکار به‌روز می‌ماند: به‌محض اینکه گوگل build‌های جدید را منتشر کند، آن‌ها استخراج می‌شوند (کامل، همه‌ی پارتیشن‌ها، با `vbmeta.digest`)، فایل‌های `.prop` جدید زیر `<codename>/` کامیت می‌شوند، `index.json` تازه‌سازی می‌شود و یک release تاریخ‌دار (`build-YYYYMMDD`) ساخته می‌شود تا دنبال‌کنندگان از هر موج به‌روزرسانی مطلع شوند.

یک `.github/workflows/build.yml` عمومی و درخواستی (`workflow_dispatch`) نیز به‌عنوان راه‌حل جایگزین دستی برای ساختن آخرین `.prop` یک دستگاه در دسترس است.

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
