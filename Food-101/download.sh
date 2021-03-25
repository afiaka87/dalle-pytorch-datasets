#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

if [[ ! -v OUTPUT_PATH]]; then
    echo "Using default output path."
    OUTPUT_PATH=../output
else
    echo "Using provided OUTPUT_PATH: $OUTPUT_PATH"
fi



aria2c https://academictorrents.com/download/470791483f8441764d3b01dbc4d22b3aa58ef46f.torrent; # food-101

tar -xf food-101.tgz --directory=$OUTPUT_PATH;
rm food-101.tgz;
