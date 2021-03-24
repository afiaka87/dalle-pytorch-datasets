#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

mkdir output;
mkdir download;

aria2c --split=4 --lowest-speed-limit=10K --parameterized-uri https://academictorrents.com/download/1bfe6871046860a2ff8c0cc1414318beb35dc916.torrent;

unzip -q ./download/images.zip
unzip -q ./download/images2.zip
