#!/usr/bin/env bash
set -e
ICON_DIR="${HOME}/.icons/Fluttershy-Pink"
mkdir -p "$ICON_DIR"
cat << 'EOF' > "$ICON_DIR/index.theme"
[Icon Theme]
Name=Fluttershy-Pink
Comment=Pastel pink and white gentle cursor theme
Inherits=Adwaita
EOF

mkdir -p "${HOME}/.icons/default"
cat << 'EOF' > "${HOME}/.icons/default/index.theme"
[Icon Theme]
Name=default
Inherits=Fluttershy-Pink
EOF

echo "✓ Fluttershy cursor theme registered in ~/.icons"
