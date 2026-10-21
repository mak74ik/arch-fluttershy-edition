#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

chmod +x main.py bin/* scripts/* 2>/dev/null || true

python3 main.py "$@"
