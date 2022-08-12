#!/bin/sh

DEBIAN_FRONTEND=noninteractive
sudo apt-get update
sudo apt-get install -y --no-install-recommends apt-utils dialog dnsutils httpie wget unzip curl jq
DEBIAN_FRONTEND=dialog

curl -sSL https://install.python-poetry.org | python -
go install github.com/rhysd/actionlint/cmd/actionlint@latest
poetry install
poetry run pre-commit install