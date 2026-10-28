[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | **Italiano** | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Un archivio navigabile e aggiornato automaticamente di file `.prop` reali di Pixel, direttamente dalle immagini OTA di Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Un archivio versionato del `build.prop` completo di ogni Pixel, estratto direttamente dalle immagini OTA ufficiali di Google e mantenuto aggiornato automaticamente. Il `.prop` di ogni dispositivo è conservato nel repository e pubblicato come asset di release, pronto per essere sfogliato o scaricato senza bisogno di alcuno strumento.

## 📥 Ottieni un `.prop`

Due modi, senza alcuna configurazione:

- **Sfoglia il repository**: apri [`props/<codename>/`](props/) e scegli `<codename>_<build_id>.prop`.
- **Scarica dalle Releases**: prendi il file dalla [release](https://github.com/VictorGabriel7Dev/build.prop/releases) più recente (con il tag `build-YYYYMMDD`).

Ogni `.prop` è l'insieme completo e organizzato delle proprietà di build per quel preciso dispositivo e build (product, vendor, odm, system, system_ext, system_dlkm e altro).

## 🔧 Compilalo da solo

Per estrarre un `.prop` localmente invece di scaricarlo, ti serve un ambiente Unix-like (Linux o macOS con Bash) oltre a `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` e Python ≥3.8 con `payload_dumper`. `requirements.sh` installa le dipendenze sulla maggior parte dei gestori di pacchetti (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

I dispositivi supportati sono le immagini di fabbrica e OTA su [Google Android Images](https://developers.google.com/android/images) e sulle [pagine OTA Beta](https://developer.android.com/about/versions/17/download-ota). L'estrazione legge ogni partizione del payload una alla volta (basso consumo di memoria) e gestisce immagini EROFS, ext4, sparse e boot/init_boot.

## 🤖 Automazione

Una pipeline di GitHub Actions (`.github/workflows/build.yml`) mantiene l'archivio aggiornato:

- Viene eseguita settimanalmente, e su richiesta tramite `workflow_dispatch` con un elenco di dispositivi separati da spazi oppure `all`; ogni dispositivo viene compilato in parallelo.
- Estrae il `.prop`, committa quelli nuovi in `props/<codename>/` e li pubblica come asset sotto un unico tag giornaliero (`build-YYYYMMDD`).
- Salta i file `.prop` già pubblicati e notifica Telegram con link di download cliccabili.

I fork che eseguono la pipeline hanno bisogno di due secret: `TELEGRAM_BOT_TOKEN` (da [@BotFather](https://t.me/BotFather)) e `TELEGRAM_CHAT_ID`.

## Ringraziamenti

Questo progetto è un fork di **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** di **[@T3SL4](https://github.com/T3SL4)**, che ha dato il via alla pipeline di estrazione da OTA a prop. Tutto il merito del lavoro originale va al suo autore.

## Contatto

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licenza

**GNU GPL-3.0-or-later** - vedi [LICENSE](LICENSE). Copyleft: chiunque distribuisca una versione modificata deve offrirne il codice sorgente agli stessi termini.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
