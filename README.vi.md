[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | **Tiếng Việt** | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | [ไทย](README.th.md)

# Pixel Prop Builder

*Trích xuất và phân phối `.prop` đầy đủ của Pixel trực tiếp từ các ảnh OTA của Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

Trích xuất và quản lý các thuộc tính hệ thống từ các bản cập nhật OTA của Pixel một cách dễ dàng với bộ công cụ tự động hóa mạnh mẽ này. Nó trích xuất `.prop` đầy đủ và có tổ chức của từng thiết bị trực tiếp từ các ảnh OTA chính thức của Google, rồi **lưu trữ và phân phối các tệp `.prop` đó** - vừa được quản lý phiên bản trong kho vừa được phát hành dưới dạng asset của release. Không có mô-đun cài đặt: chỉ các thuộc tính.

## 🚀 Bắt đầu nhanh

### Điều kiện tiên quyết

- **Môi trường kiểu Unix**: Linux hoặc macOS có Bash.
- **Tiện ích cốt lõi**:
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

## Cài đặt

1. **Nhân bản kho lưu trữ**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **Tạo và kích hoạt môi trường ảo** (tùy chọn nhưng được khuyến nghị):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **Cài đặt các phụ thuộc**:

    ```bash
    pip3 install payload_dumper
    ```

## Cách dùng

### Cục bộ

1. **Tải các ảnh OTA mới nhất**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    Ví dụ:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### Các thiết bị được hỗ trợ trong ảnh factory hoặc OTA mong muốn từ [Google Android Images](https://developers.google.com/android/images) hoặc [các trang Beta OTA](https://developer.android.com/about/versions/17/download-ota).

2. **Giải nén ảnh và thu thập `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    Việc này tự động:
    - Giải nén các phân vùng payload.bin lần lượt từng cái một (ít tốn bộ nhớ)
    - Phát hiện và xử lý ảnh **EROFS**, **ext4**, **sparse** và **boot/init_boot**
    - Dựng `.prop` đầy đủ và có tổ chức từ build.prop của mỗi phân vùng
    - Lưu vào `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

Kho lưu trữ bao gồm một pipeline CI hoàn toàn tự động (`.github/workflows/build.yml`):

- **Bản dựng theo lịch**: chạy vào nửa đêm UTC mỗi Chủ nhật.
- **Kích hoạt thủ công**: kích hoạt qua `workflow_dispatch` với danh sách thiết bị phân tách bằng dấu cách hoặc `all`.
- **Bản dựng ma trận**: mỗi thiết bị được xử lý song song.
- **Ngăn trùng lặp**: bỏ qua các `.prop` đã có trong các bản phát hành hiện có.
- **Quản lý phiên bản trong kho**: các `.prop` mới được commit vào `props/<codename>/`.
- **Bản phát hành gộp**: tất cả các `.prop` mới được phát hành dưới một thẻ hằng ngày duy nhất (`build-YYYYMMDD`).
- **Thông báo Telegram**: gửi một tin nhắn có định dạng kèm liên kết tải xuống có thể nhấp.

#### Secret cần thiết

| Secret | Mô tả |
|--------|-------|
| `TELEGRAM_BOT_TOKEN` | Token bot Telegram của bạn lấy từ [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID cuộc trò chuyện đích (người dùng, nhóm hoặc kênh) |

## ✨ Tính năng chính

- **Tự động thu thập OTA**: tải các bản dựng mới nhất trực tiếp từ các nguồn chính thức của Google.
- **Hỗ trợ hệ thống tệp hiện đại**: xử lý ảnh EROFS, ext4, sparse và ramdisk boot/init_boot.
- **Tạo `.prop` đầy đủ**: dựng một `.prop` có tổ chức duy nhất cho mỗi thiết bị từ build.prop của mỗi phân vùng (product, vendor, odm, system, system_ext, system_dlkm và hơn nữa).
- **Giải nén tiết kiệm bộ nhớ**: các phân vùng payload được trích xuất lần lượt để tránh OOM trên các OTA lớn.
- **Quản lý gói đa nền tảng**: `requirements.sh` hỗ trợ apt, pacman, dnf, yum, zypper, apk, xbps, brew và Termux.
- **Lưu trữ và phân phối**:
  - **Trong kho**: mỗi `.prop` được commit vào `props/<codename>/`, có phiên bản và có thể duyệt.
  - **Dưới dạng asset của release**: mỗi `.prop` được phát hành dưới thẻ hằng ngày để tải xuống trực tiếp.
- **Tích hợp GitHub Actions**:
  - **Quy trình theo lịch**: tự động hóa cập nhật, trích xuất và phát hành theo lịch trình.
  - **Ngăn phát hành trùng lặp**: tránh các bản phát hành dư thừa bằng cách kiểm tra asset của các bản phát hành hiện có.
  - **Phát hành idempotent**: tải lên lại vào một thẻ phát hành hằng ngày hiện có nếu được kích hoạt lại.
  - **Thông báo Telegram**: nhận các cập nhật kịp thời kèm liên kết tải xuống có thể nhấp.

## 📝 Nguyên tắc sử dụng có trách nhiệm

Dự án này được cung cấp cho mục đích giáo dục và thử nghiệm. Mặc dù được thiết kế để hiệu quả, điều quan trọng là phải sử dụng công cụ này một cách có trách nhiệm.

- **Xem xét mã**: xem xét và hiểu kỹ mã trước khi triển khai trong bất kỳ môi trường nào.
- **Thực hành bảo mật tốt nhất**: tuân thủ các tiêu chuẩn ngành về bảo mật và tuân thủ pháp lý.

Những người tạo ra dự án này không chịu trách nhiệm cho bất kỳ việc lạm dụng hay thiệt hại nào phát sinh từ việc sử dụng nó.

## Lời cảm ơn

Dự án này là một fork của **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** bởi **[@T3SL4](https://github.com/T3SL4)**, người đã tiên phong pipeline trích xuất từ OTA sang prop. Ở đây nó được tái cấu trúc để lưu trữ và phân phối các tệp `.prop` thay vì các mô-đun cài đặt. Mọi công lao cho công trình gốc thuộc về tác giả của nó.

## Liên hệ

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## Giấy phép

**GNU GPL-3.0-or-later** - xem [LICENSE](LICENSE). Copyleft: bất kỳ ai phân phối phiên bản đã sửa đổi phải cung cấp mã nguồn của nó theo cùng các điều khoản.

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
