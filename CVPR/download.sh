#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

aria2c https://academictorrents.com/download/59aa0ad684e5d849f68bad9a6d43a9000a927164.torrent; # indoor CVPR


mkdir output;

#tar -xf food-101.tgz --directory=output; 
# extract indoorCVPR
tar -xf indoorCVPR_09.tar --directory=output;
rm indoorCVPR_09.tar;
mv output/Images/ indoorCVPR/; # change the name to correct dataset folder
