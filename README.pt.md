[English](README.md) | **Português** | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Um acervo navegável e atualizado automaticamente de arquivos `.prop` reais de Pixel, direto das imagens OTA do Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Um acervo versionado do `build.prop` completo de cada Pixel, extraído diretamente das imagens OTA oficiais do Google e mantido atualizado automaticamente. O `.prop` de cada aparelho é armazenado no repositório e publicado como asset de release, pronto para navegar ou baixar sem precisar de nenhuma ferramenta.

## 📥 Obtenha um `.prop`

Duas maneiras, sem configuração necessária:

- **Navegue pelo repositório**: abra [`props/<codename>/`](props/) e escolha `<codename>_<build_id>.prop`.
- **Baixe pelas Releases**: pegue o arquivo na [release](https://github.com/VictorGabriel7Dev/build.prop/releases) mais recente (com a tag `build-YYYYMMDD`).

Cada `.prop` é o conjunto completo e organizado de propriedades de build daquele aparelho e build exatos (product, vendor, odm, system, system_ext, system_dlkm e mais).

## 🔧 Compile você mesmo

Para extrair um `.prop` localmente em vez de baixá-lo, você precisa de um ambiente Unix-like (Linux ou macOS com Bash) além de `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` e Python ≥3.8 com `payload_dumper`. O `requirements.sh` instala as dependências na maioria dos gerenciadores de pacotes (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
pip3 install payload_dumper
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Os aparelhos suportados são as imagens de fábrica e OTA em [Google Android Images](https://developers.google.com/android/images) e nas [páginas de OTA Beta](https://developer.android.com/about/versions/17/download-ota). A extração lê cada partição do payload uma de cada vez (baixo consumo de memória) e lida com imagens EROFS, ext4, sparse e boot/init_boot.

## 🤖 Automação

Um pipeline do GitHub Actions (`.github/workflows/build.yml`) mantém o acervo atualizado:

- Executa semanalmente, e sob demanda via `workflow_dispatch` com uma lista de aparelhos separada por espaços ou `all`; cada aparelho é compilado em paralelo.
- Extrai o `.prop`, faz commit dos novos em `props/<codename>/` e os publica como assets sob uma única tag diária (`build-YYYYMMDD`).
- Pula os arquivos `.prop` já publicados e notifica o Telegram com links de download clicáveis.

Forks que executam o pipeline precisam de dois secrets: `TELEGRAM_BOT_TOKEN` (do [@BotFather](https://t.me/BotFather)) e `TELEGRAM_CHAT_ID`.

## Agradecimentos

Este projeto é um fork de **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** de **[@T3SL4](https://github.com/T3SL4)**, que foi pioneiro no pipeline de extração de OTA para prop. Todo o crédito pelo trabalho original é do seu autor.

## Contato

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Licença

**GNU GPL-3.0-or-later** - veja [LICENSE](LICENSE). Copyleft: quem distribuir uma versão modificada deve oferecer o código-fonte dela sob os mesmos termos.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
