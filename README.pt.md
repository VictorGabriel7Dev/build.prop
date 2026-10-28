[English](README.md) | **Português** | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Extraia e distribua o `.prop` completo do Pixel direto das imagens OTA do Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Extraia e gerencie sem esforço as propriedades de sistema a partir das atualizações OTA do Pixel com esta robusta suíte de automação. Ela extrai o `.prop` completo e organizado de cada dispositivo direto das imagens OTA oficiais do Google e então **armazena e distribui esses arquivos `.prop`** - tanto versionados no repositório quanto publicados como assets de release. Sem módulos instaláveis: apenas as propriedades.

## 🚀 Início rápido

### Pré-requisitos

- **Ambiente Unix-like**: Linux ou macOS com Bash.
- **Utilitários essenciais**:
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

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Crie e ative um ambiente virtual** (opcional, mas recomendado):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Instale as dependências**:

    ```bash
    pip3 install payload_dumper
    ```

## Uso

### Local

1. **Baixe as imagens OTA mais recentes**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Exemplos:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Dispositivos suportados nas imagens de fábrica ou OTA desejadas em [Google Android Images](https://developers.google.com/android/images) ou nas [páginas de OTA Beta](https://developer.android.com/about/versions/17/download-ota).

2. **Extraia as imagens e colete o `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Isto automaticamente:
    - Extrai as partições do payload.bin uma de cada vez (baixo consumo de memória)
    - Detecta e trata imagens **EROFS**, **ext4**, **sparse** e **boot/init_boot**
    - Monta o `.prop` completo e organizado a partir do build.prop de cada partição
    - Salva em `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

O repositório inclui um pipeline de CI totalmente automatizado (`.github/workflows/build.yml`):

- **Builds agendados**: executam todo domingo à meia-noite UTC.
- **Disparo manual**: acione via `workflow_dispatch` com uma lista de dispositivos separada por espaços ou `all`.
- **Builds em matriz**: cada dispositivo é processado em paralelo.
- **Prevenção de duplicatas**: pula os `.prop` já presentes em releases existentes.
- **Versionado no repositório**: os `.prop` novos são commitados em `props/<codename>/`.
- **Releases agregadas**: todos os `.prop` novos são publicados sob uma única tag diária (`build-YYYYMMDD`).
- **Notificações no Telegram**: envia uma mensagem formatada com links de download clicáveis.

#### Secrets necessários

| Secret | Descrição |
|--------|-----------|
| `TELEGRAM_BOT_TOKEN` | Seu token de bot do Telegram, obtido no [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID do chat de destino (usuário, grupo ou canal) |

## ✨ Principais recursos

- **Aquisição automática de OTA**: baixa os builds mais recentes direto das fontes oficiais do Google.
- **Suporte a sistemas de arquivos modernos**: trata imagens EROFS, ext4, sparse e ramdisks boot/init_boot.
- **Geração do `.prop` completo**: monta um único `.prop` organizado por dispositivo a partir do build.prop de cada partição (product, vendor, odm, system, system_ext, system_dlkm e mais).
- **Extração eficiente em memória**: as partições do payload são despejadas uma de cada vez para evitar OOM em OTAs grandes.
- **Gerenciamento de pacotes multiplataforma**: o `requirements.sh` suporta apt, pacman, dnf, yum, zypper, apk, xbps, brew e Termux.
- **Armazenamento e distribuição**:
  - **No repositório**: cada `.prop` é commitado em `props/<codename>/`, versionado e navegável.
  - **Como assets de release**: cada `.prop` é publicado sob a tag diária para download direto.
- **Integração com GitHub Actions**:
  - **Workflows agendados**: automatizam atualizações, extração e releases em uma agenda.
  - **Prevenção de releases duplicadas**: evita releases redundantes verificando os assets de releases existentes.
  - **Releases idempotentes**: reenvia para uma tag de release diária existente se reacionado.
  - **Notificações no Telegram**: receba atualizações no momento certo com links de download clicáveis.

## 📝 Diretrizes de uso responsável

Este projeto é fornecido para fins educacionais e experimentais. Embora tenha sido projetado para eficiência, é fundamental usar esta ferramenta de forma responsável.

- **Revisão de código**: revise e entenda bem o código antes de implantá-lo em qualquer ambiente.
- **Boas práticas de segurança**: siga os padrões do setor para segurança e conformidade legal.

Os criadores deste projeto não se responsabilizam por qualquer uso indevido ou danos decorrentes de seu uso.

## Agradecimentos

Este projeto é um fork do **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** de **[@T3SL4](https://github.com/T3SL4)**, que foi o pioneiro do pipeline de extração de OTA para prop. Aqui ele é remodelado para armazenar e distribuir arquivos `.prop` em vez de módulos instaláveis. Todo o crédito pelo trabalho original é do seu autor.

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

**GNU GPL-3.0-or-later** - veja [LICENSE](LICENSE). Copyleft: quem distribuir uma versão modificada deve oferecer o código-fonte sob os mesmos termos.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
