#!/usr/bin/env bash

set -euxo pipefail

echo "installing dependencies..."
python -m pip install --upgrade pip build hatch
python -m build

echo "done!"