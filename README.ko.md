[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | **한국어** | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Google의 공식 이미지에서 바로 가져온 실제 Pixel `build.prop` 데이터를 탐색할 수 있고 자동으로 업데이트되는 아카이브*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

최근의 모든 Pixel에 대해 **각 채널의 최근 4개 빌드**(stable, beta, canary)를 버전별로 보관하는 아카이브로, Google 공식 팩토리 이미지와 OTA 이미지에서 직접 추출합니다. 각 항목은 **전체** `build.prop`으로, **모든 파티션**(system, system_ext, product, vendor, odm 및 `_dlkm` 이미지)에 걸쳐 병합되며 **`ro.boot.vbmeta.digest`**(verified boot 해시)를 담고 있습니다. 모든 것이 저장소에 보관되고, 머신으로 읽을 수 있는 `index.json`에 색인되며, 릴리스 자산으로 게시됩니다. 어떠한 도구도 필요하지 않습니다.

## 📥 Get the data

설정이 필요 없는 세 가지 방법:

- **저장소 탐색하기**: [`<codename>/`](.)를 열고 파일을 선택하세요. 채널별 명명 규칙:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`**: 각 기기 → 채널 → 최신 빌드를 매핑하는 머신 판독용 매니페스트로, `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental`, `vbmeta_digest`를 포함합니다. 자동화와 도구 연동에 이상적입니다.
- **Releases**: 최신 [릴리스](https://github.com/VictorGabriel7Dev/build.prop/releases)(`build-YYYYMMDD`로 태그됨)에서 전체 코퍼스를 단일 `.zip`(및 `index.json`)으로 다운로드하세요.

각 `.prop`은 해당 기기와 빌드에 정확히 대응하는, 완전하고 정리된 속성 집합입니다 - 모든 파티션과 함께 `ro.boot.vbmeta.digest`도 포함합니다.

## 🗂️ What's inside

- **최근의 모든 Pixel 기기**(Pixel 6 및 이후 기종).
- **기기당 세 개의 채널** - stable, beta, canary, 각각의 최신 빌드(Google이 실제로 게시하는 내용에 따라 다름. 일부 신규 기기는 canary에 아직 빌드가 한두 개뿐일 수 있습니다).
- **전체 `build.prop`**, 빌드당 약 300-390개의 속성으로, 모든 파티션에서 병합됩니다.
- **`vbmeta.digest`**(verified boot 해시)가 속성과 함께 저장됩니다.

## 🔧 Build one yourself

다운로드하는 대신 로컬에서 단일 `.prop`을 추출하려면 Unix 계열 환경(Bash가 있는 Linux 또는 macOS)과 함께 `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, 그리고 `payload_dumper`가 포함된 Python ≥3.8이 필요합니다. `requirements.sh`는 대부분의 패키지 관리자(apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux)에서 의존성을 설치합니다.

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

지원되는 기기는 [Google Android Images](https://developers.google.com/android/images)와 [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota)에 있는 팩토리 이미지 및 OTA 이미지입니다. 추출은 각 payload 파티션을 한 번에 하나씩 읽으며(낮은 메모리), EROFS, ext4, sparse 및 boot/init_boot 이미지를 처리합니다.

## 🤖 Automation

아카이브는 자동으로 최신 상태를 유지합니다: Google이 새 빌드를 게시하면 추출되고(전체, 모든 파티션, `vbmeta.digest` 포함), 새로운 `.prop`이 `<codename>/` 아래에 커밋되며, `index.json`이 갱신되고, 날짜가 붙은 릴리스(`build-YYYYMMDD`)가 생성되어 관찰자들이 모든 업데이트 물결마다 알림을 받습니다.

범용이고 온디맨드인 `.github/workflows/build.yml`(`workflow_dispatch`)도 기기의 최신 `.prop`을 수동으로 빌드하기 위한 대체 수단으로 제공됩니다.

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
