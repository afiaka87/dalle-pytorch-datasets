#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

aria2c https://academictorrents.com/download/470791483f8441764d3b01dbc4d22b3aa58ef46f.torrent; # food-101

mkdir output;

tar -xf food-101.tgz --directory=output;
rm food-101.tgz;
