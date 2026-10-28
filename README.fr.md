[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | **Français** | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Extrayez et distribuez le `.prop` complet de Pixel directement depuis les images OTA de Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Extrayez et gérez sans effort les propriétés système à partir des mises à jour OTA de Pixel grâce à cette suite d'automatisation robuste. Elle extrait le `.prop` complet et organisé de chaque appareil directement depuis les images OTA officielles de Google, puis **stocke et distribue ces fichiers `.prop`** - à la fois versionnés dans le dépôt et publiés comme assets de release. Aucun module installable : seulement les propriétés.

## 🚀 Démarrage rapide

### Prérequis

- **Environnement de type Unix** : Linux ou macOS avec Bash.
- **Utilitaires essentiels** :
  - `zip`, `unzip`, `p7zip-full`
  - `dos2unix`, `aria2`, `curl`
  - `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`
  - `xxd`, `jq`
- **Python ≥3.8** :

    ```bash
    sudo apt-get update -y
    sudo apt-get install -y python3 python3-pip python3-venv jq xxd \
      p7zip-full e2fsprogs erofs-utils lz4 cpio dos2unix aria2 curl
    ```

## Installation

1. **Clonez le dépôt** :

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Créez et activez un environnement virtuel** (facultatif mais recommandé) :

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Installez les dépendances** :

    ```bash
    pip3 install payload_dumper
    ```

## Utilisation

### En local

1. **Récupérez les dernières images OTA** :

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Exemples :
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Appareils pris en charge dans les images d'usine ou OTA souhaitées sur [Google Android Images](https://developers.google.com/android/images) ou les [pages OTA Beta](https://developer.android.com/about/versions/17/download-ota).

2. **Extrayez les images et collectez le `.prop`** :

    ```bash
    ./extract_images.sh
    ```

    Cela réalise automatiquement :
    - Extrait les partitions de payload.bin une par une (faible empreinte mémoire)
    - Détecte et gère les images **EROFS**, **ext4**, **sparse** et **boot/init_boot**
    - Construit le `.prop` complet et organisé à partir du build.prop de chaque partition
    - L'enregistre dans `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

Le dépôt inclut un pipeline CI entièrement automatisé (`.github/workflows/build.yml`) :

- **Builds planifiés** : s'exécutent chaque dimanche à minuit UTC.
- **Déclenchement manuel** : lancez-le via `workflow_dispatch` avec une liste d'appareils séparée par des espaces ou `all`.
- **Builds en matrice** : chaque appareil est traité en parallèle.
- **Prévention des doublons** : ignore les `.prop` déjà présents dans les releases existantes.
- **Versionné dans le dépôt** : les nouveaux `.prop` sont commités dans `props/<codename>/`.
- **Releases agrégées** : tous les nouveaux `.prop` sont publiés sous une seule étiquette quotidienne (`build-YYYYMMDD`).
- **Notifications Telegram** : envoie un message formaté avec des liens de téléchargement cliquables.

#### Secrets requis

| Secret | Description |
|--------|-------------|
| `TELEGRAM_BOT_TOKEN` | Le jeton de votre bot Telegram obtenu auprès de [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID du chat cible (utilisateur, groupe ou canal) |

## ✨ Fonctionnalités clés

- **Acquisition OTA automatisée** : télécharge les derniers builds directement depuis les sources officielles de Google.
- **Prise en charge des systèmes de fichiers modernes** : gère les images EROFS, ext4, sparse et les ramdisks boot/init_boot.
- **Génération du `.prop` complet** : construit un seul `.prop` organisé par appareil à partir du build.prop de chaque partition (product, vendor, odm, system, system_ext, system_dlkm et plus).
- **Extraction économe en mémoire** : les partitions du payload sont extraites une par une pour éviter l'OOM sur les OTA volumineuses.
- **Gestion de paquets multiplateforme** : `requirements.sh` prend en charge apt, pacman, dnf, yum, zypper, apk, xbps, brew et Termux.
- **Stockage et distribution** :
  - **Dans le dépôt** : chaque `.prop` est commité dans `props/<codename>/`, versionné et navigable.
  - **Comme assets de release** : chaque `.prop` est publié sous l'étiquette quotidienne pour un téléchargement direct.
- **Intégration GitHub Actions** :
  - **Workflows planifiés** : automatisent les mises à jour, l'extraction et les releases selon un calendrier.
  - **Prévention des releases en double** : évite les releases redondantes en vérifiant les assets des releases existantes.
  - **Releases idempotentes** : réimporte dans une étiquette de release quotidienne existante en cas de nouveau déclenchement.
  - **Notifications Telegram** : recevez des mises à jour en temps voulu avec des liens de téléchargement cliquables.

## 📝 Consignes d'utilisation responsable

Ce projet est fourni à des fins éducatives et expérimentales. Bien qu'il soit conçu pour l'efficacité, il est crucial d'utiliser cet outil de manière responsable.

- **Revue du code** : examinez et comprenez soigneusement le code avant de le déployer dans un quelconque environnement.
- **Bonnes pratiques de sécurité** : respectez les normes du secteur en matière de sécurité et de conformité légale.

Les créateurs de ce projet déclinent toute responsabilité en cas d'utilisation abusive ou de dommages résultant de son utilisation.

## Remerciements

Ce projet est un fork de **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** de **[@T3SL4](https://github.com/T3SL4)**, qui a initié le pipeline d'extraction d'OTA vers prop. Il est ici remodelé pour stocker et distribuer des fichiers `.prop` au lieu de modules installables. Tout le mérite du travail original revient à son auteur.

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

**GNU GPL-3.0-or-later** - voir [LICENSE](LICENSE). Copyleft : quiconque distribue une version modifiée doit en proposer le code source aux mêmes conditions.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
