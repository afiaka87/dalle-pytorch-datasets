#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

URL="https://www.dropbox.com/s/6ptycnlypb1psp7/wit_en_94k_256px.tar.gz"

wget $URL

