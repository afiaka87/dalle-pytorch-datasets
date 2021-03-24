#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

mkdir output;
cd output;

# Images
wget https://www.dropbox.com/s/dpqqewh7kum36vp/open_images_256.tar.gz;
tar xf open_images_256.tar.gz;
rm -rf open_images_256.tar.gz;

# Captions
wget https://www.dropbox.com/s/o33hxj3azn185sw/open_images_v6_captions_1.tar.gz;
tar xf open_images_v6_captions_1.tar.gz;
rm -rf open_images_v6_captions_1.tar.gz;


cd ../;
