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

# Using util_functions.sh
[ -f "util_functions.sh" ] && . ./util_functions.sh || { echo "util_functions.sh not found" && exit 1; }

# Start processing directories (default to ./extracted_images)
process_directories "${BASH_SOURCE[0]}" "$1"

# Define the props path
declare EXT_PROP_FILES=$(find_prop_files "$dir")

# Store the content of all prop files in a variable
declare EXT_PROP_CONTENT=$(cat $EXT_PROP_FILES)

# Building props config from there
system_prop=""
module_prop=""

###
# System Props
###

brand_for_attestation="$(grep_prop "ro.product.brand_for_attestation" "$EXT_PROP_CONTENT")"
[ -z "$brand_for_attestation" ] && brand_for_attestation="$(grep_prop "ro.product.vendor.brand" "$EXT_PROP_CONTENT")"
[ -z "$brand_for_attestation" ] && brand_for_attestation="$(grep_prop "ro.product.product.brand" "$EXT_PROP_CONTENT")"
[ -z "$brand_for_attestation" ] && brand_for_attestation="$(grep_prop "ro.product.system.brand" "$EXT_PROP_CONTENT")"

device_for_attestation="$(grep_prop "ro.product.device_for_attestation" "$EXT_PROP_CONTENT")"
[ -z "$device_for_attestation" ] && device_for_attestation="$(grep_prop "ro.product.vendor.device" "$EXT_PROP_CONTENT")"
[ -z "$device_for_attestation" ] && device_for_attestation="$(grep_prop "ro.product.product.device" "$EXT_PROP_CONTENT")"
[ -z "$device_for_attestation" ] && device_for_attestation="$(grep_prop "ro.product.system.device" "$EXT_PROP_CONTENT")"

manufacturer_for_attestation="$(grep_prop "ro.product.manufacturer_for_attestation" "$EXT_PROP_CONTENT")"
[ -z "$manufacturer_for_attestation" ] && manufacturer_for_attestation="$(grep_prop "ro.product.vendor.manufacturer" "$EXT_PROP_CONTENT")"
[ -z "$manufacturer_for_attestation" ] && manufacturer_for_attestation="$(grep_prop "ro.product.product.manufacturer" "$EXT_PROP_CONTENT")"
[ -z "$manufacturer_for_attestation" ] && manufacturer_for_attestation="$(grep_prop "ro.product.system.manufacturer" "$EXT_PROP_CONTENT")"

model_for_attestation="$(grep_prop "ro.product.model_for_attestation" "$EXT_PROP_CONTENT")"
[ -z "$model_for_attestation" ] && model_for_attestation="$(grep_prop "ro.product.vendor.model" "$EXT_PROP_CONTENT")"
[ -z "$model_for_attestation" ] && model_for_attestation="$(grep_prop "ro.product.product.model" "$EXT_PROP_CONTENT")"
[ -z "$model_for_attestation" ] && model_for_attestation="$(grep_prop "ro.product.system.model" "$EXT_PROP_CONTENT")"

name_for_attestation="$(grep_prop "ro.product.name_for_attestation" "$EXT_PROP_CONTENT")"
[ -z "$name_for_attestation" ] && name_for_attestation="$(grep_prop "ro.product.vendor.name" "$EXT_PROP_CONTENT")"
[ -z "$name_for_attestation" ] && name_for_attestation="$(grep_prop "ro.product.product.name" "$EXT_PROP_CONTENT")"
[ -z "$name_for_attestation" ] && name_for_attestation="$(grep_prop "ro.product.system.name" "$EXT_PROP_CONTENT")"

# Build our system.prop
to_system_prop "##
# Beautiful Pixel Props https://t.me/PixelProps
# By @T3SL4
##

###
#-#
###

###
# begin product/etc/build.prop
###

# begin common build properties"
add_prop_as_ini to_system_prop "ro.product.brand" "$brand_for_attestation"
add_prop_as_ini to_system_prop "ro.product.device" "$device_for_attestation"
add_prop_as_ini to_system_prop "ro.product.manufacturer" "$manufacturer_for_attestation"
add_prop_as_ini to_system_prop "ro.product.model" "$model_for_attestation"
add_prop_as_ini to_system_prop "ro.product.name" "$name_for_attestation"
build_system_prop "ro.product.product.brand"
build_system_prop "ro.product.product.device"
build_system_prop "ro.product.product.manufacturer"
build_system_prop "ro.product.product.model"
build_system_prop "ro.product.product.name"
build_system_prop "ro.product.brand_for_attestation"
build_system_prop "ro.product.device_for_attestation"
build_system_prop "ro.product.manufacturer_for_attestation"
build_system_prop "ro.product.model_for_attestation"
build_system_prop "ro.product.name_for_attestation"
build_system_prop "ro.product.build.date"
build_system_prop "ro.product.build.date.utc"
build_system_prop "ro.product.build.fingerprint"
build_system_prop "ro.product.build.id"
build_system_prop "ro.product.build.uuid"
build_system_prop "ro.product.build.tags"
build_system_prop "ro.product.build.type"
build_system_prop "ro.product.build.version.incremental"
build_system_prop "ro.product.build.version.release"
build_system_prop "ro.product.build.version.release_or_codename"
build_system_prop "ro.product.build.version.sdk"
to_system_prop "# end common build properties

