#!/bin/bash

# Enable strict mode.
set -euo pipefail;
IFS=$'\n\t';

if [[ ! -v OUTPUT_PATH ]]; then
    echo "Using default output path."
    OUTPUT_PATH=../output;
else
    echo "Using provided OUTPUT_PATH: $OUTPUT_PATH"
fi

mkdir -p $OUTPUT_PATH
cd $OUTPUT_PATH

ZIP_DIR="VG_100K_2";

aria2c --split=4 --lowest-speed-limit=10K --parameterized-uri https://academictorrents.com/download/1bfe6871046860a2ff8c0cc1414318beb35dc916.torrent;

mv $ZIP_DIR/ $OUTPUT_PATH

unzip -q images.zip;
rm -rf images.zip;

unzip -q images2.zip;
rm -rf images2.zip;


wget -q "http://visualgenome.org/static/data/dataset/region_descriptions.json.zip";
unzip -q region_descriptions.json.zip;
mv region_descriptions.json $OUTPUT_PATH;


