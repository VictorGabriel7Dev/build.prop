[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | **Svenska** | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Ett bläddringsbart, automatiskt uppdaterat arkiv med riktiga Pixel-`build.prop`-data, direkt från Googles officiella avbilder*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Ett versionshanterat arkiv med **de senaste 4 byggena i varje kanal** (stable, beta och canary) för varje modern Pixel, extraherat direkt från Googles officiella factory- och OTA-avbilder. Varje post är den **fullständiga** `build.prop`, sammanslagen över **varje partition** (system, system_ext, product, vendor, odm och `_dlkm`-avbilderna), och innehåller **`ro.boot.vbmeta.digest`** (verified boot-hash). Allt lagras i förvaret, indexeras i en maskinläsbar `index.json` och publiceras som release-tillgångar. Inga verktyg krävs.

## 📥 Get the data

Tre sätt, ingen konfiguration behövs:

- **Bläddra i förvaret** - öppna [`<codename>/`](.) och välj en fil. Namngivning per kanal:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - ett maskinläsbart manifest som kopplar varje enhet → kanal → senaste bygge, med `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` och `vbmeta_digest`. Perfekt för automatisering och verktyg.
- **Releases** - varje `.prop` bifogas individuellt (plus `index.json`) till den senaste [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (taggad `build-YYYYMMDD`).

Varje `.prop` är den fullständiga, organiserade uppsättningen egenskaper för exakt den enheten och det bygget - alla partitioner, plus `ro.boot.vbmeta.digest`.

## 🗂️ What's inside

- **Varje modern Pixel-enhet** (Pixel 6 och nyare).
- **Tre kanaler per enhet** - stable, beta och canary, de senaste byggena av var och en (beroende på vad Google faktiskt publicerar; vissa helt nya enheter har hittills bara ett bygge eller två på canary).
- **Fullständig `build.prop`** per bygge (~300-390 egenskaper), sammanslagen från alla partitioner.
- **`vbmeta.digest`** (verified boot-hashen) lagrad tillsammans med egenskaperna.

## 🔧 Build one yourself

För att extrahera en enskild `.prop` lokalt i stället för att ladda ner den behöver du en Unix-liknande miljö (Linux eller macOS med Bash) plus `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` och Python ≥3.8 med `payload_dumper`. `requirements.sh` installerar beroendena för de flesta pakethanterare (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Stödda enheter är factory- och OTA-avbilderna på [Google Android Images](https://developers.google.com/android/images) och [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Extraktionen läser varje payload-partition en i taget (lågt minnesbehov) och hanterar EROFS-, ext4-, sparse- och boot/init_boot-avbilder.

## 🤖 Automation

Arkivet hålls automatiskt aktuellt: när Google publicerar nya byggen extraheras de (fullständigt, alla partitioner, med `vbmeta.digest`), de nya `.prop` committas under `<codename>/`, `index.json` uppdateras och en daterad release (`build-YYYYMMDD`) skapas så att de som bevakar förvaret aviseras om varje våg.

Det finns även en generisk `.github/workflows/build.yml` på begäran (`workflow_dispatch`) som ett manuellt reservalternativ för att bygga en enhets senaste `.prop`.

## Acknowledgements

Det här projektet är en fork av **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** av **[@T3SL4](https://github.com/T3SL4)**, som var först med OTA-till-prop-extraktionspipelinen. All heder för det ursprungliga arbetet går till dess upphovsman.

## Contact

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - se [LICENSE](LICENSE). Copyleft: den som distribuerar en modifierad version måste erbjuda dess källkod under samma villkor.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
