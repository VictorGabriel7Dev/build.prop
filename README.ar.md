[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | **العربية** | [ไทย](README.th.md)

# Pixel Prop Builder

*أرشيف قابل للتصفح ويُحدَّث تلقائياً لملفات `.prop` الحقيقية لأجهزة Pixel، مأخوذة مباشرة من صور OTA من Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

أرشيف مُصدَّر لملف `build.prop` الكامل لكل جهاز Pixel، مُستخرَج مباشرة من صور OTA الرسمية من Google ويُبقى مُحدَّثاً تلقائياً. يُخزَّن ملف `.prop` لكل جهاز في المستودع ويُنشَر كأصل ضمن release، جاهز للتصفح أو التنزيل دون الحاجة إلى أي أدوات.

## 📥 Get a `.prop`

طريقتان، دون الحاجة إلى أي إعداد:

- **تصفَّح المستودع**: افتح [`props/<codename>/`](props/) واختر `<codename>_<build_id>.prop`.
- **نزِّل من Releases**: احصل على الملف من أحدث [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (الموسوم بـ `build-YYYYMMDD`).

كل ملف `.prop` هو المجموعة الكاملة والمنظَّمة من خصائص build لذلك الجهاز وذلك الإصدار بالتحديد (product وvendor وodm وsystem وsystem_ext وsystem_dlkm وأكثر).

## 🔧 Build it yourself

لاستخراج ملف `.prop` محلياً بدلاً من تنزيله، تحتاج إلى بيئة شبيهة بـ Unix (Linux أو macOS مع Bash) بالإضافة إلى `p7zip-full` و`e2fsprogs` و`erofs-utils` و`lz4` و`cpio` و`dos2unix` و`aria2` و`curl` و`xxd` و`jq`، وPython ≥3.8 مع `payload_dumper`. يقوم `requirements.sh` بتثبيت التبعيات عبر معظم مديري الحزم (apt وpacman وdnf وyum وzypper وapk وxbps وbrew وTermux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

الأجهزة المدعومة هي صور factory وOTA الموجودة على [Google Android Images](https://developers.google.com/android/images) و[صفحات Beta OTA](https://developer.android.com/about/versions/17/download-ota). يقرأ الاستخراج كل قسم payload واحداً تلو الآخر (ذاكرة منخفضة) ويتعامل مع صور EROFS وext4 وsparse وboot/init_boot.

## 🤖 Automation

يُبقي خط أنابيب GitHub Actions (`.github/workflows/build.yml`) الأرشيف محدَّثاً:

- يعمل أسبوعياً، وعند الطلب عبر `workflow_dispatch` بقائمة أجهزة مفصولة بمسافات أو `all`؛ يُبنى كل جهاز بالتوازي.
- يستخرج ملف `.prop`، ويُودِع الملفات الجديدة ضمن `props/<codename>/`، وينشرها كأصول ضمن وسم يومي واحد (`build-YYYYMMDD`).
- يتخطى ملفات `.prop` التي سبق إصدارها ويُخطر Telegram بروابط تنزيل قابلة للنقر.

تحتاج النسخ المتفرعة التي تشغّل خط الأنابيب إلى سرّين اثنين: `TELEGRAM_BOT_TOKEN` (من [@BotFather](https://t.me/BotFather)) و`TELEGRAM_CHAT_ID`.

## Acknowledgements

هذا المشروع هو نسخة متفرعة من **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** من إعداد **[@T3SL4](https://github.com/T3SL4)**، الذي كان رائداً في خط أنابيب الاستخراج من OTA إلى prop. كل الفضل في العمل الأصلي يعود إلى مؤلفه.

## التواصل

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - راجع [LICENSE](LICENSE). كوبي‌لفت: على كل من يوزّع نسخة معدَّلة أن يُتيح شفرتها المصدرية وفق الشروط ذاتها.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
