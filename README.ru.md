[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | **Русский** | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Просматриваемый, автоматически обновляемый архив реальных файлов `.prop` для Pixel, напрямую из OTA-образов Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Версионированный архив полного `build.prop` каждого Pixel, извлечённого напрямую из официальных OTA-образов Google и автоматически поддерживаемого в актуальном состоянии. Файл `.prop` каждого устройства хранится в репозитории и публикуется как ресурс релиза, готовый к просмотру или загрузке без каких-либо инструментов.

## 📥 Получить `.prop`

Два способа, настройка не требуется:

- **Просмотр репозитория**: откройте [`props/<codename>/`](props/) и выберите `<codename>_<build_id>.prop`.
- **Загрузка из релизов**: возьмите файл из последнего [релиза](https://github.com/VictorGabriel7Dev/build.prop/releases) (с тегом `build-YYYYMMDD`).

Каждый `.prop` - это полный, организованный набор свойств сборки для этого конкретного устройства и сборки (product, vendor, odm, system, system_ext, system_dlkm и другие).

## 🔧 Собрать самостоятельно

Чтобы извлечь `.prop` локально вместо его загрузки, вам понадобится Unix-подобное окружение (Linux или macOS с Bash) плюс `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` и Python ≥3.8 с `payload_dumper`. `requirements.sh` устанавливает зависимости в большинстве менеджеров пакетов (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
pip3 install payload_dumper
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Поддерживаемые устройства - это заводские и OTA-образы на [Google Android Images](https://developers.google.com/android/images) и [страницах Beta OTA](https://developer.android.com/about/versions/17/download-ota). Извлечение читает каждый раздел payload по одному (низкое потребление памяти) и обрабатывает образы EROFS, ext4, sparse и boot/init_boot.

## 🤖 Автоматизация

Конвейер GitHub Actions (`.github/workflows/build.yml`) поддерживает архив в актуальном состоянии:

- Запускается еженедельно, а также по требованию через `workflow_dispatch` со списком устройств через пробел или `all`; каждое устройство собирается параллельно.
- Извлекает `.prop`, коммитит новые файлы в `props/<codename>/` и публикует их как ресурсы под единым ежедневным тегом (`build-YYYYMMDD`).
- Пропускает уже выпущенные файлы `.prop` и уведомляет Telegram с кликабельными ссылками для загрузки.

Форкам, запускающим конвейер, нужны два секрета: `TELEGRAM_BOT_TOKEN` (от [@BotFather](https://t.me/BotFather)) и `TELEGRAM_CHAT_ID`.

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

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
