[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | **Русский** | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Просматриваемый, автоматически обновляемый архив реальных данных `build.prop` для Pixel, прямо из официальных образов Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Версионированный архив **последних 4 сборок каждого канала** (stable, beta и canary) для каждого современного Pixel, извлечённый напрямую из официальных заводских и OTA-образов Google. Каждая запись - это **полный** `build.prop`, объединённый по **всем разделам** (system, system_ext, product, vendor, odm и образы `_dlkm`), и содержит **`ro.boot.vbmeta.digest`** (хеш verified boot). Всё хранится в репозитории, индексируется в машиночитаемом `index.json` и публикуется как ресурсы релиза. Инструменты не требуются.

## 📥 Получить данные

Три способа, настройка не требуется:

- **Просмотр репозитория** - откройте [`<codename>/`](.) и выберите файл. Именование по каналам:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - машиночитаемый манифест, сопоставляющий каждое устройство → канал → последнюю сборку, с `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` и `vbmeta_digest`. Идеально для автоматизации и инструментов.
- **Релизы** - загрузите весь корпус одним `.zip` (плюс `index.json`) из последнего [релиза](https://github.com/VictorGabriel7Dev/build.prop/releases) (с тегом `build-YYYYMMDD`).

Каждый `.prop` - это полный, организованный набор свойств для этого конкретного устройства и сборки - все разделы, плюс `ro.boot.vbmeta.digest`.

## 🗂️ Что внутри

- **Каждое современное устройство Pixel** (Pixel 6 и новее).
- **Три канала на устройство** - stable, beta и canary, последние сборки каждого (в зависимости от того, что Google фактически публикует; у некоторых совсем новых устройств пока есть лишь одна-две сборки на canary).
- **Полный `build.prop`** на каждую сборку (~300-390 свойств), объединённый из всех разделов.
- **`vbmeta.digest`** (хеш verified boot) хранится рядом со свойствами.

## 🔧 Собрать самостоятельно

Чтобы извлечь один `.prop` локально вместо его загрузки, вам понадобится Unix-подобное окружение (Linux или macOS с Bash) плюс `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` и Python ≥3.8 с `payload_dumper`. `requirements.sh` устанавливает зависимости в большинстве менеджеров пакетов (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Поддерживаемые устройства - это заводские и OTA-образы на [Google Android Images](https://developers.google.com/android/images) и [страницах Beta OTA](https://developer.android.com/about/versions/17/download-ota). Извлечение читает каждый раздел payload по одному (низкое потребление памяти) и обрабатывает образы EROFS, ext4, sparse и boot/init_boot.

## 🤖 Автоматизация

Архив автоматически поддерживается в актуальном состоянии: по мере публикации Google новых сборок они извлекаются (полностью, все разделы, с `vbmeta.digest`), новые `.prop` коммитятся в `<codename>/`, `index.json` обновляется, и выпускается датированный релиз (`build-YYYYMMDD`), чтобы наблюдатели получали уведомление о каждой волне.

Также доступен универсальный `.github/workflows/build.yml` по требованию (`workflow_dispatch`) как ручной резервный вариант для сборки последнего `.prop` устройства.

## Благодарности

Этот проект является форком **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** от **[@T3SL4](https://github.com/T3SL4)**, который впервые реализовал конвейер извлечения prop из OTA. Все заслуги за оригинальную работу принадлежат её автору.

## Контакты

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Лицензия

**GNU GPL-3.0-or-later** - см. [LICENSE](LICENSE). Copyleft: каждый, кто распространяет изменённую версию, обязан предоставить её исходный код на тех же условиях.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
