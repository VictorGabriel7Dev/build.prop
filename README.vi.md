[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | **Tiếng Việt** | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Một kho lưu trữ có thể duyệt, tự động cập nhật các tệp `.prop` Pixel thật, lấy thẳng từ các ảnh OTA của Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Một kho lưu trữ theo phiên bản chứa toàn bộ `build.prop` của từng máy Pixel, được trích xuất trực tiếp từ các ảnh OTA chính thức của Google và tự động giữ cho luôn cập nhật. Tệp `.prop` của mỗi thiết bị được lưu trong kho và được phát hành dưới dạng tài nguyên release, sẵn sàng để duyệt hoặc tải xuống mà không cần bất kỳ công cụ nào.

## 📥 Get a `.prop`

Hai cách, không cần thiết lập gì:

- **Duyệt kho**: mở [`props/<codename>/`](props/) và chọn `<codename>_<build_id>.prop`.
- **Tải từ Releases**: lấy tệp từ [release](https://github.com/VictorGabriel7Dev/build.prop/releases) mới nhất (được gắn thẻ `build-YYYYMMDD`).

Mỗi `.prop` là tập hợp đầy đủ và được sắp xếp các thuộc tính build cho đúng thiết bị và bản build đó (product, vendor, odm, system, system_ext, system_dlkm và nhiều hơn nữa).

## 🔧 Build it yourself

Để trích xuất một `.prop` cục bộ thay vì tải xuống, bạn cần một môi trường kiểu Unix (Linux hoặc macOS có Bash) cùng với `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, và Python ≥3.8 có `payload_dumper`. `requirements.sh` cài đặt các phụ thuộc trên hầu hết các trình quản lý gói (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

Các thiết bị được hỗ trợ là những ảnh factory và OTA trên [Google Android Images](https://developers.google.com/android/images) và các [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Quá trình trích xuất đọc từng phân vùng payload một lần một (ít bộ nhớ) và xử lý các ảnh EROFS, ext4, sparse và boot/init_boot.

## 🤖 Automation

Một pipeline GitHub Actions (`.github/workflows/build.yml`) giữ cho kho lưu trữ luôn cập nhật:

- Chạy hàng tuần, và theo yêu cầu qua `workflow_dispatch` với danh sách thiết bị phân tách bằng khoảng trắng hoặc `all`; mỗi thiết bị được build song song.
- Trích xuất `.prop`, commit những tệp mới vào `props/<codename>/`, và phát hành chúng dưới dạng tài nguyên dưới một thẻ hằng ngày duy nhất (`build-YYYYMMDD`).
- Bỏ qua các tệp `.prop` đã được phát hành và thông báo qua Telegram kèm các liên kết tải xuống có thể nhấp được.

Các fork chạy pipeline cần hai secret: `TELEGRAM_BOT_TOKEN` (từ [@BotFather](https://t.me/BotFather)) và `TELEGRAM_CHAT_ID`.

## Acknowledgements

Dự án này là một fork của **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** của **[@T3SL4](https://github.com/T3SL4)**, người đã tiên phong tạo ra pipeline trích xuất từ OTA sang prop. Toàn bộ công lao cho công trình gốc thuộc về tác giả của nó.

## Liên hệ

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - xem [LICENSE](LICENSE). Copyleft: bất kỳ ai phân phối một phiên bản đã sửa đổi đều phải cung cấp mã nguồn của nó theo cùng các điều khoản.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
