[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | **Italiano** | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Un archivio navigabile e aggiornato automaticamente di dati reali di `build.prop` di Pixel, direttamente dalle immagini ufficiali di Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Un archivio versionato degli **ultimi 4 build di ogni canale** (stable, beta e canary) di ogni Pixel recente, estratto direttamente dalle immagini ufficiali di fabbrica e OTA di Google. Ogni voce è il `build.prop` **completo**, unito da **tutte le partizioni** (system, system_ext, product, vendor, odm e le immagini `_dlkm`), e porta con sé il **`ro.boot.vbmeta.digest`** (hash del verified boot). Tutto è conservato nel repository, indicizzato in un `index.json` leggibile dalla macchina e pubblicato come asset di release. Nessuno strumento necessario.

## 📥 Ottieni i dati

Tre modi, senza alcuna configurazione:

- **Sfoglia il repository** - apri [`<codename>/`](.) e scegli un file. Nomenclatura per canale:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - un manifest leggibile dalla macchina che mappa ogni dispositivo → canale → build più recente, con `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` e `vbmeta_digest`. Ideale per automazione e strumenti.
- **Releases** - scarica l'intero corpus come un unico `.zip` (più l'`index.json`) dalla [release](https://github.com/VictorGabriel7Dev/build.prop/releases) più recente (con il tag `build-YYYYMMDD`).

Ogni `.prop` è l'insieme completo e organizzato delle proprietà per quel preciso dispositivo e build - tutte le partizioni, più il `ro.boot.vbmeta.digest`.

## 🗂️ Cosa contiene

- **Ogni dispositivo Pixel recente** (Pixel 6 e successivi).
- **Tre canali per dispositivo** - stable, beta e canary, i build più recenti di ciascuno (soggetto a ciò che Google pubblica effettivamente; alcuni dispositivi appena usciti hanno ancora solo uno o due build su canary).
- **`build.prop` completo** per build (~300-390 proprietà), unito da tutte le partizioni.
- **`vbmeta.digest`** (l'hash del verified boot) conservato accanto alle proprietà.

## 🔧 Compilalo da solo

Per estrarre un singolo `.prop` localmente invece di scaricarlo, ti serve un ambiente Unix-like (Linux o macOS con Bash) oltre a `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` e Python ≥3.8 con `payload_dumper`. `requirements.sh` installa le dipendenze sulla maggior parte dei gestori di pacchetti (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

I dispositivi supportati sono le immagini di fabbrica e OTA su [Google Android Images](https://developers.google.com/android/images) e sulle [pagine OTA Beta](https://developer.android.com/about/versions/17/download-ota). L'estrazione legge ogni partizione del payload una alla volta (basso consumo di memoria) e gestisce immagini EROFS, ext4, sparse e boot/init_boot.

## 🤖 Automazione

L'archivio resta aggiornato automaticamente: man mano che Google pubblica nuovi build, questi vengono estratti (completi, tutte le partizioni, con `vbmeta.digest`), i nuovi `.prop` vengono committati sotto `<codename>/`, l'`index.json` viene aggiornato e viene creata una release datata (`build-YYYYMMDD`) così che i watcher siano avvisati a ogni ondata.

È disponibile anche un `.github/workflows/build.yml` generico e su richiesta (`workflow_dispatch`) come fallback manuale per compilare il `.prop` più recente di un dispositivo.

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
