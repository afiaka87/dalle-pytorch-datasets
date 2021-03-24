#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

wget https://www.dropbox.com/s/ge29pmic7blwkkv/urls_en.tar.gz;

tar -xf url.en.tar.gz;
cd url;
cat *.txt > all_urls.txt;
mkdir OUTPUT;
aria2c --auto-file-renaming false --conditional-get --no-file-allocation-limit=1K -P true --deferred-input true --optimize-concurrent-downloads -i ./all_urls.txt -d ./OUTPUT;
