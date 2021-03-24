#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

wget https://www.dropbox.com/s/dtjjz9cpenmpowr/train2017.zip;
unzip -q train2017.zip;
