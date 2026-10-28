[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | **Italiano** | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Estrai e distribuisci il `.prop` completo di Pixel direttamente dalle immagini OTA di Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Estrai e gestisci senza sforzo le proprietà di sistema dagli aggiornamenti OTA di Pixel con questa robusta suite di automazione. Estrae il `.prop` completo e organizzato di ogni dispositivo direttamente dalle immagini OTA ufficiali di Google e poi **archivia e distribuisce quei file `.prop`** - sia versionati nel repository sia pubblicati come asset di release. Nessun modulo installabile: solo le proprietà.

## 🚀 Avvio rapido

### Prerequisiti

- **Ambiente Unix-like**: Linux o macOS con Bash.
- **Utilità essenziali**:
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

## Installazione

1. **Clona il repository**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Crea e attiva un ambiente virtuale** (opzionale ma consigliato):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Installa le dipendenze**:

    ```bash
    pip3 install payload_dumper
    ```

## Utilizzo

### In locale

1. **Scarica le immagini OTA più recenti**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Esempi:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Dispositivi supportati nelle immagini di fabbrica o OTA desiderate su [Google Android Images](https://developers.google.com/android/images) o sulle [pagine OTA Beta](https://developer.android.com/about/versions/17/download-ota).

2. **Estrai le immagini e raccogli il `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Questo automaticamente:
    - Estrae le partizioni di payload.bin una alla volta (basso consumo di memoria)
    - Rileva e gestisce immagini **EROFS**, **ext4**, **sparse** e **boot/init_boot**
    - Costruisce il `.prop` completo e organizzato dal build.prop di ogni partizione
    - Lo salva in `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

Il repository include una pipeline CI completamente automatizzata (`.github/workflows/build.yml`):

- **Build pianificate**: vengono eseguite ogni domenica a mezzanotte UTC.
- **Avvio manuale**: attivala tramite `workflow_dispatch` con un elenco di dispositivi separato da spazi o `all`.
- **Build a matrice**: ogni dispositivo viene elaborato in parallelo.
- **Prevenzione dei duplicati**: salta i `.prop` già presenti nelle release esistenti.
- **Versionato nel repository**: i nuovi `.prop` vengono committati in `props/<codename>/`.
- **Release aggregate**: tutti i nuovi `.prop` vengono pubblicati sotto un'unica tag giornaliera (`build-YYYYMMDD`).
- **Notifiche Telegram**: invia un messaggio formattato con link di download cliccabili.

#### Secret necessari

| Secret | Descrizione |
|--------|-------------|
| `TELEGRAM_BOT_TOKEN` | Il token del tuo bot Telegram, ottenuto da [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID della chat di destinazione (utente, gruppo o canale) |

## ✨ Caratteristiche principali

- **Acquisizione OTA automatica**: scarica le build più recenti direttamente dalle fonti ufficiali di Google.
- **Supporto ai filesystem moderni**: gestisce immagini EROFS, ext4, sparse e ramdisk boot/init_boot.
- **Generazione del `.prop` completo**: costruisce un unico `.prop` organizzato per dispositivo dal build.prop di ogni partizione (product, vendor, odm, system, system_ext, system_dlkm e altro).
- **Estrazione efficiente in memoria**: le partizioni del payload vengono estratte una alla volta per evitare l'OOM sulle OTA di grandi dimensioni.
- **Gestione pacchetti multipiattaforma**: `requirements.sh` supporta apt, pacman, dnf, yum, zypper, apk, xbps, brew e Termux.
- **Archiviazione e distribuzione**:
  - **Nel repository**: ogni `.prop` viene committato in `props/<codename>/`, versionato e navigabile.
  - **Come asset di release**: ogni `.prop` viene pubblicato sotto la tag giornaliera per il download diretto.
- **Integrazione con GitHub Actions**:
  - **Workflow pianificati**: automatizzano aggiornamenti, estrazione e release secondo una pianificazione.
  - **Prevenzione delle release duplicate**: evita release ridondanti controllando gli asset delle release esistenti.
  - **Release idempotenti**: ricarica su una tag di release giornaliera esistente se riattivata.
  - **Notifiche Telegram**: ricevi aggiornamenti tempestivi con link di download cliccabili.

## 📝 Linee guida per un uso responsabile

Questo progetto è fornito a scopo didattico e sperimentale. Sebbene sia progettato per l'efficienza, è fondamentale usare questo strumento in modo responsabile.

- **Revisione del codice**: esamina e comprendi bene il codice prima di distribuirlo in qualsiasi ambiente.
- **Buone pratiche di sicurezza**: attieniti agli standard del settore per la sicurezza e la conformità legale.

I creatori di questo progetto non sono responsabili per eventuali usi impropri o danni derivanti dal suo utilizzo.

## Ringraziamenti

Questo progetto è un fork di **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** di **[@T3SL4](https://github.com/T3SL4)**, che ha dato origine alla pipeline di estrazione da OTA a prop. Qui è rimodellato per archiviare e distribuire file `.prop` invece di moduli installabili. Tutto il merito del lavoro originale va al suo autore.

## Contatti

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licenza

**GNU GPL-3.0-or-later** - vedi [LICENSE](LICENSE). Copyleft: chi distribuisce una versione modificata deve offrirne il codice sorgente agli stessi termini.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
