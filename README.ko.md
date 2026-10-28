[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | **한국어** | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Google OTA 이미지에서 직접 Pixel의 전체 `.prop`를 추출하고 배포하세요*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

이 강력한 자동화 도구 모음으로 Pixel OTA 업데이트에서 시스템 속성을 손쉽게 추출하고 관리하세요. 각 기기의 완전하고 정리된 `.prop`를 Google 공식 OTA 이미지에서 직접 추출한 다음 **그 `.prop` 파일들을 저장하고 배포합니다** - 저장소에서 버전 관리되며 릴리스 자산으로도 게시됩니다. 설치형 모듈은 없습니다: 속성만 있습니다.

## 🚀 빠른 시작

### 사전 요구 사항

- **유닉스 계열 환경**: Bash가 있는 Linux 또는 macOS.
- **핵심 유틸리티**:
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

## 설치

1. **저장소를 복제합니다**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **가상 환경을 만들고 활성화합니다**(선택 사항이지만 권장):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **의존성을 설치합니다**:

    ```bash
    pip3 install payload_dumper
    ```

## 사용법

### 로컬

1. **최신 OTA 이미지를 가져옵니다**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    예시:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### [Google Android Images](https://developers.google.com/android/images) 또는 [베타 OTA 페이지](https://developer.android.com/about/versions/17/download-ota)에서 원하는 공장 초기화 이미지 또는 OTA 이미지가 지원하는 기기.

2. **이미지를 추출하고 `.prop`를 수집합니다**:

    ```bash
    ./extract_images.sh
    ```

    이 작업은 자동으로:
    - payload.bin 파티션을 하나씩 추출합니다(낮은 메모리 사용량)
    - **EROFS**, **ext4**, **sparse**, **boot/init_boot** 이미지를 감지하고 처리합니다
    - 각 파티션의 build.prop에서 완전하고 정리된 `.prop`를 구성합니다
    - 이를 `props/<codename>/<codename>_<build_id>.prop`에 저장합니다

### GitHub Actions

이 저장소에는 완전히 자동화된 CI 파이프라인(`.github/workflows/build.yml`)이 포함되어 있습니다.

- **예약 빌드**: 매주 일요일 UTC 자정에 실행됩니다.
- **수동 실행**: 공백으로 구분된 기기 목록 또는 `all`을 사용하여 `workflow_dispatch`로 트리거합니다.
- **매트릭스 빌드**: 각 기기를 병렬로 처리합니다.
- **중복 방지**: 기존 릴리스에 이미 있는 `.prop` 파일은 건너뜁니다.
- **저장소에서 버전 관리**: 새 `.prop` 파일은 `props/<codename>/` 아래에 커밋됩니다.
- **집계 릴리스**: 모든 새 `.prop` 파일은 하나의 일일 태그(`build-YYYYMMDD`) 아래에 게시됩니다.
- **Telegram 알림**: 클릭 가능한 다운로드 링크가 포함된 형식화된 메시지를 보냅니다.

#### 필요한 시크릿

| 시크릿 | 설명 |
|--------|------|
| `TELEGRAM_BOT_TOKEN` | [@BotFather](https://t.me/BotFather)에서 받은 Telegram 봇 토큰 |
| `TELEGRAM_CHAT_ID` | 대상 채팅 ID(사용자, 그룹 또는 채널) |

## ✨ 주요 기능

- **자동 OTA 획득**: 최신 빌드를 Google 공식 소스에서 직접 다운로드합니다.
- **최신 파일 시스템 지원**: EROFS, ext4, sparse 이미지와 boot/init_boot ramdisk를 처리합니다.
- **완전한 `.prop` 생성**: 각 파티션의 build.prop에서 기기별로 하나의 정리된 `.prop`를 구성합니다(product, vendor, odm, system, system_ext, system_dlkm 등).
- **메모리 효율적 추출**: 대용량 OTA에서 OOM을 피하기 위해 payload 파티션을 하나씩 덤프합니다.
- **크로스 플랫폼 패키지 관리**: `requirements.sh`는 apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux를 지원합니다.
- **저장 및 배포**:
  - **저장소에서**: 각 `.prop`는 `props/<codename>/` 아래에 커밋되어 버전 관리되고 탐색할 수 있습니다.
  - **릴리스 자산으로**: 각 `.prop`는 직접 다운로드를 위해 일일 태그 아래에 게시됩니다.
- **GitHub Actions 통합**:
  - **예약 워크플로**: 업데이트, 추출, 릴리스를 일정에 따라 자동화합니다.
  - **중복 릴리스 방지**: 기존 릴리스 자산을 확인하여 불필요한 릴리스를 방지합니다.
  - **멱등 릴리스**: 다시 트리거되면 기존 일일 릴리스 태그에 다시 업로드합니다.
  - **Telegram 알림**: 클릭 가능한 다운로드 링크로 적시의 업데이트를 받습니다.

## 📝 책임 있는 사용 지침

이 프로젝트는 교육 및 실험 목적으로 제공됩니다. 효율성을 위해 설계되었지만 이 도구를 책임감 있게 사용하는 것이 매우 중요합니다.

- **코드 검토**: 어떤 환경에 배포하기 전에 코드를 철저히 검토하고 이해하세요.
- **보안 모범 사례**: 보안 및 법적 준수를 위한 업계 표준을 준수하세요.

이 프로젝트의 제작자는 그 사용으로 인해 발생하는 어떠한 오용이나 손해에 대해서도 책임지지 않습니다.

## 감사의 말

이 프로젝트는 OTA에서 prop으로의 추출 파이프라인을 개척한 **[@T3SL4](https://github.com/T3SL4)**의 **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** 포크입니다. 여기서는 설치형 모듈 대신 `.prop` 파일을 저장하고 배포하도록 재구성되었습니다. 원본 작업에 대한 모든 공로는 그 작성자에게 있습니다.

## 연락처

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## 라이선스

**GNU GPL-3.0-or-later** - [LICENSE](LICENSE)를 참조하세요. 카피레프트: 수정된 버전을 배포하는 사람은 동일한 조건으로 소스 코드를 제공해야 합니다.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
