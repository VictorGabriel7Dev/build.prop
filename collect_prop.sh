#!/bin/bash
# ======================================================================
#  PIXEL PROP BUILDER  ::  Pixel build.prop archive
#  Extract and distribute the full Pixel build.prop from Google's OTA images.
#
#  Copyright (C) 2026  VictorGabriel7Dev
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
#
# collect_prop.sh - collect the generated .prop into <codename>/<codename>_<build_id>.prop.

# Using util_functions.sh
[ -f "util_functions.sh" ] && . ./util_functions.sh || { echo "util_functions.sh not found" && exit 1; }

# Start processing directories (default to ./extracted_images)
process_directories "${BASH_SOURCE[0]}" "$1"

prop="$dir/system.prop"
[ -f "$prop" ] || { print_message "No system.prop in \"$dir\"" error && exit 1; }
content=$(cat "$prop")

codename=$(grep_prop "ro.product.vendor.name" "$content")
[ -z "$codename" ] && codename=$(grep_prop "ro.product.system.name" "$content")
# Directory = plain codename; filename prefix = PRODUCT (carries the track: cheetah_beta /
# cheetah_canary / cheetah for stable), so every prefix coexists and is self-describing.
product=$(grep_prop "ro.product.product.name" "$content")
[ -z "$product" ] && product="$codename"
# Name by INCREMENTAL (e.g. 16269273) to match the <product>_<incremental>.prop corpus;
# fall back to ro.build.id only if the incremental is missing.
build_id=$(grep_prop "ro.build.version.incremental" "$content")
[ -z "$build_id" ] && build_id=$(grep_prop "ro.build.id" "$content")
[ -z "$codename" ] || [ -z "$build_id" ] && { print_message "Missing codename/build_id in \"$dir\"" error && exit 1; }

out="${codename}/${product}_${build_id}.prop"
mkdir -p "${codename}"
{
  cat <<'EOF'
# ======================================================================
#  PIXEL PROP BUILDER  ::  Pixel build.prop archive
#  Extract and distribute the full Pixel build.prop from Google's OTA images.
#
#  Copyright (C) 2026  VictorGabriel7Dev
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

EOF
  cat "$prop"
} > "$out"
print_message "Prop saved to \"$out\"" info
