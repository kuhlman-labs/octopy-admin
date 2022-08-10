#!/bin/sh

DEBIAN_FRONTEND=noninteractive
sudo apt-get update
sudo apt-get install -y --no-install-recommends apt-utils dialog dnsutils httpie wget unzip curl jq
DEBIAN_FRONTEND=dialog

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -