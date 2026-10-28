#!/bin/bash
# Collect the generated .prop into props/<codename>/<codename>_<build_id>.prop
# (this repo distributes .prop files, not installable Magisk modules).

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

out="props/${codename}/${codename}_${build_id}.prop"
mkdir -p "props/${codename}"
cp -f "$prop" "$out"
print_message "Prop saved to \"$out\"" info
