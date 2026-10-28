#!/bin/bash
# ======================================================================
#  PIXEL PROP BUILDER  ::  Pixel build.prop archive
#  Extract and distribute the full Pixel build.prop from Google's OTA images.
#
#  Copyright (C) 2026  @T3SL4 & VictorGabriel7Dev
#  SPDX-License-Identifier: GPL-3.0-or-later
#  Fork of Pixel-Props/build.prop by @T3SL4.
#
#  Free software under the GNU GPL v3 or later: distribute a modified
#  version and you MUST offer its source under the same terms.
#
#  Site      : https://victorgabriel.dev
#  Source    : https://github.com/VictorGabriel7Dev/build.prop
#  GitHub    : @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
#  Telegram  : @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
#  Discord   : @VictorGabriel.dev https://discord.com/users/1481407654458036265
#  LinkedIn  : in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
#  Instagram : @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
#  WhatsApp  : @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
#  E-mail    : contato@victorgabriel.dev
# ======================================================================

# Only run requirements check once per shell session
[ -n "$PIXEL_PROPS_REQS_DONE" ] && return 0
PIXEL_PROPS_REQS_DONE=1

# Those are the only partitions we need for building properties
declare PARTITIONS2EXTRACT=("product" "vendor" "vendor_dlkm" "system" "system_ext" "system_dlkm" "init_boot")

[[ $(type -t "print_message") != function ]] && . ./util_functions.sh

# Install required packages and libs
install_packages "zip" "p7zip" "erofs-utils" "lz4" "cpio" "dos2unix" "aria2"

# Check whethever python was installed, TODO: Improve install_packages function.
if ! command -v python3 >/dev/null 2>&1; then
	install_packages "python3"
fi

# Check if python3 pip module installed
python3 -m pip -V &>/dev/null || print_message "Could not find pip module in python3, To fix this issue simply aria2c and install https://bootstrap.pypa.io/get-pip.py from python3" error

# Check if payload_dumper is available
payload_dumper -h &>/dev/null || print_message "Could not find payload_dumper executable. Install it using python3 -m pip install payload_dumper/" error

# Install unpack_bootimg if not already installed
while [ ! -f "./unpack_bootimg.py" ]; do
	print_message "./unpack_bootimg.py not found. installing…" info
	aria2c -q "https://android.googlesource.com/platform/system/tools/mkbootimg/+/refs/heads/master/unpack_bootimg.py?format=TEXT" -o unpack.b64 && base64 -d unpack.b64 > unpack_bootimg.py && rm unpack.b64
    chmod +x unpack_bootimg.py
done
