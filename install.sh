#!/usr/bin/env bash
set -e

C_PINK="\033[38;2;255;182;193m"
C_CYAN="\033[38;2;128;206;214m"
C_CREAM="\033[38;2;255;249;230m"
C_RESET="\033[0m"
C_BOLD="\033[1m"

echo -e "${C_PINK}${C_BOLD}"
echo "    🌸 Arch Linux: Fluttershy Edition Installer 🌸"
echo "    ─────────────────────────────────────────────"
echo -e "${C_RESET}"

REPO_URL="https://github.com/mak74ik/arch-fluttershy-edition.git"
INSTALL_DIR="${HOME}/.local/share/arch-fluttershy-edition"

if [ -d "$INSTALL_DIR" ]; then
    echo -e "${C_CYAN}➜ Updating existing repository in $INSTALL_DIR...${C_RESET}"
    cd "$INSTALL_DIR" && git pull --quiet
else
    echo -e "${C_CYAN}➜ Cloning repository to $INSTALL_DIR...${C_RESET}"
    git clone --quiet "$REPO_URL" "$INSTALL_DIR"
fi

cd "$INSTALL_DIR"
chmod +x run.sh main.py scripts/* bin/* 2>/dev/null || true

echo -e "${C_CYAN}➜ Deploying Fluttershy terminal configurations...${C_RESET}"
python3 main.py --install

echo -e "${C_CYAN}➜ Setting up cursor theme...${C_RESET}"
./scripts/install-cursor.sh 2>/dev/null || true

echo -e "\n${C_PINK}${C_BOLD}✨ Fluttershy Edition successfully installed! ...yay! ✿${C_RESET}"
echo -e "Open a new terminal window or run ${C_CREAM}fastfetch${C_RESET} to enjoy your new rice.\n"
