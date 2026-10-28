[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | **ไทย**

# Pixel Prop Builder

*ดึงและแจกจ่าย `.prop` ฉบับเต็มของ Pixel โดยตรงจากอิมเมจ OTA ของ Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

ดึงและจัดการพร็อพเพอร์ตีของระบบจากอัปเดต OTA ของ Pixel ได้อย่างง่ายดายด้วยชุดเครื่องมืออัตโนมัติอันทรงพลังนี้ มันดึง `.prop` ฉบับเต็มและจัดระเบียบของแต่ละอุปกรณ์โดยตรงจากอิมเมจ OTA อย่างเป็นทางการของ Google จากนั้น **จัดเก็บและแจกจ่ายไฟล์ `.prop` เหล่านั้น** - ทั้งแบบมีการกำหนดเวอร์ชันในที่เก็บและเผยแพร่เป็นแอสเซ็ตของรีลีส ไม่มีโมดูลที่ติดตั้งได้: มีเพียงพร็อพเพอร์ตีเท่านั้น

## 🚀 เริ่มต้นอย่างรวดเร็ว

### ข้อกำหนดเบื้องต้น

- **สภาพแวดล้อมแบบ Unix**: Linux หรือ macOS ที่มี Bash
- **ยูทิลิตีหลัก**:
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

## การติดตั้ง

1. **โคลนที่เก็บ (repository)**:

   ```bash
   git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
   ```

2. **สร้างและเปิดใช้งานสภาพแวดล้อมเสมือน** (ไม่บังคับ แต่แนะนำ):

    ```bash
    python3 -m venv .venv
    . .venv/bin/activate
    ```

3. **ติดตั้งแพ็กเกจที่จำเป็น**:

    ```bash
    pip3 install payload_dumper
    ```

## การใช้งาน

### แบบโลคัล

1. **ดึงอิมเมจ OTA ล่าสุด**:

    ```bash
    ./download_latest_ota_build.sh <device_name> [device_name ...]
    ```

    ตัวอย่าง:
    - `./download_latest_ota_build.sh husky`
    - `./download_latest_ota_build.sh cubs grizzly_beta kodiak_beta17 yogi`

    #### อุปกรณ์ที่รองรับในอิมเมจโรงงานหรือ OTA ที่ต้องการจาก [Google Android Images](https://developers.google.com/android/images) หรือ [หน้า Beta OTA](https://developer.android.com/about/versions/17/download-ota)

2. **แตกอิมเมจและรวบรวม `.prop`**:

    ```bash
    ./extract_images.sh
    ```

    สิ่งนี้จะทำโดยอัตโนมัติ:
    - แตกพาร์ทิชันของ payload.bin ทีละรายการ (ใช้หน่วยความจำน้อย)
    - ตรวจจับและจัดการอิมเมจ **EROFS**, **ext4**, **sparse** และ **boot/init_boot**
    - สร้าง `.prop` ฉบับเต็มและจัดระเบียบจาก build.prop ของแต่ละพาร์ทิชัน
    - บันทึกไว้ที่ `props/<codename>/<codename>_<build_id>.prop`

### GitHub Actions

ที่เก็บนี้มีไปป์ไลน์ CI แบบอัตโนมัติเต็มรูปแบบ (`.github/workflows/build.yml`):

- **บิลด์ตามกำหนดเวลา**: ทำงานทุกวันอาทิตย์เวลาเที่ยงคืน UTC
- **เรียกใช้ด้วยตนเอง**: ทริกเกอร์ผ่าน `workflow_dispatch` ด้วยรายการอุปกรณ์ที่คั่นด้วยช่องว่างหรือ `all`
- **บิลด์แบบเมทริกซ์**: อุปกรณ์แต่ละตัวถูกประมวลผลแบบขนาน
- **ป้องกันรายการซ้ำ**: ข้ามไฟล์ `.prop` ที่มีอยู่แล้วในรีลีสที่มีอยู่
- **มีการกำหนดเวอร์ชันในที่เก็บ**: ไฟล์ `.prop` ใหม่ถูก commit ไว้ภายใต้ `props/<codename>/`
- **รีลีสแบบรวม**: ไฟล์ `.prop` ใหม่ทั้งหมดถูกเผยแพร่ภายใต้แท็กรายวันเดียว (`build-YYYYMMDD`)
- **การแจ้งเตือน Telegram**: ส่งข้อความที่จัดรูปแบบพร้อมลิงก์ดาวน์โหลดที่คลิกได้

#### Secrets ที่จำเป็น

| Secret | คำอธิบาย |
|--------|----------|
| `TELEGRAM_BOT_TOKEN` | โทเค็นบอต Telegram ของคุณจาก [@BotFather](https://t.me/BotFather) |
| `TELEGRAM_CHAT_ID` | ID ของแชตปลายทาง (ผู้ใช้ กลุ่ม หรือช่อง) |

## ✨ คุณสมบัติหลัก

- **การดึง OTA อัตโนมัติ**: ดาวน์โหลดบิลด์ล่าสุดโดยตรงจากแหล่งที่มาอย่างเป็นทางการของ Google
- **รองรับระบบไฟล์สมัยใหม่**: จัดการอิมเมจ EROFS, ext4, sparse และ ramdisk ของ boot/init_boot
- **การสร้าง `.prop` ฉบับเต็ม**: สร้าง `.prop` ที่จัดระเบียบหนึ่งไฟล์ต่ออุปกรณ์จาก build.prop ของแต่ละพาร์ทิชัน (product, vendor, odm, system, system_ext, system_dlkm และอื่น ๆ)
- **การแตกไฟล์ที่ประหยัดหน่วยความจำ**: พาร์ทิชันของ payload ถูกดัมพ์ทีละรายการเพื่อหลีกเลี่ยง OOM บน OTA ขนาดใหญ่
- **การจัดการแพ็กเกจข้ามแพลตฟอร์ม**: `requirements.sh` รองรับ apt, pacman, dnf, yum, zypper, apk, xbps, brew และ Termux
- **การจัดเก็บและแจกจ่าย**:
  - **ในที่เก็บ**: `.prop` แต่ละไฟล์ถูก commit ไว้ภายใต้ `props/<codename>/` มีการกำหนดเวอร์ชันและเรียกดูได้
  - **เป็นแอสเซ็ตของรีลีส**: `.prop` แต่ละไฟล์ถูกเผยแพร่ภายใต้แท็กรายวันสำหรับการดาวน์โหลดโดยตรง
- **การผสานรวมกับ GitHub Actions**:
  - **เวิร์กโฟลว์ตามกำหนดเวลา**: ทำให้การอัปเดต การแตกไฟล์ และการรีลีสเป็นอัตโนมัติตามกำหนดการ
  - **การป้องกันรีลีสซ้ำ**: หลีกเลี่ยงรีลีสที่ซ้ำซ้อนด้วยการตรวจสอบแอสเซ็ตของรีลีสที่มีอยู่
  - **รีลีสแบบ idempotent**: อัปโหลดซ้ำไปยังแท็กรีลีสรายวันที่มีอยู่หากถูกทริกเกอร์อีกครั้ง
  - **การแจ้งเตือน Telegram**: รับการอัปเดตที่ทันเวลาพร้อมลิงก์ดาวน์โหลดที่คลิกได้

## 📝 แนวทางการใช้งานอย่างมีความรับผิดชอบ

โครงการนี้จัดทำขึ้นเพื่อวัตถุประสงค์ด้านการศึกษาและการทดลอง แม้จะออกแบบมาเพื่อประสิทธิภาพ แต่การใช้เครื่องมือนี้อย่างมีความรับผิดชอบเป็นสิ่งสำคัญยิ่ง

- **การตรวจทานโค้ด**: ตรวจทานและทำความเข้าใจโค้ดอย่างละเอียดก่อนนำไปใช้งานในสภาพแวดล้อมใด ๆ
- **แนวปฏิบัติด้านความปลอดภัยที่ดีที่สุด**: ปฏิบัติตามมาตรฐานอุตสาหกรรมด้านความปลอดภัยและการปฏิบัติตามกฎหมาย

ผู้สร้างโครงการนี้ไม่รับผิดชอบต่อการใช้งานในทางที่ผิดหรือความเสียหายใด ๆ ที่เกิดจากการใช้งาน

## กิตติกรรมประกาศ

โครงการนี้เป็นฟอร์กของ **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** โดย **[@T3SL4](https://github.com/T3SL4)** ผู้ริเริ่มไปป์ไลน์การแตกข้อมูลจาก OTA ไปเป็น prop ที่นี่ได้รับการปรับใหม่เพื่อจัดเก็บและแจกจ่ายไฟล์ `.prop` แทนโมดูลที่ติดตั้งได้ เครดิตทั้งหมดของงานต้นฉบับเป็นของผู้เขียน

## ติดต่อ

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## สัญญาอนุญาต

**GNU GPL-3.0-or-later** - ดู [LICENSE](LICENSE) คอปปี้เลฟต์: ผู้ที่แจกจ่ายเวอร์ชันที่แก้ไขแล้วต้องเสนอซอร์สโค้ดภายใต้เงื่อนไขเดียวกัน

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `magisk` `kernelsu` `system-properties` `automation`
