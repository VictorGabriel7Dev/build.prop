[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | **한국어** | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Google의 OTA 이미지에서 바로 가져온 실제 Pixel `.prop` 파일을 탐색할 수 있고 자동으로 업데이트되는 아카이브*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

각 Pixel의 전체 `build.prop`을 버전별로 보관하는 아카이브로, Google 공식 OTA 이미지에서 직접 추출하여 자동으로 최신 상태를 유지합니다. 모든 기기의 `.prop`은 저장소에 보관되고 릴리스 자산으로 게시되므로, 어떠한 도구도 필요 없이 바로 탐색하거나 다운로드할 수 있습니다.

## 📥 Get a `.prop`

설정이 필요 없는 두 가지 방법:

- **저장소 탐색하기**: [`<codename>/`](.)를 열고 `<codename>_<build_id>.prop`을 선택하세요.
- **Releases에서 다운로드하기**: 최신 [릴리스](https://github.com/VictorGabriel7Dev/build.prop/releases)(`build-YYYYMMDD`로 태그됨)에서 파일을 받으세요.

각 `.prop`은 해당 기기와 빌드에 정확히 대응하는, 완전하고 정리된 빌드 속성 집합입니다(product, vendor, odm, system, system_ext, system_dlkm 등).

## 🔧 Build it yourself

다운로드하는 대신 로컬에서 `.prop`을 추출하려면 Unix 계열 환경(Bash가 있는 Linux 또는 macOS)과 함께 `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, 그리고 `payload_dumper`가 포함된 Python ≥3.8이 필요합니다. `requirements.sh`는 대부분의 패키지 관리자(apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux)에서 의존성을 설치합니다.

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

지원되는 기기는 [Google Android Images](https://developers.google.com/android/images)와 [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota)에 있는 팩토리 이미지 및 OTA 이미지입니다. 추출은 각 payload 파티션을 한 번에 하나씩 읽으며(낮은 메모리), EROFS, ext4, sparse 및 boot/init_boot 이미지를 처리합니다.

## 🤖 Automation

GitHub Actions 파이프라인(`.github/workflows/build.yml`)이 아카이브를 최신 상태로 유지합니다:

- 매주 실행되며, 공백으로 구분된 기기 목록 또는 `all`을 사용해 `workflow_dispatch`로 필요할 때도 실행할 수 있습니다. 각 기기는 병렬로 빌드됩니다.
- `.prop`을 추출하고, 새로운 것들을 `<codename>/` 아래에 커밋하며, 단일 일일 태그(`build-YYYYMMDD`) 아래에 자산으로 게시합니다.
- 이미 릴리스된 `.prop` 파일은 건너뛰고, 클릭 가능한 다운로드 링크와 함께 Telegram으로 알립니다.

파이프라인을 실행하는 fork에는 두 개의 시크릿이 필요합니다: `TELEGRAM_BOT_TOKEN`([@BotFather](https://t.me/BotFather)에서 발급)과 `TELEGRAM_CHAT_ID`.

## Acknowledgements

이 프로젝트는 OTA에서 prop으로의 추출 파이프라인을 개척한 **[@T3SL4](https://github.com/T3SL4)**의 **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)**의 fork입니다. 원작에 대한 모든 공로는 그 저자에게 돌아갑니다.

## 연락처

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - [LICENSE](LICENSE)를 참조하세요. 카피레프트: 수정된 버전을 배포하는 사람은 누구나 동일한 조건으로 그 소스를 제공해야 합니다.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