# begin PRODUCT_PRODUCT_PROPERTIES"
build_system_prop "ro.opa.eligible_device"
build_system_prop "ro.com.google.clientidbase"
build_system_prop "ro.com.google.ime.theme_id"
build_system_prop "ro.com.google.ime.system_lm_dir"
build_system_prop "ro.support_one_handed_mode"
build_system_prop "ro.quick_start.oem_id"
build_system_prop "ro.quick_start.device_id"
to_system_prop "# end PRODUCT_PRODUCT_PROPERTIES

###
# end product/etc/build.prop
###

###
#-#
###

###
# begin system/etc/ramdisk/build.prop
###
"
build_system_prop "ro.product.bootimage.brand"
build_system_prop "ro.product.bootimage.device"
build_system_prop "ro.product.bootimage.manufacturer"
build_system_prop "ro.product.bootimage.model"
build_system_prop "ro.product.bootimage.name"
build_system_prop "ro.bootimage.build.date"
build_system_prop "ro.bootimage.build.date.utc"
build_system_prop "ro.bootimage.build.fingerprint"
build_system_prop "ro.bootimage.build.id"
build_system_prop "ro.bootimage.build.uuid"
build_system_prop "ro.bootimage.build.tags"
build_system_prop "ro.bootimage.build.type"
build_system_prop "ro.bootimage.build.version.incremental"
build_system_prop "ro.bootimage.build.version.release"
build_system_prop "ro.bootimage.build.version.release_or_codename"
build_system_prop "ro.bootimage.build.version.sdk"
to_system_prop "
###
# end system/etc/ramdisk/build.prop
###

###
#-#
###

###
# begin vendor/build.prop
###

# begin common build properties"
build_system_prop "ro.product.vendor.brand"
build_system_prop "ro.product.vendor.device"
build_system_prop "ro.product.vendor.manufacturer"
build_system_prop "ro.product.vendor.model"
build_system_prop "ro.product.vendor.name"
build_system_prop "ro.vendor.build.date"
build_system_prop "ro.vendor.build.date.utc"
build_system_prop "ro.vendor.build.fingerprint"
build_system_prop "ro.vendor.build.id"
build_system_prop "ro.vendor.build.uuid"
build_system_prop "ro.vendor.build.tags"
build_system_prop "ro.vendor.build.type"
build_system_prop "ro.vendor.build.version.incremental"
build_system_prop "ro.vendor.build.version.release"
build_system_prop "ro.vendor.build.version.release_or_codename"
build_system_prop "ro.vendor.build.version.sdk"
to_system_prop "# end common build properties

# begin PRODUCT_VENDOR_PROPERTIES"
build_system_prop "ro.soc.model"
build_system_prop "ro.soc.manufacturer"
# build_system_prop "ro.hardware.egl"
# build_system_prop "ro.hardware.vulkan"
to_system_prop "# end PRODUCT_VENDOR_PROPERTIES

# begin ADDITIONAL_VENDOR_PROPERTIES"
build_system_prop "ro.product.first_api_level"
build_system_prop "ro.vendor.build.security_patch"
# build_system_prop "ro.product.board"
# build_system_prop "ro.board.platform"
# add_prop_as_ini to_system_prop "ro.hardware" "$device_for_attestation"
to_system_prop "# end ADDITIONAL_VENDOR_PROPERTIES

# begin PRODUCT_PROPERTY_OVERRIDES"
build_system_prop "keyguard.no_require_sim"
build_system_prop "debug.sf.enable_sdr_dimming"
build_system_prop "debug.sf.dim_in_gamma_in_enhanced_screenshots"
build_system_prop "ro.hardware.keystore_desede"
build_system_prop "ro.hardware.keystore"
build_system_prop "ro.hardware.gatekeeper"
build_system_prop "persist.vendor.enable.thermal.genl"
build_system_prop "ro.incremental.enable"
build_system_prop "ro.build.device_family"
# add_prop_as_ini to_system_prop "vendor.usb.product_string" "$model_for_attestation"
# add_prop_as_ini to_system_prop "bluetooth.device.default_name" "$model_for_attestation"
to_system_prop "# end PRODUCT_PROPERTY_OVERRIDES

