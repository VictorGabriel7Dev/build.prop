[English](README.md) | [Português](README.pt.md) | **Español** | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Un archivo navegable y actualizado automáticamente de archivos `.prop` reales de Pixel, directo desde las imágenes OTA de Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Un archivo versionado del `build.prop` completo de cada Pixel, extraído directamente de las imágenes OTA oficiales de Google y mantenido al día de forma automática. El `.prop` de cada dispositivo se guarda en el repositorio y se publica como asset de release, listo para navegar o descargar sin necesidad de ninguna herramienta.

## 📥 Consigue un `.prop`

Dos maneras, sin configuración necesaria:

- **Navega por el repositorio**: abre [`<codename>/`](.) y elige `<codename>_<build_id>.prop`.
- **Descarga desde Releases**: toma el archivo de la [release](https://github.com/VictorGabriel7Dev/build.prop/releases) más reciente (con la etiqueta `build-YYYYMMDD`).

Cada `.prop` es el conjunto completo y organizado de propiedades de build de ese dispositivo y build exactos (product, vendor, odm, system, system_ext, system_dlkm y más).

## 🔧 Compílalo tú mismo

Para extraer un `.prop` localmente en vez de descargarlo, necesitas un entorno tipo Unix (Linux o macOS con Bash) además de `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` y Python ≥3.8 con `payload_dumper`. El `requirements.sh` instala las dependencias en la mayoría de los gestores de paquetes (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Los dispositivos compatibles son las imágenes de fábrica y OTA en [Google Android Images](https://developers.google.com/android/images) y en las [páginas de OTA Beta](https://developer.android.com/about/versions/17/download-ota). La extracción lee cada partición del payload de una en una (bajo consumo de memoria) y maneja imágenes EROFS, ext4, sparse y boot/init_boot.

## 🤖 Automatización

Un pipeline de GitHub Actions (`.github/workflows/build.yml`) mantiene el archivo al día:

- Se ejecuta semanalmente, y bajo demanda vía `workflow_dispatch` con una lista de dispositivos separada por espacios o `all`; cada dispositivo se compila en paralelo.
- Extrae el `.prop`, hace commit de los nuevos en `<codename>/` y los publica como assets bajo una única etiqueta diaria (`build-YYYYMMDD`).
- Omite los archivos `.prop` ya publicados y notifica a Telegram con enlaces de descarga clicables.

Los forks que ejecutan el pipeline necesitan dos secrets: `TELEGRAM_BOT_TOKEN` (de [@BotFather](https://t.me/BotFather)) y `TELEGRAM_CHAT_ID`.

## Agradecimientos

Este proyecto es un fork de **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** de **[@T3SL4](https://github.com/T3SL4)**, que fue pionero en el pipeline de extracción de OTA a prop. Todo el crédito por el trabajo original es de su autor.

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

**GNU GPL-3.0-or-later** - consulta [LICENSE](LICENSE). Copyleft: cualquiera que distribuya una versión modificada debe ofrecer su código fuente bajo los mismos términos.

---

`android` `pixel` `build-prop` `ota` `factory-image` `system-properties` `system-properties` `automation`
