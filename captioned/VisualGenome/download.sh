#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

mkdir output;

TAR_DIR="VG_100K_2";

aria2c --split=4 --lowest-speed-limit=10K --parameterized-uri https://academictorrents.com/download/1bfe6871046860a2ff8c0cc1414318beb35dc916.torrent;

cd $TAR_DIR;

unzip -q images.zip;
rm -rf images.zip;

unzip -q images2.zip;
rm -rf images2.zip;

cd ../;
