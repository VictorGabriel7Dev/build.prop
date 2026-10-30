[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | **Polski** | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Przeglądalne, automatycznie aktualizowane archiwum prawdziwych danych `build.prop` dla Pixela, prosto z oficjalnych obrazów Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Wersjonowane archiwum **ostatnich 4 kompilacji z każdego kanału** (stable, beta i canary) dla każdego współczesnego Pixela, wyodrębnione bezpośrednio z oficjalnych obrazów factory i OTA Google. Każdy wpis to **pełny** `build.prop`, scalony ze **wszystkich partycji** (system, system_ext, product, vendor, odm oraz obrazów `_dlkm`), i zawiera **`ro.boot.vbmeta.digest`** (hasz verified boot). Wszystko jest przechowywane w repozytorium, zindeksowane w maszynowo czytelnym `index.json` i publikowane jako zasoby wydania. Nie są wymagane żadne narzędzia.

## 📥 Get the data

Trzy sposoby, bez konfiguracji:

- **Przeglądaj repozytorium** - otwórz [`<codename>/`](.) i wybierz plik. Nazewnictwo według kanału:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - maszynowo czytelny manifest mapujący każde urządzenie → kanał → najnowszą kompilację, z `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` i `vbmeta_digest`. Idealny do automatyzacji i narzędzi.
- **Releases** - pobierz cały korpus jako jeden `.zip` (plus `index.json`) z najnowszego [release](https://github.com/VictorGabriel7Dev/build.prop/releases) (oznaczonego tagiem `build-YYYYMMDD`).

Każdy `.prop` to pełny, uporządkowany zestaw właściwości dla dokładnie tego urządzenia i tej kompilacji - wszystkie partycje, plus `ro.boot.vbmeta.digest`.

## 🗂️ What's inside

- **Każde współczesne urządzenie Pixel** (Pixel 6 i nowsze).
- **Trzy kanały na urządzenie** - stable, beta i canary, najnowsze kompilacje każdego z nich (zależnie od tego, co Google faktycznie publikuje; niektóre zupełnie nowe urządzenia mają na razie tylko jedną lub dwie kompilacje na canary).
- **Pełny `build.prop`** na każdą kompilację (~300-390 właściwości), scalony ze wszystkich partycji.
- **`vbmeta.digest`** (hasz verified boot) przechowywany obok właściwości.

## 🔧 Build one yourself

Aby wyodrębnić pojedynczy `.prop` lokalnie, zamiast go pobierać, potrzebujesz środowiska uniksopodobnego (Linux lub macOS z Bash) oraz `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` i Pythona ≥3.8 z `payload_dumper`. `requirements.sh` instaluje zależności w większości menedżerów pakietów (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Obsługiwane urządzenia to obrazy factory i OTA z [Google Android Images](https://developers.google.com/android/images) oraz [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Wyodrębnianie odczytuje każdą partycję payload po kolei (niskie zużycie pamięci) i obsługuje obrazy EROFS, ext4, sparse oraz boot/init_boot.

## 🤖 Automation

Archiwum jest automatycznie utrzymywane w aktualności: gdy Google publikuje nowe kompilacje, są one wyodrębniane (w całości, wszystkie partycje, z `vbmeta.digest`), nowe `.prop` są zatwierdzane pod `<codename>/`, `index.json` jest odświeżany, a datowane wydanie (`build-YYYYMMDD`) jest tworzone, aby obserwujący byli powiadamiani o każdej fali.

Dostępny jest też uniwersalny `.github/workflows/build.yml` na żądanie (`workflow_dispatch`) jako ręczna opcja awaryjna do zbudowania najnowszego `.prop` urządzenia.

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
