[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | **हिन्दी** | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*असली Pixel `.prop` फ़ाइलों का एक ब्राउज़ करने योग्य, स्वतः-अपडेट होने वाला संग्रह, सीधे Google की OTA इमेज से*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

प्रत्येक Pixel के पूर्ण `build.prop` का एक संस्करणबद्ध संग्रह, जो सीधे Google की आधिकारिक OTA इमेज से निकाला जाता है और स्वचालित रूप से अद्यतन रखा जाता है। हर डिवाइस की `.prop` रिपॉज़िटरी में संग्रहीत होती है और एक release एसेट के रूप में प्रकाशित की जाती है, बिना किसी टूलिंग की आवश्यकता के ब्राउज़ या डाउनलोड करने के लिए तैयार।

## 📥 Get a `.prop`

दो तरीके, किसी सेटअप की आवश्यकता नहीं:

- **रिपॉज़िटरी ब्राउज़ करें**: [`<codename>/`](.) खोलें और `<codename>_<build_id>.prop` चुनें।
- **Releases से डाउनलोड करें**: नवीनतम [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (टैग `build-YYYYMMDD`) से फ़ाइल प्राप्त करें।

प्रत्येक `.prop` उस सटीक डिवाइस और build के लिए build प्रॉपर्टीज़ का पूर्ण, व्यवस्थित सेट है (product, vendor, odm, system, system_ext, system_dlkm और अधिक)।

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

एक GitHub Actions पाइपलाइन (`.github/workflows/build.yml`) संग्रह को वर्तमान रखती है:

- साप्ताहिक रूप से चलती है, और `workflow_dispatch` के माध्यम से मांग पर, स्पेस से अलग की गई डिवाइस सूची या `all` के साथ; प्रत्येक डिवाइस समानांतर में build होता है।
- `.prop` निकालती है, नई फ़ाइलों को `<codename>/` के अंतर्गत कमिट करती है, और उन्हें एक ही दैनिक टैग (`build-YYYYMMDD`) के अंतर्गत एसेट के रूप में प्रकाशित करती है।
- पहले से रिलीज़ की जा चुकी `.prop` फ़ाइलों को छोड़ देती है और क्लिक करने योग्य डाउनलोड लिंक के साथ Telegram को सूचित करती है।

इस पाइपलाइन को चलाने वाले फ़ोर्क को दो secrets की आवश्यकता होती है: `TELEGRAM_BOT_TOKEN` ([@BotFather](https://t.me/BotFather) से) और `TELEGRAM_CHAT_ID`।

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

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
