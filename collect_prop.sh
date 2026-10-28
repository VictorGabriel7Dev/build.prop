#!/bin/bash
#
# collect_prop.sh - collect the generated .prop into <codename>/<codename>_<build_id>.prop.
# This repo distributes .prop files (not installable modules); each file carries the
# project header below.
#
# Pixel Prop Builder - https://github.com/VictorGabriel7Dev/build.prop
# Site: https://victorgabriel.dev | GitHub: @VictorGabriel7Dev | E-mail: contato@victorgabriel.dev

# Using util_functions.sh
[ -f "util_functions.sh" ] && . ./util_functions.sh || { echo "util_functions.sh not found" && exit 1; }

# Start processing directories (default to ./extracted_images)
process_directories "${BASH_SOURCE[0]}" "$1"

prop="$dir/system.prop"
[ -f "$prop" ] || { print_message "No system.prop in \"$dir\"" error && exit 1; }
content=$(cat "$prop")

codename=$(grep_prop "ro.product.vendor.name" "$content")
[ -z "$codename" ] && codename=$(grep_prop "ro.product.system.name" "$content")
build_id=$(grep_prop "ro.build.id" "$content")
[ -z "$codename" ] || [ -z "$build_id" ] && { print_message "Missing codename/build_id in \"$dir\"" error && exit 1; }

out="${codename}/${codename}_${build_id}.prop"
mkdir -p "${codename}"
{
  cat <<EOF
# Pixel Prop Builder  -  ${codename} build.prop (build ${build_id})
# Full build.prop extracted from the official Google OTA factory image.
#
# Project : https://github.com/VictorGabriel7Dev/build.prop
# Site    : https://victorgabriel.dev
# GitHub  : @VictorGabriel7Dev https://github.com/VictorGabriel7Dev
# Telegram: @VictorGabriel_Dev https://t.me/VictorGabriel_Dev
# Discord : @VictorGabriel.dev https://discord.com/users/1481407654458036265
# LinkedIn: in/victorgabriel-dev https://www.linkedin.com/in/victorgabriel-dev
# Instagram: @VictorGabriel_Dev https://www.instagram.com/VictorGabriel_Dev
# WhatsApp: @VictorGabriel_Dev https://wa.me/@VictorGabriel_Dev
# E-mail  : contato@victorgabriel.dev
#
EOF
  cat "$prop"
} > "$out"
print_message "Prop saved to \"$out\"" info
