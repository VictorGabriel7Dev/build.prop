[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | **العربية** | [ไทย](README.th.md)

# Pixel Prop Builder

*استخرج ووزّع ملف `.prop` الكامل لأجهزة Pixel مباشرةً من صور OTA من Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

استخرج خصائص النظام من تحديثات OTA لأجهزة Pixel وأدِرها بسهولة باستخدام مجموعة الأتمتة القوية هذه. تستخرج ملف `.prop` الكامل والمنظّم لكل جهاز مباشرةً من صور OTA الرسمية من Google، ثم **تخزّن وتوزّع ملفات `.prop` تلك** - سواء بإصدارات مُدارة في المستودع أو منشورة كأصول للإصدارات. لا وحدات قابلة للتثبيت: الخصائص فقط.

## 🚀 بداية سريعة

### المتطلبات المسبقة

- **بيئة شبيهة بيونكس**: لينكس أو macOS مع Bash.
- **الأدوات الأساسية**:
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

## التثبيت

1. **استنسخ المستودع**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **أنشئ بيئة افتراضية وفعّلها** (اختياري لكن يُنصح به):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **ثبّت الاعتماديات**:

    ```bash
    pip3 install payload_dumper
    ```

## الاستخدام

### محليًا

1. **احصل على أحدث صور OTA**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    أمثلة:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### الأجهزة المدعومة في صور المصنع أو OTA المطلوبة من [Google Android Images](https://developers.google.com/android/images) أو [صفحات OTA التجريبية](https://developer.android.com/about/versions/17/download-ota).

2. **استخرج الصور واجمع ملف `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    يقوم هذا تلقائيًا بما يلي:
    - استخراج أقسام payload.bin واحدًا تلو الآخر (استهلاك منخفض للذاكرة)
    - اكتشاف صور **EROFS** و**ext4** و**sparse** و**boot/init_boot** والتعامل معها
    - بناء ملف `.prop` الكامل والمنظّم من build.prop لكل قسم
    - حفظه في `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

يتضمّن المستودع خط أنابيب CI مؤتمتًا بالكامل (`.github/workflows/build.yml`):

- **عمليات بناء مجدولة**: تعمل كل يوم أحد عند منتصف الليل بتوقيت UTC.
- **تشغيل يدوي**: شغّله عبر `workflow_dispatch` بقائمة أجهزة مفصولة بمسافات أو `all`.
- **بناء مصفوفي**: تتم معالجة كل جهاز بالتوازي.
- **منع التكرار**: يتخطّى ملفات `.prop` الموجودة بالفعل في الإصدارات الحالية.
- **مُدار بالإصدارات في المستودع**: تُسجَّل ملفات `.prop` الجديدة ضمن `props/<codename>/`.
- **إصدارات مجمّعة**: تُنشر جميع ملفات `.prop` الجديدة تحت وسم يومي واحد (`build-YYYYMMDD`).
- **إشعارات Telegram**: يرسل رسالة منسّقة تتضمّن روابط تنزيل قابلة للنقر.

#### الأسرار المطلوبة

| السر | الوصف |
|------|-------|
| `TELEGRAM_BOT_TOKEN` | رمز بوت Telegram الخاص بك من [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | معرّف الدردشة المستهدفة (مستخدم أو مجموعة أو قناة) |

## ✨ الميزات الرئيسية

- **الحصول التلقائي على OTA**: يُنزّل أحدث عمليات البناء مباشرةً من مصادر Google الرسمية.
- **دعم أنظمة الملفات الحديثة**: يتعامل مع صور EROFS وext4 وsparse وramdisks الخاصة بـ boot/init_boot.
- **توليد ملف `.prop` الكامل**: يبني ملف `.prop` منظّمًا واحدًا لكل جهاز من build.prop لكل قسم (product وvendor وodm وsystem وsystem_ext وsystem_dlkm وغيرها).
- **استخراج موفّر للذاكرة**: تُفرَّغ أقسام payload واحدًا تلو الآخر لتجنّب نفاد الذاكرة (OOM) في ملفات OTA الكبيرة.
- **إدارة حزم متعددة المنصات**: يدعم `requirements.sh` كلًّا من apt وpacman وdnf وyum وzypper وapk وxbps وbrew وTermux.
- **التخزين والتوزيع**:
  - **في المستودع**: يُسجَّل كل `.prop` ضمن `props/<codename>/`، مُدارًا بالإصدارات وقابلًا للتصفّح.
  - **كأصول للإصدارات**: يُنشر كل `.prop` تحت الوسم اليومي للتنزيل المباشر.
- **التكامل مع GitHub Actions**:
  - **سير عمل مجدول**: يؤتمت التحديثات والاستخراج والإصدارات وفق جدول زمني.
  - **منع الإصدارات المكررة**: يتجنّب الإصدارات الزائدة عبر فحص أصول الإصدارات الحالية.
  - **إصدارات متكافئة (idempotent)**: يعيد الرفع إلى وسم إصدار يومي موجود عند إعادة التشغيل.
  - **إشعارات Telegram**: تلقَّ تحديثات في الوقت المناسب مع روابط تنزيل قابلة للنقر.

## 📝 إرشادات الاستخدام المسؤول

يُقدَّم هذا المشروع لأغراض تعليمية وتجريبية. ومع أنه مُصمَّم للكفاءة، فمن الضروري استخدام هذه الأداة بمسؤولية.

- **مراجعة الكود**: راجع الكود وافهمه جيدًا قبل نشره في أي بيئة.
- **أفضل ممارسات الأمان**: التزم بمعايير الصناعة للأمان والامتثال القانوني.

لا يتحمّل صانعو هذا المشروع أي مسؤولية عن أي سوء استخدام أو أضرار ناتجة عن استخدامه.

## شكر وتقدير

هذا المشروع هو فورك من **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** بقلم **[@T3SL4](https://github.com/T3SL4)**، الذي كان رائدًا في خط أنابيب الاستخراج من OTA إلى prop. وقد أُعيد تشكيله هنا لتخزين وتوزيع ملفات `.prop` بدلًا من الوحدات القابلة للتثبيت. كل الفضل في العمل الأصلي يعود إلى مؤلفه.

## التواصل

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## الترخيص

**GNU GPL-3.0-or-later** - راجع [LICENSE](LICENSE). حقوق متروكة (Copyleft): يجب على كل من يوزّع نسخة معدّلة أن يوفّر شفرتها المصدرية بالشروط نفسها.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
