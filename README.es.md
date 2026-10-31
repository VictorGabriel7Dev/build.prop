[English](README.md) | [Português](README.pt.md) | **Español** | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Un archivo navegable y actualizado automáticamente de datos reales de `build.prop` de Pixel, directo desde las imágenes oficiales de Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Un archivo versionado de los **últimos 4 builds de cada canal** (stable, beta y canary) de cada Pixel reciente, extraído directamente de las imágenes oficiales de fábrica y OTA de Google. Cada entrada es el `build.prop` **completo**, fusionado desde **todas las particiones** (system, system_ext, product, vendor, odm y las imágenes `_dlkm`), y lleva el **`ro.boot.vbmeta.digest`** (hash del verified boot). Todo se guarda en el repositorio, se indexa en un `index.json` legible por máquina y se publica como assets de release. No se necesita ninguna herramienta.

## 📥 Consigue los datos

Tres maneras, sin configuración necesaria:

- **Navega por el repositorio** - abre [`<codename>/`](.) y elige un archivo. Nomenclatura por canal:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - un manifiesto legible por máquina que mapea cada dispositivo → canal → build más reciente, con `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` y `vbmeta_digest`. Ideal para automatización y herramientas.
- **Releases** - cada `.prop` se adjunta individualmente (más el `index.json`) a la [release](https://github.com/VictorGabriel7Dev/build.prop/releases) más reciente (con la etiqueta `build-YYYYMMDD`).

Cada `.prop` es el conjunto completo y organizado de propiedades de ese dispositivo y build exactos - todas las particiones, más el `ro.boot.vbmeta.digest`.

## 🗂️ Qué contiene

- **Todo dispositivo Pixel reciente** (Pixel 6 y posteriores).
- **Tres canales por dispositivo** - stable, beta y canary, los builds más recientes de cada uno (sujeto a lo que Google publica realmente; algunos dispositivos recién lanzados aún tienen solo uno o dos builds en canary).
- **`build.prop` completo** por build (~300-390 propiedades), fusionado desde todas las particiones.
- **`vbmeta.digest`** (el hash del verified boot) guardado junto a las propiedades.

## 🔧 Compílalo tú mismo

Para extraer un solo `.prop` localmente en vez de descargarlo, necesitas un entorno tipo Unix (Linux o macOS con Bash) además de `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` y Python ≥3.8 con `payload_dumper`. El `requirements.sh` instala las dependencias en la mayoría de los gestores de paquetes (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Los dispositivos compatibles son las imágenes de fábrica y OTA en [Google Android Images](https://developers.google.com/android/images) y en las [páginas de OTA Beta](https://developer.android.com/about/versions/17/download-ota). La extracción lee cada partición del payload de una en una (bajo consumo de memoria) y maneja imágenes EROFS, ext4, sparse y boot/init_boot.

## 🤖 Automatización

El archivo se mantiene al día de forma automática: a medida que Google publica nuevos builds, se extraen (completos, todas las particiones, con `vbmeta.digest`), los nuevos `.prop` se commitean en `<codename>/`, el `index.json` se actualiza y se crea una release con fecha (`build-YYYYMMDD`) para que los watchers sean notificados en cada oleada.

También hay disponible un `.github/workflows/build.yml` genérico y bajo demanda (`workflow_dispatch`) como alternativa manual para compilar el `.prop` más reciente de un dispositivo.

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
