#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

mkdir output;

aria2c https://academictorrents.com/download/a799a2845ac29a66c07cf74e2a2838b6c5698a6a.torrent; # STL-10


# extract STL-10
tar -xf stl10_binary.tar.gz --directory=output;
