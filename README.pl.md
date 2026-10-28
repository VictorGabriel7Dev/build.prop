[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | **Polski** | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Przeglądalne, automatycznie aktualizowane archiwum prawdziwych plików Pixel `.prop`, prosto z obrazów OTA Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Wersjonowane archiwum pełnego `build.prop` każdego Pixela, wyodrębnione bezpośrednio z oficjalnych obrazów OTA Google i automatycznie utrzymywane w aktualności. Plik `.prop` każdego urządzenia jest przechowywany w repozytorium i publikowany jako zasób wydania, gotowy do przeglądania lub pobrania bez potrzeby jakichkolwiek narzędzi.

## 📥 Get a `.prop`

Dwa sposoby, bez konfiguracji:

- **Przeglądaj repozytorium**: otwórz [`props/<codename>/`](props/) i wybierz `<codename>_<build_id>.prop`.
- **Pobierz z Releases**: pobierz plik z najnowszego [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (oznaczonego tagiem `build-YYYYMMDD`).

Każdy `.prop` to pełny, uporządkowany zestaw właściwości kompilacji dla dokładnie tego urządzenia i tej kompilacji (product, vendor, odm, system, system_ext, system_dlkm i więcej).

## 🔧 Build it yourself

Aby wyodrębnić `.prop` lokalnie, zamiast go pobierać, potrzebujesz środowiska uniksopodobnego (Linux lub macOS z Bash) oraz `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` i Pythona ≥3.8 z `payload_dumper`. `requirements.sh` instaluje zależności w większości menedżerów pakietów (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
pip3 install payload_dumper
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Obsługiwane urządzenia to obrazy factory i OTA z [Google Android Images](https://developers.google.com/android/images) oraz [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Wyodrębnianie odczytuje każdą partycję payload po kolei (niskie zużycie pamięci) i obsługuje obrazy EROFS, ext4, sparse oraz boot/init_boot.

## 🤖 Automation

Potok GitHub Actions (`.github/workflows/build.yml`) utrzymuje archiwum w aktualności:

- Uruchamia się co tydzień oraz na żądanie przez `workflow_dispatch` z listą urządzeń rozdzieloną spacjami lub `all`; każde urządzenie jest budowane równolegle.
- Wyodrębnia `.prop`, zatwierdza nowe pod `props/<codename>/` i publikuje je jako zasoby pod jednym dziennym tagiem (`build-YYYYMMDD`).
- Pomija pliki `.prop` już wydane i powiadamia Telegram klikalnymi linkami do pobrania.

Forki uruchamiające potok potrzebują dwóch sekretów: `TELEGRAM_BOT_TOKEN` (od [@BotFather](https://t.me/BotFather)) i `TELEGRAM_CHAT_ID`.

## Acknowledgements

Ten projekt jest forkiem **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** autorstwa **[@T3SL4](https://github.com/T3SL4)**, który jako pierwszy opracował potok wyodrębniania OTA-do-prop. Pełne uznanie za oryginalną pracę należy się jej autorowi.

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

**GNU GPL-3.0-or-later** - zobacz [LICENSE](LICENSE). Copyleft: każdy, kto rozpowszechnia zmodyfikowaną wersję, musi udostępnić jej kod źródłowy na tych samych warunkach.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
