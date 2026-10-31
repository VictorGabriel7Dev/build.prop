[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | **हिन्दी** | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*असली Pixel `build.prop` डेटा का एक ब्राउज़ करने योग्य, स्वतः-अपडेट होने वाला संग्रह, सीधे Google की आधिकारिक इमेज से*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

हर हाल के Pixel के लिए **प्रत्येक channel के अंतिम 4 builds** (stable, beta और canary) का एक संस्करणबद्ध संग्रह, जो सीधे Google की आधिकारिक factory और OTA इमेज से निकाला जाता है। प्रत्येक प्रविष्टि **पूर्ण** `build.prop` है, जो **हर पार्टीशन** (system, system_ext, product, vendor, odm और `_dlkm` इमेज) से विलय किया गया है, और **`ro.boot.vbmeta.digest`** (verified boot hash) रखता है। सब कुछ रिपॉज़िटरी में संग्रहीत होता है, मशीन-पठनीय `index.json` में अनुक्रमित होता है, और release एसेट के रूप में प्रकाशित किया जाता है। किसी टूलिंग की आवश्यकता नहीं।

## 📥 Get the data

तीन तरीके, किसी सेटअप की आवश्यकता नहीं:

- **रिपॉज़िटरी ब्राउज़ करें** - [`<codename>/`](.) खोलें और एक फ़ाइल चुनें। channel के अनुसार नामकरण:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - एक मशीन-पठनीय मेनिफ़ेस्ट जो प्रत्येक डिवाइस → channel → नवीनतम build को मैप करता है, जिसमें `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` और `vbmeta_digest` होते हैं। स्वचालन और टूलिंग के लिए आदर्श।
- **Releases** - प्रत्येक `.prop` अलग-अलग संलग्न किया जाता है (साथ में `index.json`) नवीनतम [release](https://github.com/VictorGabriel7Dev/build.prop/releases) में (टैग `build-YYYYMMDD`)।

प्रत्येक `.prop` उस सटीक डिवाइस और build के लिए प्रॉपर्टीज़ का पूर्ण, व्यवस्थित सेट है - सभी पार्टीशन, साथ में `ro.boot.vbmeta.digest`।

## 🗂️ What's inside

- **हर हाल का Pixel डिवाइस** (Pixel 6 और नया)।
- **प्रति डिवाइस तीन channel** - stable, beta और canary, प्रत्येक के नवीनतम builds (यह इस पर निर्भर करता है कि Google वास्तव में क्या प्रकाशित करता है; कुछ बिल्कुल नए डिवाइस के पास canary पर अभी भी केवल एक या दो build होते हैं)।
- **पूर्ण `build.prop`** प्रति build (~300-390 प्रॉपर्टीज़), सभी पार्टीशन से विलय किया गया।
- **`vbmeta.digest`** (verified boot hash) प्रॉपर्टीज़ के साथ संग्रहीत।

## 🔧 Build it yourself

किसी `.prop` को डाउनलोड करने के बजाय स्थानीय रूप से निकालने के लिए, आपको एक Unix-जैसे वातावरण (Bash के साथ Linux या macOS) के साथ-साथ `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, और `payload_dumper` के साथ Python ≥3.8 की आवश्यकता है। `requirements.sh` अधिकांश पैकेज मैनेजरों में निर्भरताएँ स्थापित करता है (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux)।

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

समर्थित डिवाइस [Google Android Images](https://developers.google.com/android/images) और [Beta OTA पृष्ठों](https://developer.android.com/about/versions/17/download-ota) पर उपलब्ध factory और OTA इमेज हैं। निष्कर्षण प्रत्येक payload पार्टीशन को एक-एक करके पढ़ता है (कम मेमोरी) और EROFS, ext4, sparse तथा boot/init_boot इमेज को संभालता है।

## 🤖 Automation

संग्रह स्वचालित रूप से वर्तमान रहता है: जैसे ही Google नए builds प्रकाशित करता है, उन्हें निकाला जाता है (पूर्ण, सभी पार्टीशन, `vbmeta.digest` के साथ), नई `.prop` फ़ाइलें `<codename>/` के अंतर्गत कमिट की जाती हैं, `index.json` को ताज़ा किया जाता है, और एक दिनांकित release (`build-YYYYMMDD`) बनाई जाती है ताकि प्रत्येक लहर की सूचना वॉचर्स को मिल जाए।

किसी डिवाइस की नवीनतम `.prop` बनाने के लिए एक मैन्युअल फ़ॉलबैक के रूप में एक सामान्य, मांग-आधारित `.github/workflows/build.yml` भी उपलब्ध है (`workflow_dispatch`)।

## Acknowledgements

यह परियोजना **[@T3SL4](https://github.com/T3SL4)** द्वारा बनाई गई **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** का एक फ़ोर्क है, जिसने OTA-से-prop निष्कर्षण पाइपलाइन की शुरुआत की। मूल कार्य का पूरा श्रेय उसके लेखक को जाता है।

## संपर्क

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - [LICENSE](LICENSE) देखें। कॉपीलेफ्ट: जो कोई भी संशोधित संस्करण वितरित करता है, उसे उसका स्रोत समान शर्तों के तहत उपलब्ध कराना होगा।

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