###
# end vendor/build.prop
###

###
#-#
###

###
# begin vendor/odm/etc/build.prop
###

# begin common build properties"
build_system_prop "ro.product.odm.brand"
build_system_prop "ro.product.odm.device"
build_system_prop "ro.product.odm.manufacturer"
build_system_prop "ro.product.odm.model"
build_system_prop "ro.product.odm.name"
build_system_prop "ro.odm.build.date"
build_system_prop "ro.odm.build.date.utc"
build_system_prop "ro.odm.build.fingerprint"
build_system_prop "ro.odm.build.id"
build_system_prop "ro.odm.build.uuid"
build_system_prop "ro.odm.build.tags"
build_system_prop "ro.odm.build.type"
build_system_prop "ro.odm.build.version.incremental"
build_system_prop "ro.odm.build.version.release"
build_system_prop "ro.odm.build.version.release_or_codename"
build_system_prop "ro.odm.build.version.sdk"
to_system_prop "# end common build properties

###
# end vendor/odm/etc/build.prop
###

###
# begin vendor/odm_dlkm/etc/build.prop
###

# begin common build properties"
build_system_prop "ro.product.odm_dlkm.brand"
build_system_prop "ro.product.odm_dlkm.device"
build_system_prop "ro.product.odm_dlkm.manufacturer"
build_system_prop "ro.product.odm_dlkm.model"
build_system_prop "ro.product.odm_dlkm.name"
build_system_prop "ro.odm_dlkm.build.date"
build_system_prop "ro.odm_dlkm.build.date.utc"
build_system_prop "ro.odm_dlkm.build.fingerprint"
build_system_prop "ro.odm_dlkm.build.id"
build_system_prop "ro.odm_dlkm.build.uuid"
build_system_prop "ro.odm_dlkm.build.tags"
build_system_prop "ro.odm_dlkm.build.type"
build_system_prop "ro.odm_dlkm.build.version.incremental"
build_system_prop "ro.odm_dlkm.build.version.release"
build_system_prop "ro.odm_dlkm.build.version.release_or_codename"
build_system_prop "ro.odm_dlkm.build.version.sdk"
to_system_prop "# end common build properties

###
# end vendor/odm_dlkm/etc/build.prop
###

###
#-#
###

###
# begin vendor_dlkm/etc/build.prop
###

# begin common build properties"
build_system_prop "ro.product.vendor_dlkm.brand"
build_system_prop "ro.product.vendor_dlkm.device"
build_system_prop "ro.product.vendor_dlkm.manufacturer"
build_system_prop "ro.product.vendor_dlkm.model"
build_system_prop "ro.product.vendor_dlkm.name"
build_system_prop "ro.vendor_dlkm.build.date"
build_system_prop "ro.vendor_dlkm.build.date.utc"
build_system_prop "ro.vendor_dlkm.build.fingerprint"
build_system_prop "ro.vendor_dlkm.build.id"
build_system_prop "ro.vendor_dlkm.build.uuid"
build_system_prop "ro.vendor_dlkm.build.tags"
build_system_prop "ro.vendor_dlkm.build.type"
build_system_prop "ro.vendor_dlkm.build.version.incremental"
build_system_prop "ro.vendor_dlkm.build.version.release"
build_system_prop "ro.vendor_dlkm.build.version.release_or_codename"
build_system_prop "ro.vendor_dlkm.build.version.sdk"
to_system_prop "# end common build properties

###
# end vendor_dlkm/etc/build.prop
###

###
#-#
###

###
# begin system/system/build.prop
###

# begin common build properties"
build_system_prop "ro.product.system.brand"
build_system_prop "ro.product.system.device"
build_system_prop "ro.product.system.manufacturer"
build_system_prop "ro.product.system.model"
build_system_prop "ro.product.system.name"
build_system_prop "ro.system.build.date"
build_system_prop "ro.system.build.date.utc"
build_system_prop "ro.system.build.fingerprint"
build_system_prop "ro.system.build.id"
build_system_prop "ro.system.build.uuid"
build_system_prop "ro.system.build.tags"
build_system_prop "ro.system.build.type"
build_system_prop "ro.system.build.version.incremental"
build_system_prop "ro.system.build.version.release"
build_system_prop "ro.system.build.version.release_or_codename"
build_system_prop "ro.system.build.version.sdk"
to_system_prop "# end common build properties

