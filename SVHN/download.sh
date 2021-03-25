#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

mkdir output;

aria2c https://academictorrents.com/download/6f4caf3c24803d114c3cae3ab9cb946cd23c7213.torrent; # SVHN

# extracting SVHN
for i in extra.tar.gz test.tar.gz train.tar.gz
do 
	echo "Untarring: $i";
	tar -xf $i --directory=output;
done

