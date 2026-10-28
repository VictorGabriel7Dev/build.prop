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

# Using requirements.sh
[ -f "requirements.sh" ] && . ./requirements.sh || { echo "requirements.sh not found" && exit 1; }

# Extracted image paths
EI="./extracted_images"
EAI="./extracted_archive_images"
EI_BP="${EI##"./"}"
EAI_BP="${EAI##"./"}"

# Extract payload as ota or system image if factory
[ -d "dl" ] && print_message "Extracting images from the Android OTA update package or factory image…\n" info
for file in ./dl/*; do                                      # Iterate through files in the directory ./dl/*
	if [ -f "${file:?}" ] && [ "${file: -4}" == ".zip" ]; then # Check if it is a ZIP file
		filename="${file##*/}"                                    # Extract the filename (remove the path)
		basename="${filename%.*}"                                 # Extract the basename (remove the extension)
		# devicename="${basename%%-*}"                              # Extract the device name (remove the extension)
		print_message "Processing \"$filename\"…" info

		# Time the extraction
		extraction_start=$(date +%s)

		# Extract images
		if unzip -l "$file" | grep -q "payload.bin"; then
			print_message "Extracting OTA image…" debug

			# Skip image if it failed to get extracted
			if ! 7z e "$file" -o"$EAI" "payload.bin" -r &>/dev/null; then
				print_message "Failed to extract payload.bin from $file using 7z. Skipping…\n" warning
				continue
			fi

			# If it managed to dump the payload then move it correspondingly.
			mv -f "$EAI_BP/payload.bin" "$EAI/$basename.bin"
			print_message "Saved to \"$EAI/$basename.bin\"." debug
		else
			print_message "Detected Factory image, Extracting everything…" debug

			# Skip image if it failed to get extracted
			if ! 7z e "$file" -o"$EAI_BP" -r -y &>/dev/null; then
				print_message "Failed to extract everything from $file. Skipping…" warning
				continue
			fi
		fi

		# We dont need the downloaded archive image anymore
		rm "$file"

		# Time the extraction
		extraction_end=$(date +%s)
		extraction_runtime=$((extraction_end - extraction_start))

		# Print the time
		print_message "Extraction time: $extraction_runtime seconds\n" debug
	fi
done

if [ -d "$EAI_BP" ]; then
	if [ -n "$(ls -A "$EAI_BP"/*.{zip,bin} 2>/dev/null)" ]; then
		print_message "Dumping images from \"$EAI_BP\"…\n" info

		for file in "$EAI"/*.{zip,bin}; do                                         # List directory zip & bin files
			if [ -f "${file:?}" ] && [[ "$file" == *.zip || "$file" == *.bin ]]; then # Check if file is a zip or bin file
				filename="${file##*/}"                                                   # Remove the path
				basename="${filename%.*}"                                                # Remove the extension
				print_message "Processing \"$filename\"…" info

				# Time the extraction
				extraction_start=$(date +%s)

			    # Extract/Dump
				if [ "${file: -4}" == ".bin" ]; then # If is payload use the Android OTA Dumper
					# Dump one partition at a time to keep memory usage low
					for image_name in "${PARTITIONS2EXTRACT[@]}"; do
						print_message "Dumping \"$image_name\" from payload…" debug

						if ! payload_dumper "$file" --partitions="$image_name" --out="$EI_BP/$basename" 2>/dev/null; then
							print_message "Failed to extract $image_name from $file using Android OTA Dumper. Skipping…" warning
							rm -f "$EI_BP/$basename/$image_name.img"
							continue
						fi
					done
				else # Else directly extract all the required image using 7z
					for image_name in "${PARTITIONS2EXTRACT[@]}"; do
						print_message "Extracting \"$image_name\"…" debug

						# Skip image if it failed to get extracted
						if ! 7z e "$file" -o"$EI_BP/$basename" "$image_name.img" -r &>/dev/null; then
							print_message "Failed to extract $image_name.img from $file using 7z. Skipping…\n" warning
							rm -rf "$EI_BP/$basename/$image_name.img"
							continue
						fi
					done
				fi

				# We dont need the image anymore
				rm "$file"

				# Time the extraction
				extraction_end=$(date +%s)
				extraction_runtime=$((extraction_end - extraction_start))

				# Print the time
				print_message "Extraction time: $extraction_runtime seconds\n" debug
			fi
		done
	else
		print_message "The directory \"$EAI_BP\" does not have any ZIP or BIN files.\n" warning
	fi
fi

# Extract the images directories
[ -d "$EI" ] && print_message "Extracting images…\n" info

# Sanity check: if we have nothing in extracted_images and nothing in extracted_archive_images, abort
if [ ! -d "$EI" ] || [ -z "$(ls -A "$EI" 2>/dev/null)" ]; then
  print_message "No extracted images in \"$EI_BP\" and no archives in \"$EAI_BP\". Nothing to process.\n" error
fi

for dir in "$EI"/*; do  # List directory ./*
	if [ -d "$dir" ]; then # Check if it is a directory
		dir=${dir%*/}         # Remove last /
		print_message "Processing \"${dir##*/}\"…" info

		# Time the extraction
		extraction_start=$(date +%s)

		# Extract all and clean
		for image_name in "${PARTITIONS2EXTRACT[@]}"; do
			if [ -f "$dir/$image_name.img" ]; then
				extract_image "$dir" "$image_name"
			fi
		done

		# Time the extraction
		extraction_end=$(date +%s)
		extraction_runtime=$((extraction_end - extraction_start))

		# Print the extraction time
		print_message "Extraction time: $extraction_runtime seconds\n" debug
	fi
done

# Build props and collect .prop files after extraction
[ -d "$EI" ] && print_message "Building props and collecting .prop files…\n" info
for dir in "$EI"/*; do  # List directory ./*
	if [ -d "$dir" ]; then # Check if it is a directory
		dir=${dir%*/}         # Remove last /
		print_message "Processing \"${dir##*/}\"…" info

		# Time the extraction
		extraction_start=$(date +%s)

		# Build system.prop (the full, organized .prop with all partitions)
		print_message "Building props…" info
		./build_props.sh "$dir"

		# Collect the .prop file (module building removed; this repo distributes .prop)
		print_message "Collecting .prop…" info
		./collect_prop.sh "$dir"

		# Time the extraction
		extraction_end=$(date +%s)
		extraction_runtime=$((extraction_end - extraction_start))

		# Print the build time
		print_message "Build time: $extraction_runtime seconds\n" debug
	fi
done
