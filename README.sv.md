[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | **Svenska** | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Ett bläddringsbart, automatiskt uppdaterat arkiv med riktiga Pixel-`.prop`-filer, direkt från Googles OTA-avbilder*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Ett versionshanterat arkiv med varje Pixels fullständiga `build.prop`, extraherat direkt från Googles officiella OTA-avbilder och automatiskt hållet uppdaterat. Varje enhets `.prop` lagras i förvaret och publiceras som en release-tillgång, redo att bläddra i eller ladda ner utan att några verktyg krävs.

## 📥 Get a `.prop`

Två sätt, ingen konfiguration behövs:

- **Bläddra i förvaret**: öppna [`props/<codename>/`](props/) och välj `<codename>_<build_id>.prop`.
- **Ladda ner från Releases**: hämta filen från den senaste [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (taggad `build-YYYYMMDD`).

Varje `.prop` är den fullständiga, organiserade uppsättningen byggegenskaper för exakt den enheten och den bygget (product, vendor, odm, system, system_ext, system_dlkm med mera).

## 🔧 Build it yourself

För att extrahera en `.prop` lokalt i stället för att ladda ner den behöver du en Unix-liknande miljö (Linux eller macOS med Bash) plus `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` och Python ≥3.8 med `payload_dumper`. `requirements.sh` installerar beroendena för de flesta pakethanterare (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Stödda enheter är factory- och OTA-avbilderna på [Google Android Images](https://developers.google.com/android/images) och [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Extraktionen läser varje payload-partition en i taget (lågt minnesbehov) och hanterar EROFS-, ext4-, sparse- och boot/init_boot-avbilder.

## 🤖 Automation

En GitHub Actions-pipeline (`.github/workflows/build.yml`) håller arkivet aktuellt:

- Körs varje vecka och på begäran via `workflow_dispatch` med en mellanslagsseparerad enhetslista eller `all`; varje enhet byggs parallellt.
- Extraherar `.prop`, committar nya under `props/<codename>/` och publicerar dem som tillgångar under en enda daglig tagg (`build-YYYYMMDD`).
- Hoppar över `.prop`-filer som redan släppts och aviserar Telegram med klickbara nedladdningslänkar.

Forkar som kör pipelinen behöver två hemligheter: `TELEGRAM_BOT_TOKEN` (från [@BotFather](https://t.me/BotFather)) och `TELEGRAM_CHAT_ID`.

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

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
