[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | **Tiếng Việt** | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Một kho lưu trữ có thể duyệt, tự động cập nhật dữ liệu `build.prop` Pixel thật, lấy thẳng từ các ảnh chính thức của Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Một kho lưu trữ theo phiên bản gồm **4 bản build gần nhất của mỗi kênh** (stable, beta và canary) cho mọi máy Pixel gần đây, được trích xuất trực tiếp từ các ảnh factory và OTA chính thức của Google. Mỗi mục là tệp `build.prop` **đầy đủ**, được gộp từ **mọi phân vùng** (system, system_ext, product, vendor, odm và các ảnh `_dlkm`), và mang theo **`ro.boot.vbmeta.digest`** (hash verified boot). Mọi thứ được lưu trong kho, được lập chỉ mục trong một `index.json` mà máy đọc được, và được phát hành dưới dạng tài nguyên release. Không cần công cụ nào.

## 📥 Get the data

Ba cách, không cần thiết lập gì:

- **Duyệt kho** - mở [`<codename>/`](.) và chọn một tệp. Đặt tên theo kênh:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - một manifest mà máy đọc được, ánh xạ mỗi thiết bị → kênh → bản build mới nhất, với `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` và `vbmeta_digest`. Lý tưởng cho tự động hóa và công cụ.
- **Releases** - tải toàn bộ kho ngữ liệu dưới dạng một tệp `.zip` duy nhất (kèm `index.json`) từ [release](https://github.com/VictorGabriel7Dev/build.prop/releases) mới nhất (được gắn thẻ `build-YYYYMMDD`).

Mỗi `.prop` là tập hợp đầy đủ và được sắp xếp các thuộc tính cho đúng thiết bị và bản build đó - tất cả phân vùng, cộng với `ro.boot.vbmeta.digest`.

## 🗂️ What's inside

- **Mọi thiết bị Pixel gần đây** (Pixel 6 trở lên).
- **Ba kênh cho mỗi thiết bị** - stable, beta và canary, các bản build mới nhất của mỗi kênh (tùy theo những gì Google thực sự phát hành; một số thiết bị hoàn toàn mới vẫn chỉ có một hoặc hai bản build trên canary).
- **`build.prop` đầy đủ** cho mỗi bản build (~300-390 thuộc tính), được gộp từ tất cả phân vùng.
- **`vbmeta.digest`** (hash verified boot) được lưu cùng với các thuộc tính.

## 🔧 Build it yourself

Để trích xuất một `.prop` cục bộ thay vì tải xuống, bạn cần một môi trường kiểu Unix (Linux hoặc macOS có Bash) cùng với `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq`, và Python ≥3.8 có `payload_dumper`. `requirements.sh` cài đặt các phụ thuộc trên hầu hết các trình quản lý gói (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux).

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

Các thiết bị được hỗ trợ là những ảnh factory và OTA trên [Google Android Images](https://developers.google.com/android/images) và các [Beta OTA pages](https://developer.android.com/about/versions/17/download-ota). Quá trình trích xuất đọc từng phân vùng payload một lần một (ít bộ nhớ) và xử lý các ảnh EROFS, ext4, sparse và boot/init_boot.

## 🤖 Automation

Kho lưu trữ tự động được giữ cập nhật: khi Google phát hành các bản build mới, chúng được trích xuất (đầy đủ, tất cả phân vùng, kèm `vbmeta.digest`), các tệp `.prop` mới được commit vào `<codename>/`, `index.json` được làm mới, và một release có ngày tháng (`build-YYYYMMDD`) được tạo để những người theo dõi được thông báo về mỗi đợt.

Một `.github/workflows/build.yml` tổng quát, chạy theo yêu cầu cũng có sẵn (`workflow_dispatch`) như một phương án dự phòng thủ công để build `.prop` mới nhất của một thiết bị.

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
