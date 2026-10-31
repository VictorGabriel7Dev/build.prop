[English](README.md) | [Português](README.pt.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Tiếng Việt](README.vi.md) | [中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [فارسی](README.fa.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md) | **ไทย**

# Pixel Prop Builder

*คลังข้อมูล `build.prop` จริงของ Pixel ที่เรียกดูได้และอัปเดตอัตโนมัติ ตรงจากอิมเมจอย่างเป็นทางการของ Google*

[![License: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/VictorGabriel7Dev/build.prop)](https://github.com/VictorGabriel7Dev/build.prop/releases)
[![Languages](https://img.shields.io/badge/languages-21-orange.svg)](README.md)

คลังเก็บแบบมีเวอร์ชันของ **4 build ล่าสุดของแต่ละ channel** (stable, beta และ canary) สำหรับ Pixel รุ่นใหม่ ๆ ทุกเครื่อง ซึ่งดึงมาโดยตรงจากอิมเมจ factory และ OTA อย่างเป็นทางการของ Google แต่ละรายการคือ `build.prop` **ฉบับเต็ม** ที่รวมจาก **ทุกพาร์ทิชัน** (system, system_ext, product, vendor, odm และอิมเมจ `_dlkm`) และมี **`ro.boot.vbmeta.digest`** (hash ของ verified boot) ทุกอย่างถูกเก็บไว้ในที่เก็บโค้ด จัดทำดัชนีไว้ใน `index.json` ที่เครื่องอ่านได้ และเผยแพร่เป็นแอสเซตของ release โดยไม่ต้องใช้เครื่องมือใด ๆ

## 📥 Get the data

สามวิธี ไม่ต้องตั้งค่าใด ๆ:

- **เรียกดูที่เก็บโค้ด** - เปิด [`<codename>/`](.) แล้วเลือกไฟล์ การตั้งชื่อตาม channel:
  - `<codename>_<incremental>.prop` - stable
  - `<codename>_beta_<incremental>.prop` - beta
  - `<codename>_canary_<incremental>.prop` - canary
- **`index.json`** - ไฟล์ manifest ที่เครื่องอ่านได้ ซึ่งจับคู่แต่ละอุปกรณ์ → channel → build ล่าสุด พร้อม `model`, `soc`, `first_api_level`, `security_patch`, `android`, `build`, `incremental` และ `vbmeta_digest` เหมาะอย่างยิ่งสำหรับงานอัตโนมัติและเครื่องมือต่าง ๆ
- **Releases** - แต่ละไฟล์ `.prop` จะถูกแนบแยกต่างหาก (พร้อม `index.json`) กับ [release](https://github.com/VictorGabriel7Dev/build.prop/releases) ล่าสุด (ติดแท็ก `build-YYYYMMDD`)

`.prop` แต่ละไฟล์คือชุดคุณสมบัติฉบับเต็มที่จัดระเบียบแล้วสำหรับอุปกรณ์และ build นั้นโดยเฉพาะ - ทุกพาร์ทิชัน พร้อม `ro.boot.vbmeta.digest`

## 🗂️ What's inside

- **อุปกรณ์ Pixel รุ่นใหม่ทุกเครื่อง** (Pixel 6 ขึ้นไป)
- **สาม channel ต่ออุปกรณ์** - stable, beta และ canary ซึ่งเป็น build ล่าสุดของแต่ละอัน (ขึ้นอยู่กับสิ่งที่ Google เผยแพร่จริง อุปกรณ์ใหม่เอี่ยมบางเครื่องยังมีเพียงหนึ่งหรือสอง build บน canary)
- **`build.prop` ฉบับเต็ม** ต่อ build (~300-390 คุณสมบัติ) รวมจากทุกพาร์ทิชัน
- **`vbmeta.digest`** (hash ของ verified boot) ถูกเก็บไว้ข้างคุณสมบัติ

## 🔧 Build it yourself

หากต้องการแยกไฟล์ `.prop` ในเครื่องเองแทนการดาวน์โหลด คุณต้องมีสภาพแวดล้อมแบบ Unix (Linux หรือ macOS ที่มี Bash) พร้อมกับ `p7zip-full`, `e2fsprogs`, `erofs-utils`, `lz4`, `cpio`, `dos2unix`, `aria2`, `curl`, `xxd`, `jq` และ Python ≥3.8 พร้อม `payload_dumper` โดย `requirements.sh` จะติดตั้ง dependency เหล่านี้ผ่านตัวจัดการแพ็กเกจส่วนใหญ่ (apt, pacman, dnf, yum, zypper, apk, xbps, brew, Termux)

```bash
git clone --recurse-submodules https://github.com/VictorGabriel7Dev/build.prop && cd build.prop
./requirements.sh
./download_latest_ota_build.sh <device_name> [device_name ...]   # e.g. husky  |  cubs grizzly_beta
./extract_images.sh                                              # -> <codename>/<codename>_<build_id>.prop
```

อุปกรณ์ที่รองรับคืออิมเมจ factory และ OTA ที่อยู่บน [Google Android Images](https://developers.google.com/android/images) และ [หน้า Beta OTA](https://developer.android.com/about/versions/17/download-ota) การแยกไฟล์จะอ่านแต่ละพาร์ทิชันของ payload ทีละรายการ (ใช้หน่วยความจำต่ำ) และรองรับอิมเมจแบบ EROFS, ext4, sparse และ boot/init_boot

## 🤖 Automation

คลังเก็บจะเป็นปัจจุบันโดยอัตโนมัติ: เมื่อ Google เผยแพร่ build ใหม่ build เหล่านั้นจะถูกแยกออกมา (ฉบับเต็ม ทุกพาร์ทิชัน พร้อม `vbmeta.digest`) ไฟล์ `.prop` ใหม่จะถูก commit ไว้ภายใต้ `<codename>/` `index.json` จะถูกรีเฟรช และมีการสร้าง release ที่ระบุวันที่ (`build-YYYYMMDD`) เพื่อให้ผู้ติดตามได้รับแจ้งทุกระลอก

นอกจากนี้ยังมี `.github/workflows/build.yml` แบบทั่วไปที่เรียกใช้ตามคำสั่ง (`workflow_dispatch`) ให้ใช้เป็นทางสำรองแบบแมนนวลสำหรับการ build `.prop` ล่าสุดของอุปกรณ์หนึ่ง ๆ

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

`android` `pixel` `build-prop` `ota` `factory-image` `vbmeta` `system-properties` `build-properties` `automation`
