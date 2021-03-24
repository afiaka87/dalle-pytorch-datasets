#!/bin/bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

wget https://www.dropbox.com/s/yxibearxqgkh58k/conceptual_captions_train_256.zip;
unzip -q conceptual_captions_train_256.zip;
