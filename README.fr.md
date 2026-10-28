[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | **Français** | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Une archive navigable et mise à jour automatiquement de fichiers `.prop` réels de Pixel, directement issus des images OTA de Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Une archive versionnée du `build.prop` complet de chaque Pixel, extrait directement des images OTA officielles de Google et maintenu à jour automatiquement. Le `.prop` de chaque appareil est stocké dans le dépôt et publié comme asset de release, prêt à être parcouru ou téléchargé sans aucun outil requis.

## 📥 Obtenir un `.prop`

Deux façons, sans aucune configuration :

- **Parcourir le dépôt** : ouvrez [`<codename>/`](.) et choisissez `<codename>_<build_id>.prop`.
- **Télécharger depuis les Releases** : récupérez le fichier dans la [release](https://github.com/VictorGabriel7Dev/build.prop/releases) la plus récente (avec le tag `build-YYYYMMDD`).

Chaque `.prop` est l'ensemble complet et organisé des propriétés de build pour cet appareil et ce build précis (product, vendor, odm, system, system_ext, system_dlkm et plus).

## 🔧 Compilez-le vous-même

Pour extraire un `.prop` localement au lieu de le télécharger, il vous faut un environnement de type Unix (Linux ou macOS avec Bash) ainsi que `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, et Python ≥3.8 avec `payload_dumper`. `requirements.sh` installe les dépendances sur la plupart des gestionnaires de paquets (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Les appareils pris en charge sont les images d'usine et OTA sur [Google Android Images](https://developers.google.com/android/images) et les [pages OTA Beta](https://developer.android.com/about/versions/17/download-ota). L'extraction lit chaque partition du payload une par une (faible consommation de mémoire) et gère les images EROFS, ext4, sparse et boot/init_boot.

## 🤖 Automatisation

Un pipeline GitHub Actions (`.github/workflows/build.yml`) maintient l'archive à jour :

- S'exécute chaque semaine, et à la demande via `workflow_dispatch` avec une liste d'appareils séparés par des espaces ou `all` ; chaque appareil est compilé en parallèle.
- Extrait le `.prop`, committe les nouveaux dans `<codename>/` et les publie comme assets sous un unique tag quotidien (`build-YYYYMMDD`).
- Ignore les fichiers `.prop` déjà publiés et notifie Telegram avec des liens de téléchargement cliquables.

Les forks qui exécutent le pipeline ont besoin de deux secrets : `TELEGRAM_BOT_TOKEN` (depuis [@BotFather](https://t.me/BotFather)) et `TELEGRAM_CHAT_ID`.

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

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
