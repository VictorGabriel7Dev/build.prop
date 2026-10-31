[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | **العربية** | [ไทย](README.th.md)

# Pixel Prop Builder

*أرشيف قابل للتصفح ويُحدَّث تلقائياً لبيانات `build.prop` الحقيقية لأجهزة Pixel، مأخوذة مباشرة من صور Google الرسمية*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

أرشيف مُصدَّر يضم **آخر 4 إصدارات (builds) من كل قناة** (stable وbeta وcanary) لكل جهاز Pixel حديث، مُستخرَج مباشرة من صور factory وOTA الرسمية من Google. كل مُدخَل هو `build.prop` **الكامل**، مدموج عبر **كل الأقسام** (system وsystem_ext وproduct وvendor وodm وصور `_dlkm`)، ويحمل **`ro.boot.vbmeta.digest`** (قيمة تجزئة verified boot). كل شيء مُخزَّن في المستودع، ومُفهرَس في ملف `index.json` قابل للقراءة آلياً، ومنشور كأصول ضمن release. لا حاجة إلى أي أدوات.

## 📥 Get the data

ثلاث طرق، دون الحاجة إلى أي إعداد:

- **تصفَّح المستودع**: افتح [`<codename>/`](.) واختر ملفاً. التسمية بحسب القناة:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`**: بيان قابل للقراءة آلياً يربط كل جهاز → قناة → أحدث build، مع `model` و`soc` و`first_api_level` و`security_patch` و`android` و`build` و`incremental` و`vbmeta_digest`. مثالي للأتمتة والأدوات.
- **Releases**: يُرفَق كل `.prop` على حِدة (بالإضافة إلى `index.json`) بأحدث [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (الموسوم بـ `build-YYYYMMDD`).

كل ملف `.prop` هو المجموعة الكاملة والمنظَّمة من الخصائص لذلك الجهاز وذلك الإصدار بالتحديد - كل الأقسام، بالإضافة إلى `ro.boot.vbmeta.digest`.

## 🗂️ What's inside

- **كل جهاز Pixel حديث** (Pixel 6 وما بعده).
- **ثلاث قنوات لكل جهاز** - stable وbeta وcanary، أحدث إصدار من كل منها (رهناً بما تنشره Google فعلياً؛ بعض الأجهزة الجديدة تماماً لا تزال تحتوي على إصدار أو اثنين فقط على canary).
- **`build.prop` الكامل** لكل build (نحو 300-390 خاصية)، مدموج من كل الأقسام.
- **`vbmeta.digest`** (قيمة تجزئة verified boot) مُخزَّن جنباً إلى جنب مع الخصائص.

## 🔧 Build one yourself

لاستخراج ملف `.prop` واحد محلياً بدلاً من تنزيله، تحتاج إلى بيئة شبيهة بـ Unix (Linux أو macOS مع Bash) بالإضافة إلى `p7zip-full` و`e2fsprogs` و`erofs-utils` و`lz4` و`cpio` و`dos2unix` و`aria2` و`curl` و`xxd` و`jq`، وPython ≥3.8 مع `payload_dumper`. يقوم `requirements.sh` بتثبيت التبعيات عبر معظم مديري الحزم (apt وpacman وdnf وyum وzypper وapk وxbps وbrew وTermux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

الأجهزة المدعومة هي صور factory وOTA الموجودة على [Google Android Images](https://developers.google.com/android/images) و[صفحات Beta OTA](https://developer.android.com/about/versions/17/download-ota). يقرأ الاستخراج كل قسم payload واحداً تلو الآخر (ذاكرة منخفضة) ويتعامل مع صور EROFS وext4 وsparse وboot/init_boot.

## 🤖 Automation

يبقى الأرشيف محدَّثاً تلقائياً: ما إن تنشر Google إصدارات جديدة حتى تُستخرَج (كاملة، كل الأقسام، مع `vbmeta.digest`)، وتُودَع ملفات `.prop` الجديدة ضمن `<codename>/`، ويُحدَّث `index.json`، ويُنشأ release مؤرَّخ (`build-YYYYMMDD`) كي يُخطَر المتابعون بكل موجة.

يتوفر أيضاً ملف `.github/workflows/build.yml` عام وعند الطلب (`workflow_dispatch`) كحل بديل يدوي لبناء أحدث `.prop` لجهاز ما.

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
