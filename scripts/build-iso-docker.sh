#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

echo "🌸 Building Arch Linux Fluttershy Edition ISO via Docker Container..."
mkdir -p out

docker run --rm --privileged \
  -v "${DIR}:/workspace" \
  -w /workspace \
  archlinux:latest bash -c "
    echo '==> Refreshing Arch Linux keyring and installing archiso...'
    pacman -Sy --noconfirm archlinux-keyring
    pacman -S --noconfirm archiso
    echo '==> Running mkarchiso...'
    mkarchiso -v -w /tmp/archiso-tmp -o /workspace/out /workspace/archiso
    echo '==> Build completed! Calculating SHA256 checksum...'
    cd /workspace/out && sha256sum archlinux-fluttershy-*.iso > sha256.txt
    echo '==> ISO Image ready in out/ directory.'
"
