[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | **ไทย**

# Pixel Prop Builder

*คลังไฟล์ `.prop` จริงของ Pixel ที่เรียกดูได้และอัปเดตอัตโนมัติ ตรงจากอิมเมจ OTA ของ Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

คลังเก็บแบบมีเวอร์ชันของ `build.prop` ฉบับเต็มของ Pixel แต่ละเครื่อง ซึ่งดึงมาโดยตรงจากอิมเมจ OTA อย่างเป็นทางการของ Google และคงความเป็นปัจจุบันไว้โดยอัตโนมัติ ไฟล์ `.prop` ของทุกอุปกรณ์ถูกเก็บไว้ในที่เก็บโค้ดและเผยแพร่เป็นแอสเซตของ release พร้อมให้เรียกดูหรือดาวน์โหลดได้โดยไม่ต้องใช้เครื่องมือใด ๆ

## 📥 Get a `.prop`

สองวิธี ไม่ต้องตั้งค่าใด ๆ:

- **เรียกดูที่เก็บโค้ด**: เปิด [`props/<codename>/`](props/) แล้วเลือก `<codename>_<build_id>.prop`
- **ดาวน์โหลดจาก Releases**: ดึงไฟล์จาก [release](https://github.com/VictorGabriel7Dev/build.prop/releases) ล่าสุด (ติดแท็ก `build-YYYYMMDD`)

`.prop` แต่ละไฟล์คือชุดคุณสมบัติ build ฉบับเต็มที่จัดระเบียบแล้วสำหรับอุปกรณ์และ build นั้นโดยเฉพาะ (product, vendor, odm, system, system_ext, system_dlkm และอื่น ๆ)

## 🔧 Build it yourself

หากต้องการแยกไฟล์ `.prop` ในเครื่องเองแทนการดาวน์โหลด คุณต้องมีสภาพแวดล้อมแบบ Unix (Linux หรือ macOS ที่มี Bash) พร้อมกับ `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` และ Python ≥3.8 พร้อม `payload_dumper` โดย `requirements.sh` จะติดตั้ง dependency เหล่านี้ผ่านตัวจัดการแพ็กเกจส่วนใหญ่ (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux)

```bash
git clone https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
pip3 install payload_dumper
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> props/<codename>/<codename>_<build_id>.prop
```

อุปกรณ์ที่รองรับคืออิมเมจ factory และ OTA ที่อยู่บน [Google Android Images](https://developers.google.com/android/images) และ [หน้า Beta OTA](https://developer.android.com/about/versions/17/download-ota) การแยกไฟล์จะอ่านแต่ละพาร์ทิชันของ payload ทีละรายการ (ใช้หน่วยความจำต่ำ) และรองรับอิมเมจแบบ EROFS, ext4, sparse และ boot/init_boot

## 🤖 Automation

ไปป์ไลน์ GitHub Actions (`.github/workflows/build.yml`) คอยให้คลังเก็บเป็นปัจจุบันอยู่เสมอ:

- ทำงานรายสัปดาห์ และตามคำสั่งผ่าน `workflow_dispatch` ด้วยรายชื่ออุปกรณ์ที่คั่นด้วยช่องว่างหรือ `all` โดยแต่ละอุปกรณ์จะ build แบบขนานกัน
- แยกไฟล์ `.prop`, commit ไฟล์ใหม่ไว้ภายใต้ `props/<codename>/` และเผยแพร่เป็นแอสเซตภายใต้แท็กรายวันแท็กเดียว (`build-YYYYMMDD`)
- ข้ามไฟล์ `.prop` ที่เผยแพร่ไปแล้ว และแจ้ง Telegram พร้อมลิงก์ดาวน์โหลดที่คลิกได้

Fork ที่รันไปป์ไลน์นี้ต้องใช้ secret สองรายการ: `TELEGRAM_BOT_TOKEN` (จาก [@BotFather](https://t.me/BotFather)) และ `TELEGRAM_CHAT_ID`

## Acknowledgements

โปรเจกต์นี้เป็น fork ของ **[Pixel-Props/build.prop](https://github.com/Pixel-Props/build.prop)** โดย **[@T3SL4](https://github.com/T3SL4)** ผู้บุกเบิกไปป์ไลน์การแยกจาก OTA ไปเป็น prop เครดิตทั้งหมดของงานต้นฉบับเป็นของผู้เขียน

## ติดต่อ

- https://victorgabriel.dev
- **GitHub:** @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
- **Telegram:** @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
- **Discord:** @VictorGabriel.dev https://discord.com/users/1481407654458036265
- **LinkedIn:** in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
- **Instagram:** @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
- **WhatsApp:** @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
- **E-mail:** contato@victorgabriel.dev

## License

**GNU GPL-3.0-or-later** - ดู [LICENSE](LICENSE) แบบ copyleft: ผู้ใดก็ตามที่แจกจ่ายเวอร์ชันที่ดัดแปลงต้องเสนอซอร์สของมันภายใต้เงื่อนไขเดียวกัน

---

`android` `pixel` `build-prop` `ota` `factory-image` `device-fingerprint` `play-integrity` `attestation` `system-properties` `automation`
