[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | **Русский** | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Извлекайте и распространяйте полный `.prop` Pixel напрямую из OTA-образов Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Легко извлекайте и управляйте системными свойствами из OTA-обновлений Pixel с помощью этого надёжного набора средств автоматизации. Он извлекает полный, упорядоченный `.prop` каждого устройства напрямую из официальных OTA-образов Google, а затем **хранит и распространяет эти файлы `.prop`** - как версионируемые в репозитории, так и публикуемые в виде ассетов релиза. Никаких устанавливаемых модулей: только свойства.

## 🚀 Быстрый старт

### Предварительные требования

- **Unix-подобная среда**: Linux или macOS с Bash.
- **Основные утилиты**:
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

## Установка

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Создайте и активируйте виртуальное окружение** (необязательно, но рекомендуется):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Установите зависимости**:

    ```bash
    pip3 install payload_dumper
    ```

## Использование

### Локально

1. **Загрузите последние OTA-образы**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Примеры:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Поддерживаемые устройства в нужных заводских или OTA-образах на [Google Android Images](https://developers.google.com/android/images) или на [страницах бета-OTA](https://developer.android.com/about/versions/17/download-ota).

2. **Извлеките образы и соберите `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Это автоматически:
    - Извлекает разделы payload.bin по одному (низкое потребление памяти)
    - Обнаруживает и обрабатывает образы **EROFS**, **ext4**, **sparse** и **boot/init_boot**
    - Собирает полный, упорядоченный `.prop` из build.prop каждого раздела
    - Сохраняет его в `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

Репозиторий включает полностью автоматизированный CI-конвейер (`.github/workflows/build.yml`):

- **Запланированные сборки**: выполняются каждое воскресенье в полночь по UTC.
- **Ручной запуск**: запускается через `workflow_dispatch` со списком устройств через пробел или `all`.
- **Матричные сборки**: каждое устройство обрабатывается параллельно.
- **Предотвращение дубликатов**: пропускает `.prop`, уже присутствующие в существующих релизах.
- **Версионирование в репозитории**: новые `.prop` коммитятся в `props/<codename>/`.
- **Сводные релизы**: все новые `.prop` публикуются под одним общим ежедневным тегом (`build-YYYYMMDD`).
- **Уведомления в Telegram**: отправляет отформатированное сообщение с кликабельными ссылками для загрузки.

#### Необходимые секреты

| Секрет | Описание |
|--------|----------|
| `TELEGRAM_BOT_TOKEN` | Токен вашего Telegram-бота, полученный у [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID целевого чата (пользователь, группа или канал) |

## ✨ Ключевые возможности

- **Автоматическое получение OTA**: загружает последние сборки напрямую из официальных источников Google.
- **Поддержка современных файловых систем**: обрабатывает образы EROFS, ext4, sparse и ramdisk-образы boot/init_boot.
- **Генерация полного `.prop`**: собирает единый упорядоченный `.prop` для каждого устройства из build.prop каждого раздела (product, vendor, odm, system, system_ext, system_dlkm и других).
- **Экономичное по памяти извлечение**: разделы payload распаковываются по одному, чтобы избежать OOM на крупных OTA.
- **Кроссплатформенное управление пакетами**: `requirements.sh` поддерживает apt, pacman, dnf, yum, zypper, apk, xbps, brew и Termux.
- **Хранение и распространение**:
  - **В репозитории**: каждый `.prop` коммитится в `props/<codename>/`, версионируется и доступен для просмотра.
  - **Как ассеты релиза**: каждый `.prop` публикуется под ежедневным тегом для прямой загрузки.
- **Интеграция с GitHub Actions**:
  - **Запланированные рабочие процессы**: автоматизируют обновления, извлечение и релизы по расписанию.
  - **Предотвращение дублирующих релизов**: избегает избыточных релизов, проверяя ассеты существующих релизов.
  - **Идемпотентные релизы**: повторно загружает в существующий ежедневный тег релиза при повторном запуске.
  - **Уведомления в Telegram**: получайте своевременные обновления с кликабельными ссылками для загрузки.

## 📝 Рекомендации по ответственному использованию

Этот проект предоставляется в образовательных и экспериментальных целях. Хотя он разработан с упором на эффективность, крайне важно использовать этот инструмент ответственно.

- **Проверка кода**: тщательно изучите и поймите код, прежде чем развёртывать его в какой-либо среде.
- **Лучшие практики безопасности**: придерживайтесь отраслевых стандартов безопасности и правового соответствия.

Создатели этого проекта не несут ответственности за любое неправомерное использование или ущерб, возникший в результате его применения.

## Благодарности

Этот проект - форк **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** от **[@T3SL4](https://github.com/T3SL4)**, который создал конвейер извлечения из OTA в prop. Здесь он переработан для хранения и распространения файлов `.prop` вместо устанавливаемых модулей. Вся заслуга за оригинальную работу принадлежит её автору.

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

**GNU GPL-3.0-or-later** - см. [LICENSE](LICENSE). Копилефт: тот, кто распространяет изменённую версию, должен предоставить её исходный код на тех же условиях.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
