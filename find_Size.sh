#!/bin/bash

get_size() {
	local way="$1"
	local size=$(du -hs "$way" 2>/dev/null |cut -f1)
	echo $size
}

items=$(ls -A)

for item in $items; do
	size=$(get_size "$item")
	echo -e "$size\t$item"
done | sort -rh -k1,1
