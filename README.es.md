[English](README.md) | [Português](README.pt.md) | **Español** | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Extrae y distribuye el `.prop` completo de Pixel directamente desde las imágenes OTA de Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Extrae y gestiona sin esfuerzo las propiedades del sistema a partir de las actualizaciones OTA de Pixel con esta robusta suite de automatización. Extrae el `.prop` completo y organizado de cada dispositivo directamente desde las imágenes OTA oficiales de Google y luego **almacena y distribuye esos archivos `.prop`** - tanto versionados en el repositorio como publicados como assets de release. Sin módulos instalables: solo las propiedades.

## 🚀 Inicio rápido

### Requisitos previos

- **Entorno tipo Unix**: Linux o macOS con Bash.
- **Utilidades esenciales**:
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

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Crea y activa un entorno virtual** (opcional pero recomendado):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Instala las dependencias**:

    ```bash
    pip3 install payload_dumper
    ```

## Uso

### Local

1. **Descarga las imágenes OTA más recientes**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Ejemplos:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Dispositivos compatibles en las imágenes de fábrica u OTA deseadas en [Google Android Images](https://developers.google.com/android/images) o en las [páginas de OTA Beta](https://developer.android.com/about/versions/17/download-ota).

2. **Extrae las imágenes y recopila el `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Esto automáticamente:
    - Extrae las particiones de payload.bin una por una (bajo consumo de memoria)
    - Detecta y maneja imágenes **EROFS**, **ext4**, **sparse** y **boot/init_boot**
    - Construye el `.prop` completo y organizado a partir del build.prop de cada partición
    - Lo guarda en `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

El repositorio incluye una canalización de CI totalmente automatizada (`.github/workflows/build.yml`):

- **Compilaciones programadas**: se ejecutan todos los domingos a medianoche UTC.
- **Ejecución manual**: actívala mediante `workflow_dispatch` con una lista de dispositivos separada por espacios o `all`.
- **Compilaciones en matriz**: cada dispositivo se procesa en paralelo.
- **Prevención de duplicados**: omite los `.prop` que ya están presentes en releases existentes.
- **Versionado en el repositorio**: los `.prop` nuevos se confirman en `props/<codename>/`.
- **Releases agregadas**: todos los `.prop` nuevos se publican bajo una única etiqueta diaria (`build-YYYYMMDD`).
- **Notificaciones de Telegram**: envía un mensaje con formato y enlaces de descarga en los que se puede hacer clic.

#### Secrets necesarios

| Secret | Descripción |
|--------|-------------|
| `TELEGRAM_BOT_TOKEN` | Tu token de bot de Telegram, obtenido de [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID del chat de destino (usuario, grupo o canal) |

## ✨ Características principales

- **Adquisición automática de OTA**: descarga las compilaciones más recientes directamente de las fuentes oficiales de Google.
- **Compatibilidad con sistemas de archivos modernos**: maneja imágenes EROFS, ext4, sparse y ramdisks boot/init_boot.
- **Generación del `.prop` completo**: construye un único `.prop` organizado por dispositivo a partir del build.prop de cada partición (product, vendor, odm, system, system_ext, system_dlkm y más).
- **Extracción eficiente en memoria**: las particiones del payload se vuelcan una por una para evitar OOM en OTAs grandes.
- **Gestión de paquetes multiplataforma**: `requirements.sh` admite apt, pacman, dnf, yum, zypper, apk, xbps, brew y Termux.
- **Almacenamiento y distribución**:
  - **En el repositorio**: cada `.prop` se confirma en `props/<codename>/`, versionado y navegable.
  - **Como assets de release**: cada `.prop` se publica bajo la etiqueta diaria para descarga directa.
- **Integración con GitHub Actions**:
  - **Workflows programados**: automatizan actualizaciones, extracción y releases según un calendario.
  - **Prevención de releases duplicadas**: evita releases redundantes comprobando los assets de releases existentes.
  - **Releases idempotentes**: vuelve a subir a una etiqueta de release diaria existente si se reactiva.
  - **Notificaciones de Telegram**: recibe actualizaciones oportunas con enlaces de descarga en los que se puede hacer clic.

## 📝 Pautas de uso responsable

Este proyecto se ofrece con fines educativos y experimentales. Aunque está diseñado para ser eficiente, es crucial usar esta herramienta de forma responsable.

- **Revisión del código**: revisa y comprende bien el código antes de desplegarlo en cualquier entorno.
- **Buenas prácticas de seguridad**: cumple con los estándares del sector en materia de seguridad y conformidad legal.

Los creadores de este proyecto no se hacen responsables de ningún uso indebido ni de los daños derivados de su uso.

## Agradecimientos

Este proyecto es un fork de **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** de **[@T3SL4](https://github.com/T3SL4)**, que fue pionero en el pipeline de extracción de OTA a prop. Aquí se reformula para almacenar y distribuir archivos `.prop` en lugar de módulos instalables. Todo el crédito del trabajo original es de su autor.

## Contacto

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licencia

**GNU GPL-3.0-or-later** - consulta [LICENSE](LICENSE). Copyleft: quien distribuya una versión modificada debe ofrecer su código fuente bajo los mismos términos.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
