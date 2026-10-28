[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | **Čeština** | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Extrahujte a distribuujte kompletní `.prop` Pixelu přímo z OTA obrazů Googlu*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Bez námahy extrahujte a spravujte systémové vlastnosti z OTA aktualizací Pixelu pomocí této robustní automatizační sady. Extrahuje kompletní, uspořádaný `.prop` každého zařízení přímo z oficiálních OTA obrazů Googlu a poté **tyto soubory `.prop` ukládá a distribuuje** - jak verzované v repozitáři, tak publikované jako aktiva vydání. Žádné instalovatelné moduly: jen vlastnosti.

## 🚀 Rychlý start

### Předpoklady

- **Prostředí typu Unix**: Linux nebo macOS s Bash.
- **Základní nástroje**:
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

## Instalace

1. **Naklonujte repozitář**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Vytvořte a aktivujte virtuální prostředí** (volitelné, ale doporučené):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Nainstalujte závislosti**:

    ```bash
    pip3 install payload_dumper
    ```

## Použití

### Lokálně

1. **Stáhněte nejnovější OTA obrazy**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Příklady:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Podporovaná zařízení v požadovaných továrních nebo OTA obrazech z [Google Android Images](https://developers.google.com/android/images) nebo [stránek Beta OTA](https://developer.android.com/about/versions/17/download-ota).

2. **Extrahujte obrazy a shromážděte `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Toto automaticky:
    - Extrahuje oddíly payload.bin po jednom (nízká paměťová náročnost)
    - Rozpozná a zpracuje obrazy **EROFS**, **ext4**, **sparse** a **boot/init_boot**
    - Sestaví kompletní, uspořádaný `.prop` z build.prop každého oddílu
    - Uloží jej do `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

Repozitář obsahuje plně automatizovanou CI pipeline (`.github/workflows/build.yml`):

- **Naplánované buildy**: běží každou neděli o půlnoci UTC.
- **Ruční spuštění**: spusťte přes `workflow_dispatch` se seznamem zařízení odděleným mezerami nebo `all`.
- **Maticové buildy**: každé zařízení se zpracovává paralelně.
- **Prevence duplicit**: přeskakuje soubory `.prop`, které už jsou v existujících vydáních.
- **Verzováno v repozitáři**: nové soubory `.prop` se commitují do `props/<codename>/`.
- **Agregovaná vydání**: všechny nové soubory `.prop` se publikují pod jedním denním tagem (`build-YYYYMMDD`).
- **Oznámení Telegramu**: odešle formátovanou zprávu s klikacími odkazy ke stažení.

#### Potřebné secrets

| Secret | Popis |
|--------|-------|
| `TELEGRAM_BOT_TOKEN` | Token vašeho Telegram bota od [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID cílového chatu (uživatel, skupina nebo kanál) |

## ✨ Klíčové funkce

- **Automatizované získávání OTA**: stahuje nejnovější buildy přímo z oficiálních zdrojů Googlu.
- **Podpora moderních souborových systémů**: zpracovává obrazy EROFS, ext4, sparse a ramdisky boot/init_boot.
- **Generování kompletního `.prop`**: sestaví jeden uspořádaný `.prop` na zařízení z build.prop každého oddílu (product, vendor, odm, system, system_ext, system_dlkm a dalších).
- **Paměťově úsporná extrakce**: oddíly payloadu se vypisují po jednom, aby se předešlo OOM u velkých OTA.
- **Multiplatformní správa balíčků**: `requirements.sh` podporuje apt, pacman, dnf, yum, zypper, apk, xbps, brew a Termux.
- **Ukládání a distribuce**:
  - **V repozitáři**: každý `.prop` se commituje do `props/<codename>/`, verzovaný a procházitelný.
  - **Jako aktiva vydání**: každý `.prop` se publikuje pod denním tagem pro přímé stažení.
- **Integrace s GitHub Actions**:
  - **Naplánované workflow**: automatizují aktualizace, extrakci a vydání podle plánu.
  - **Prevence duplicitních vydání**: zabraňuje nadbytečným vydáním kontrolou aktiv existujících vydání.
  - **Idempotentní vydání**: při opětovném spuštění znovu nahraje do existujícího denního tagu vydání.
  - **Oznámení Telegramu**: dostávejte včasné aktualizace s klikacími odkazy ke stažení.

## 📝 Zásady odpovědného používání

Tento projekt je poskytován pro vzdělávací a experimentální účely. I když je navržen pro efektivitu, je zásadní používat tento nástroj odpovědně.

- **Revize kódu**: před nasazením v jakémkoli prostředí si kód důkladně prostudujte a pochopte jej.
- **Osvědčené bezpečnostní postupy**: dodržujte oborové standardy bezpečnosti a právní shody.

Tvůrci tohoto projektu nenesou odpovědnost za jakékoli zneužití nebo škody vzniklé jeho použitím.

## Poděkování

Tento projekt je fork **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** od **[@T3SL4](https://github.com/T3SL4)**, který stál u zrodu pipeline pro extrakci z OTA do prop. Zde je přepracován tak, aby ukládal a distribuoval soubory `.prop` místo instalovatelných modulů. Veškerá zásluha za původní práci patří jejímu autorovi.

## Kontakt

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licence

**GNU GPL-3.0-or-later** - viz [LICENSE](LICENSE). Copyleft: kdo distribuuje upravenou verzi, musí nabídnout její zdrojový kód za stejných podmínek.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
