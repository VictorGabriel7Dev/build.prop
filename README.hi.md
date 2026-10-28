[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | **हिन्दी** | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Pixel की पूरी `.prop` को सीधे Google की OTA इमेज से निकालें और वितरित करें*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

इस मज़बूत ऑटोमेशन सुइट से Pixel OTA अपडेट से सिस्टम प्रॉपर्टीज़ को आसानी से निकालें और प्रबंधित करें। यह प्रत्येक डिवाइस की पूरी, व्यवस्थित `.prop` को सीधे Google की आधिकारिक OTA इमेज से निकालता है और फिर **उन `.prop` फ़ाइलों को संग्रहीत और वितरित करता है** - रिपॉज़िटरी में संस्करणित और रिलीज़ एसेट के रूप में प्रकाशित दोनों। कोई इंस्टॉल करने योग्य मॉड्यूल नहीं: केवल प्रॉपर्टीज़।

## 🚀 त्वरित शुरुआत

### पूर्वापेक्षाएँ

- **Unix-जैसा वातावरण**: Bash वाला Linux या macOS।
- **मुख्य उपयोगिताएँ**:
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

## स्थापना

1. **रिपॉज़िटरी क्लोन करें**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **एक वर्चुअल एनवायरनमेंट बनाएँ और सक्रिय करें** (वैकल्पिक, पर अनुशंसित):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **निर्भरताएँ स्थापित करें**:

    ```bash
    pip3 install payload_dumper
    ```

## उपयोग

### स्थानीय

1. **नवीनतम OTA इमेज प्राप्त करें**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    उदाहरण:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### [Google Android Images](https://developers.google.com/android/images) या [Beta OTA पृष्ठों](https://developer.android.com/about/versions/17/download-ota) से वांछित फ़ैक्टरी या OTA इमेज में समर्थित डिवाइस।

2. **इमेज निकालें और `.prop` एकत्र करें**:

    ```bash
    ./extract_images.sh
    ```

    यह स्वतः:
    - payload.bin के विभाजनों को एक-एक करके निकालता है (कम मेमोरी उपयोग)
    - **EROFS**, **ext4**, **sparse** और **boot/init_boot** इमेज का पता लगाता और संभालता है
    - प्रत्येक विभाजन की build.prop से पूरी, व्यवस्थित `.prop` बनाता है
    - इसे `props/<codename>/<codename>_<build_id>.prop` में सहेजता है

### GitHub Actions

रिपॉज़िटरी में एक पूर्णतः स्वचालित CI पाइपलाइन (`.github/workflows/build.yml`) शामिल है:

- **अनुसूचित बिल्ड**: हर रविवार UTC मध्यरात्रि को चलते हैं।
- **मैन्युअल ट्रिगर**: स्पेस से अलग किए गए डिवाइस सूची या `all` के साथ `workflow_dispatch` से ट्रिगर करें।
- **मैट्रिक्स बिल्ड**: प्रत्येक डिवाइस समानांतर में संसाधित होता है।
- **डुप्लिकेट रोकथाम**: मौजूदा रिलीज़ में पहले से मौजूद `.prop` फ़ाइलों को छोड़ देता है।
- **रिपॉज़िटरी में संस्करणित**: नई `.prop` फ़ाइलें `props/<codename>/` के अंतर्गत कमिट की जाती हैं।
- **समेकित रिलीज़**: सभी नई `.prop` फ़ाइलें एक ही दैनिक टैग (`build-YYYYMMDD`) के अंतर्गत प्रकाशित होती हैं।
- **Telegram सूचनाएँ**: क्लिक करने योग्य डाउनलोड लिंक के साथ एक स्वरूपित संदेश भेजता है।

#### आवश्यक Secrets

| Secret | विवरण |
|--------|-------|
| `TELEGRAM_BOT_TOKEN` | [@BotFather](https://t.me/BotFather) से प्राप्त आपका Telegram बॉट टोकन |
| `TELEGRAM_CHAT_ID` | लक्ष्य चैट ID (उपयोगकर्ता, समूह या चैनल) |

## ✨ मुख्य विशेषताएँ

- **स्वचालित OTA प्राप्ति**: नवीनतम बिल्ड सीधे Google के आधिकारिक स्रोतों से डाउनलोड करता है।
- **आधुनिक फ़ाइल सिस्टम समर्थन**: EROFS, ext4, sparse इमेज और boot/init_boot ramdisks को संभालता है।
- **पूरी `.prop` निर्माण**: प्रत्येक विभाजन की build.prop से प्रति डिवाइस एक व्यवस्थित `.prop` बनाता है (product, vendor, odm, system, system_ext, system_dlkm आदि)।
- **मेमोरी-कुशल निष्कर्षण**: बड़े OTA पर OOM से बचने के लिए payload विभाजन एक-एक करके डंप किए जाते हैं।
- **क्रॉस-प्लेटफ़ॉर्म पैकेज प्रबंधन**: `requirements.sh` apt, pacman, dnf, yum, zypper, apk, xbps, brew और Termux का समर्थन करता है।
- **संग्रहण और वितरण**:
  - **रिपॉज़िटरी में**: प्रत्येक `.prop` `props/<codename>/` के अंतर्गत कमिट होती है, संस्करणित और ब्राउज़ करने योग्य।
  - **रिलीज़ एसेट के रूप में**: प्रत्येक `.prop` सीधे डाउनलोड के लिए दैनिक टैग के अंतर्गत प्रकाशित होती है।
- **GitHub Actions एकीकरण**:
  - **अनुसूचित वर्कफ़्लो**: अपडेट, निष्कर्षण और रिलीज़ को एक शेड्यूल पर स्वचालित करते हैं।
  - **डुप्लिकेट रिलीज़ रोकथाम**: मौजूदा रिलीज़ की संपत्तियों की जाँच करके अनावश्यक रिलीज़ से बचता है।
  - **इडेम्पोटेंट रिलीज़**: पुनः ट्रिगर होने पर मौजूदा दैनिक रिलीज़ टैग में फिर से अपलोड करता है।
  - **Telegram सूचनाएँ**: क्लिक करने योग्य डाउनलोड लिंक के साथ समय पर अपडेट प्राप्त करें।

## 📝 उत्तरदायी उपयोग दिशानिर्देश

यह परियोजना शैक्षिक और प्रयोगात्मक उद्देश्यों के लिए प्रदान की गई है। यद्यपि यह दक्षता के लिए बनाई गई है, इस उपकरण का उत्तरदायी ढंग से उपयोग करना अत्यंत महत्वपूर्ण है।

- **कोड समीक्षा**: किसी भी वातावरण में तैनात करने से पहले कोड की भली-भाँति समीक्षा करें और उसे समझें।
- **सुरक्षा सर्वोत्तम प्रथाएँ**: सुरक्षा और कानूनी अनुपालन के उद्योग मानकों का पालन करें।

इस परियोजना के निर्माता इसके उपयोग से होने वाले किसी भी दुरुपयोग या क्षति के लिए उत्तरदायी नहीं हैं।

## आभार

यह परियोजना **[@T3SL4](https://github.com/T3SL4)** की **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** का एक फ़ोर्क है, जिन्होंने OTA से prop तक की निष्कर्षण पाइपलाइन का बीड़ा उठाया। यहाँ इसे इंस्टॉल करने योग्य मॉड्यूल के बजाय `.prop` फ़ाइलों को संग्रहीत और वितरित करने के लिए पुनर्गठित किया गया है। मूल कार्य का पूरा श्रेय इसके लेखक को जाता है।

## संपर्क

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## लाइसेंस

**GNU GPL-3.0-or-later** - [LICENSE](LICENSE) देखें। कॉपीलेफ़्ट: जो कोई संशोधित संस्करण वितरित करता है, उसे उसी शर्तों पर उसका स्रोत कोड उपलब्ध कराना होगा।

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
