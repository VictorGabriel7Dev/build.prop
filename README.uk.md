[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md) | **Українська**

# Pixel Prop Builder

*Зручний для перегляду, автоматично оновлюваний архів реальних даних `build.prop` пристроїв Pixel, напряму з офіційних образів Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-22-orange.svg)](README.md)

Версійований архів **останніх 4 складань кожного каналу** (stable, beta та canary) для кожного сучасного Pixel, витягнутих напряму з офіційних заводських (factory) та OTA образів Google. Кожен запис - це **повний** `build.prop`, об'єднаний з **усіх розділів** (system, system_ext, product, vendor, odm та образів `_dlkm`), і містить **`ro.boot.vbmeta.digest`** (хеш перевіреного завантаження). Усе зберігається в репозиторії, індексується у машиночитаному `index.json` і публікується як ресурси релізів. Жодних інструментів не потрібно.

## 📥 Отримати дані

Три способи, без жодного налаштування:

- **Перегляд репозиторію** - відкрийте [`<codename>/`](.) і виберіть файл. Іменування за каналом:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - машиночитаний маніфест, що зіставляє кожен пристрій → канал → останнє складання, з полями `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` та `vbmeta_digest`. Ідеально для автоматизації та інструментів.
- **Релізи** - кожен `.prop` додається окремо (разом з `index.json`) до останнього [релізу](https://github.com/VictorGabriel7Dev/build.prop/releases) (з тегом `build-YYYYMMDD`).

Кожен `.prop` - це повний, упорядкований набір властивостей для цього конкретного пристрою та складання - усі розділи, плюс `ro.boot.vbmeta.digest`.

## 🗂️ Що всередині

- **Кожен сучасний пристрій Pixel** (Pixel 6 і новіші).
- **Три канали на пристрій** - stable, beta та canary, останні складання кожного (залежно від того, що Google фактично публікує; деякі зовсім нові пристрої мають лише одне-два складання на canary).
- **Повний `build.prop`** на складання (~300-390 властивостей), об'єднаний з усіх розділів.
- **`vbmeta.digest`** (хеш перевіреного завантаження) зберігається поряд із властивостями.

## 🔧 Зібрати самостійно

Щоб витягти один `.prop` локально замість завантаження, потрібне Unix-подібне середовище (Linux або macOS з Bash), а також `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` і Python ≥3.8 з `payload_dumper`. `requirements.sh` встановлює залежності для більшості пакетних менеджерів (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # напр. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Підтримувані пристрої - це заводські та OTA образи на [Google Android Images](https://developers.google.com/android/images) та [сторінках Beta OTA](https://developer.android.com/about/versions/17/download-ota). Витягування читає кожен розділ payload по черзі (низьке споживання пам'яті) та обробляє образи EROFS, ext4, sparse і boot/init_boot.

## 🤖 Автоматизація

Архів оновлюється автоматично: щойно Google публікує нові складання, вони витягуються (повністю, усі розділи, з `vbmeta.digest`), нові `.prop` комітяться в `<codename>/`, `index.json` оновлюється, і створюється датований реліз (`build-YYYYMMDD`), щоб спостерігачі отримували сповіщення про кожну хвилю.

Також доступний універсальний `.github/workflows/build.yml` на вимогу (`workflow_dispatch`) як ручний запасний варіант для збирання останнього `.prop` пристрою.

## Подяки

Цей проєкт є форком **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** від **[@T3SL4](https://github.com/T3SL4)**, який започаткував конвеєр витягування OTA-to-prop. Уся заслуга за оригінальну роботу належить її автору.

## Контакти

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Ліцензія

**GNU GPL-3.0-or-later** - див. [LICENSE](LICENSE). Copyleft: кожен, хто розповсюджує змінену версію, повинен надати її вихідний код на тих самих умовах.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
