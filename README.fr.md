[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | **Français** | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Une archive navigable et mise à jour automatiquement de données réelles de `build.prop` de Pixel, directement issues des images officielles de Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Une archive versionnée des **4 derniers builds de chaque canal** (stable, beta et canary) de chaque Pixel récent, extraite directement des images officielles d'usine et OTA de Google. Chaque entrée est le `build.prop` **complet**, fusionné depuis **toutes les partitions** (system, system_ext, product, vendor, odm et les images `_dlkm`), et porte le **`ro.boot.vbmeta.digest`** (hash du verified boot). Tout est stocké dans le dépôt, indexé dans un `index.json` lisible par machine et publié comme assets de release. Aucun outil requis.

## 📥 Obtenir les données

Trois façons, sans aucune configuration :

- **Parcourir le dépôt** - ouvrez [`<codename>/`](.) et choisissez un fichier. Nommage par canal :
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - un manifeste lisible par machine qui associe chaque appareil → canal → build le plus récent, avec `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` et `vbmeta_digest`. Idéal pour l'automatisation et l'outillage.
- **Releases** - chaque `.prop` est joint individuellement (plus l'`index.json`) à la [release](https://github.com/VictorGabriel7Dev/build.prop/releases) la plus récente (avec le tag `build-YYYYMMDD`).

Chaque `.prop` est l'ensemble complet et organisé des propriétés pour cet appareil et ce build précis - toutes les partitions, plus le `ro.boot.vbmeta.digest`.

## 🗂️ Ce qu'elle contient

- **Chaque appareil Pixel récent** (Pixel 6 et plus récents).
- **Trois canaux par appareil** - stable, beta et canary, les builds les plus récents de chacun (selon ce que Google publie réellement ; certains appareils tout nouveaux n'ont encore qu'un build ou deux sur canary).
- **`build.prop` complet** par build (~300-390 propriétés), fusionné depuis toutes les partitions.
- **`vbmeta.digest`** (le hash du verified boot) stocké aux côtés des propriétés.

## 🔧 Compilez-le vous-même

Pour extraire un seul `.prop` localement au lieu de le télécharger, il vous faut un environnement de type Unix (Linux ou macOS avec Bash) ainsi que `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, et Python ≥3.8 avec `payload_dumper`. `requirements.sh` installe les dépendances sur la plupart des gestionnaires de paquets (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Les appareils pris en charge sont les images d'usine et OTA sur [Google Android Images](https://developers.google.com/android/images) et les [pages OTA Beta](https://developer.android.com/about/versions/17/download-ota). L'extraction lit chaque partition du payload une par une (faible consommation de mémoire) et gère les images EROFS, ext4, sparse et boot/init_boot.

## 🤖 Automatisation

L'archive reste à jour automatiquement : à mesure que Google publie de nouveaux builds, ils sont extraits (complets, toutes les partitions, avec `vbmeta.digest`), les nouveaux `.prop` sont committés sous `<codename>/`, l'`index.json` est actualisé et une release datée (`build-YYYYMMDD`) est créée afin que les watchers soient notifiés à chaque vague.

Un `.github/workflows/build.yml` générique et à la demande est également disponible (`workflow_dispatch`) comme solution de repli manuelle pour compiler le `.prop` le plus récent d'un appareil.

## Remerciements

Ce projet est un fork de **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** par **[@T3SL4](https://github.com/T3SL4)**, qui a été le pionnier du pipeline d'extraction d'OTA vers prop. Tout le crédit du travail original revient à son auteur.

## Contact

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licence

**GNU GPL-3.0-or-later** - voir [LICENSE](LICENSE). Copyleft : quiconque distribue une version modifiée doit en proposer le code source selon les mêmes termes.

---

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
