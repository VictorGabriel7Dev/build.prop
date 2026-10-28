[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | **Polski** | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Wyodrębniaj i dystrybuuj pełny `.prop` Pixela prosto z obrazów OTA Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Bez wysiłku wyodrębniaj i zarządzaj właściwościami systemu z aktualizacji OTA urządzeń Pixel dzięki temu solidnemu zestawowi automatyzacji. Wyodrębnia pełny, uporządkowany `.prop` każdego urządzenia prosto z oficjalnych obrazów OTA Google, a następnie **przechowuje i dystrybuuje te pliki `.prop`** - zarówno wersjonowane w repozytorium, jak i publikowane jako zasoby wydań. Bez instalowalnych modułów: tylko właściwości.

## 🚀 Szybki start

### Wymagania wstępne

- **Środowisko uniksopodobne**: Linux lub macOS z powłoką Bash.
- **Podstawowe narzędzia**:
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

## Instalacja

1. **Sklonuj repozytorium**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Utwórz i aktywuj środowisko wirtualne** (opcjonalne, ale zalecane):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Zainstaluj zależności**:

    ```bash
    pip3 install payload_dumper
    ```

## Użycie

### Lokalnie

1. **Pobierz najnowsze obrazy OTA**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Przykłady:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Obsługiwane urządzenia w wybranych obrazach fabrycznych lub OTA z [Google Android Images](https://developers.google.com/android/images) lub [stron OTA Beta](https://developer.android.com/about/versions/17/download-ota).

2. **Wyodrębnij obrazy i zbierz `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Robi to automatycznie:
    - Wyodrębnia partycje payload.bin po jednej naraz (niskie zużycie pamięci)
    - Wykrywa i obsługuje obrazy **EROFS**, **ext4**, **sparse** oraz **boot/init_boot**
    - Buduje pełny, uporządkowany `.prop` z pliku build.prop każdej partycji
    - Zapisuje go w `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

Repozytorium zawiera w pełni zautomatyzowany potok CI (`.github/workflows/build.yml`):

- **Zaplanowane kompilacje**: uruchamiane w każdą niedzielę o północy UTC.
- **Ręczne uruchomienie**: wyzwalane przez `workflow_dispatch` z listą urządzeń oddzieloną spacjami lub `all`.
- **Kompilacje macierzowe**: każde urządzenie jest przetwarzane równolegle.
- **Zapobieganie duplikatom**: pomija pliki `.prop` już obecne w istniejących wydaniach.
- **Wersjonowane w repozytorium**: nowe pliki `.prop` są commitowane do `props/<codename>/`.
- **Zbiorcze wydania**: wszystkie nowe pliki `.prop` są publikowane pod jednym dziennym tagiem (`build-YYYYMMDD`).
- **Powiadomienia Telegram**: wysyła sformatowaną wiadomość z klikalnymi linkami do pobrania.

#### Wymagane sekrety

| Sekret | Opis |
|--------|------|
| `TELEGRAM_BOT_TOKEN` | Token Twojego bota Telegram uzyskany od [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID docelowego czatu (użytkownik, grupa lub kanał) |

## ✨ Najważniejsze funkcje

- **Automatyczne pozyskiwanie OTA**: pobiera najnowsze kompilacje bezpośrednio z oficjalnych źródeł Google.
- **Obsługa nowoczesnych systemów plików**: obsługuje obrazy EROFS, ext4, sparse oraz ramdyski boot/init_boot.
- **Generowanie pełnego `.prop`**: buduje jeden uporządkowany `.prop` na urządzenie z pliku build.prop każdej partycji (product, vendor, odm, system, system_ext, system_dlkm i inne).
- **Oszczędna pamięciowo ekstrakcja**: partycje payloadu są rozpakowywane po jednej, aby uniknąć OOM przy dużych OTA.
- **Wieloplatformowe zarządzanie pakietami**: `requirements.sh` obsługuje apt, pacman, dnf, yum, zypper, apk, xbps, brew i Termux.
- **Przechowywanie i dystrybucja**:
  - **W repozytorium**: każdy `.prop` jest commitowany do `props/<codename>/`, wersjonowany i możliwy do przeglądania.
  - **Jako zasoby wydań**: każdy `.prop` jest publikowany pod dziennym tagiem do bezpośredniego pobrania.
- **Integracja z GitHub Actions**:
  - **Zaplanowane przepływy pracy**: automatyzują aktualizacje, ekstrakcję i wydania według harmonogramu.
  - **Zapobieganie duplikatom wydań**: unika zbędnych wydań, sprawdzając zasoby istniejących wydań.
  - **Idempotentne wydania**: ponownie przesyła do istniejącego dziennego tagu wydania przy ponownym wyzwoleniu.
  - **Powiadomienia Telegram**: otrzymuj aktualne powiadomienia z klikalnymi linkami do pobrania.

## 📝 Wytyczne odpowiedzialnego użytkowania

Ten projekt jest udostępniany w celach edukacyjnych i eksperymentalnych. Choć został zaprojektowany z myślą o wydajności, kluczowe jest odpowiedzialne korzystanie z tego narzędzia.

- **Przegląd kodu**: dokładnie przejrzyj i zrozum kod przed wdrożeniem go w jakimkolwiek środowisku.
- **Najlepsze praktyki bezpieczeństwa**: przestrzegaj branżowych standardów bezpieczeństwa i zgodności prawnej.

Twórcy tego projektu nie ponoszą odpowiedzialności za jakiekolwiek niewłaściwe użycie ani szkody wynikające z jego stosowania.

## Podziękowania

Ten projekt jest forkiem **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** autorstwa **[@T3SL4](https://github.com/T3SL4)**, który zapoczątkował potok ekstrakcji z OTA do prop. Tutaj został przekształcony, aby przechowywać i dystrybuować pliki `.prop` zamiast instalowalnych modułów. Pełne uznanie za oryginalną pracę należy do jej autora.

## Kontakt

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licencja

**GNU GPL-3.0-or-later** - zobacz [LICENSE](LICENSE). Copyleft: każdy, kto dystrybuuje zmodyfikowaną wersję, musi udostępnić jej kod źródłowy na tych samych warunkach.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