# begin build properties"
add_prop_as_ini to_system_prop "ro.build.fingerprint" "$(grep_prop "ro.system.build.fingerprint" "$EXT_PROP_CONTENT")"
build_system_prop "ro.build.id"
build_system_prop "ro.build.uuid"
build_system_prop "ro.build.display.id"
# build_system_prop "ro.build.product"
build_system_prop "ro.build.description"
build_system_prop "ro.build.version.incremental"
build_system_prop "ro.build.version.sdk"
build_system_prop "ro.build.version.release"
build_system_prop "ro.build.version.release_or_codename"
build_system_prop "ro.build.version.security_patch"
build_system_prop "ro.build.date"
build_system_prop "ro.build.date.utc"
build_system_prop "ro.build.type"
build_system_prop "ro.build.user"
build_system_prop "ro.build.host"
build_system_prop "ro.build.tags"
build_system_prop "ro.build.flavor"
to_system_prop "# end build properties

# begin PRODUCT_SYSTEM_PROPERTIES"
build_system_prop "ro.hotword.detection_service_required"
to_system_prop "#end PRODUCT_SYSTEM_PROPERTIES

###
# end system/system/build.prop
###

###
#-#
###

###
# begin system_ext/etc/build.prop
###

# begin common build properties"
build_system_prop "ro.product.system_ext.brand"
build_system_prop "ro.product.system_ext.device"
build_system_prop "ro.product.system_ext.manufacturer"
build_system_prop "ro.product.system_ext.model"
build_system_prop "ro.product.system_ext.name"
build_system_prop "ro.system_ext.build.date"
build_system_prop "ro.system_ext.build.date.utc"
build_system_prop "ro.system_ext.build.fingerprint"
build_system_prop "ro.system_ext.build.id"
build_system_prop "ro.system_ext.build.uuid"
build_system_prop "ro.system_ext.build.tags"
build_system_prop "ro.system_ext.build.type"
build_system_prop "ro.system_ext.build.version.incremental"
build_system_prop "ro.system_ext.build.version.release"
build_system_prop "ro.system_ext.build.version.release_or_codename"
build_system_prop "ro.system_ext.build.version.sdk"
to_system_prop "# end common build properties

###
# end system_ext/etc/build.prop
###

###
# begin system_dlkm/etc/build.prop
###

# begin common build properties"
build_system_prop "ro.product.system_dlkm.brand"
build_system_prop "ro.product.system_dlkm.device"
build_system_prop "ro.product.system_dlkm.manufacturer"
build_system_prop "ro.product.system_dlkm.model"
build_system_prop "ro.product.system_dlkm.name"
build_system_prop "ro.system_dlkm.build.date"
build_system_prop "ro.system_dlkm.build.date.utc"
build_system_prop "ro.system_dlkm.build.fingerprint"
build_system_prop "ro.system_dlkm.build.id"
build_system_prop "ro.system_dlkm.build.uuid"
build_system_prop "ro.system_dlkm.build.tags"
build_system_prop "ro.system_dlkm.build.type"
build_system_prop "ro.system_dlkm.build.version.incremental"
build_system_prop "ro.system_dlkm.build.version.release"
build_system_prop "ro.system_dlkm.build.version.release_or_codename"
build_system_prop "ro.system_dlkm.build.version.sdk"
to_system_prop "# end common build properties

###
# end system_dlkm/etc/build.prop
###

###
# begin of custom props
###

# begin common build properties"
add_prop_as_ini to_system_prop "ro.boot.hwname" "$device_for_attestation"
add_prop_as_ini to_system_prop "ro.boot.hwdevice" "$device_for_attestation"
add_prop_as_ini to_system_prop "ro.product.hardware.sku" "$device_for_attestation"
add_prop_as_ini to_system_prop "ro.boot.product.hardware.sku" "$device_for_attestation"
to_system_prop "# end common build properties

###
# end of custom props
###"

# Save the system.prop file
echo -n "${system_prop::-1}" >"$dir/system.prop"

###
# Module Props
###
device_name=$model_for_attestation
device_build_description=$(grep_prop "ro.build.description" "$EXT_PROP_CONTENT")
device_codename=$(grep_prop "ro.product.vendor.name" "$EXT_PROP_CONTENT")
device_build_security_patch=$(grep_prop "ro.vendor.build.security_patch" "$EXT_PROP_CONTENT")
device_build_fingerprint=$(grep_prop "ro.product.build.id" "$EXT_PROP_CONTENT")
device_build_id=$(grep_prop "ro.build.id" "$EXT_PROP_CONTENT")
base_name="${device_codename}_$device_build_id"

# (module.prop generation removed: this fork distributes the raw Pixel build.prop files, not
# installable modules. No module metadata, no third-party description/donate/support strings.)

# Display information about prop
print_message "Built props for $device_name [$device_build_description]!" info

# Display saving location
print_message "Props saved to \"${dir}\"" debug
