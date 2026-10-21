# 🌸 Arch Linux: Fluttershy Edition 🌸

[![Arch Linux](https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white)](https://archlinux.org)
[![Theme](https://img.shields.io/badge/Aesthetic-Fluttershy_Pastel_Pink_%26_Cream-FFB6C1?style=for-the-badge)](https://github.com/mak74ik/arch-fluttershy-edition)
[![ISO Builder](https://img.shields.io/badge/Archiso-Automated_CI%2FCD-00C853?style=for-the-badge)](https://github.com/mak74ik/arch-fluttershy-edition/actions)
[![License](https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge)](https://github.com/mak74ik/arch-fluttershy-edition/blob/main/LICENSE)

> *"Umm... if it's not too much trouble, welcome to my Arch Linux terminal! ...yay! ✿"*

An ultra-aesthetic, terminal-focused Arch Linux rice & bootable system distribution inspired by **Fluttershy** from *My Little Pony: Friendship is Magic*. Crafted with a calming pastel pink and buttercream palette, custom ASCII art, cute prompt indicators, seamless terminal configs (Kitty, Alacritty, Ghostty), Fastfetch styling, and a complete bootable **Archiso** profile.

---

```
          .---.
       ,-'     `-.               Arch Linux Fluttershy Edition
      /   .-^^^-.  \            ────────────────────────────────────
     /   /   ____ \  \           OS:        Arch Linux x86_64
    |   |   /    \ |  |          Theme:     Fluttershy Pastel Pink & Cream
    |   |  | (o)  (o) ||          Style:     Minimalist TUI / CLI Rice
     \   \  \   v   / /  /          Cursor:    Fluttershy-Pink
      `-. `---...---' .'           Quote:     "...yay! ✿"
         /          \             ────────────────────────────────────
        |   ƸӜƷ     |            ● ● ● ● ● ●
        |            |
        (____/\____)
```

---

## 🎨 Color Palette & Design Tokens

| Token | Hex | RGB | Description |
|---|---|---|---|
| **Mane Pastel Pink** | `#FFB6C1` | `rgb(255, 182, 193)` | Primary highlight, prompt accent, borders |
| **Rose Petal** | `#F4ACB7` | `rgb(244, 172, 183)` | Secondary accent, active tab, keybindings |
| **Buttercup Cream** | `#FFF9E6` | `rgb(255, 249, 230)` | Fluttershy coat, terminal background (light) |
| **Obsidian Plum** | `#1E1A24` | `rgb(30, 26, 36)` | Deep terminal background (dark mode) |
| **Aqua Teal** | `#80CED6` | `rgb(128, 206, 214)` | Cutie mark butterflies, eyes, special symbols |
| **Lavender Mist** | `#D8B4E2` | `rgb(216, 180, 226)` | Selection highlight, search matches |
| **Velvet Charcoal** | `#2E2A36` | `rgb(46, 42, 54)` | Foreground text (light mode) |
| **Soft Silk White** | `#FDFBF7` | `rgb(253, 251, 247)` | Foreground text (dark mode) |

---

## 🚀 Instant One-Line Install (On Any Arch Linux)

Apply the complete Fluttershy rice (Kitty, Alacritty, Fastfetch, Bash/Zsh, ASCII MOTD, and cursor) to your current system with a single command:

```bash
curl -sSL https://raw.githubusercontent.com/mak74ik/arch-fluttershy-edition/main/install.sh | bash
```

Or clone and run the interactive TUI configurator:

```bash
git clone https://github.com/mak74ik/arch-fluttershy-edition.git
cd arch-fluttershy-edition
chmod +x run.sh
./run.sh
```

---

## 💿 Bootable ISO: Download or Build

### 1. Download Pre-Built ISO
Every commit to `main` triggers a GitHub Actions workflow that builds the full bootable `archlinux-fluttershy-x86_64.iso` using official Archiso tooling.
- Head to [Releases / Actions](https://github.com/mak74ik/arch-fluttershy-edition/releases) to download the ready `.iso` image.
- Flash to a USB stick:
  ```bash
  sudo dd bs=4M if=archlinux-fluttershy-x86_64.iso of=/dev/sdX status=progress oflag=sync
  ```

### 2. Build Locally via Docker (Zero Setup Required)
If you have Docker installed on your machine:
```bash
./scripts/build-iso-docker.sh
```
This launches an official `archlinux:latest` container with `--privileged`, compiles the ISO, and outputs it to `./out/archlinux-fluttershy-x86_64.iso`.

### 3. Build Locally via Native Archiso
On any Arch Linux installation:
```bash
sudo pacman -S --needed archiso
sudo mkarchiso -v -w /tmp/archiso-tmp -o out archiso/
```

---

## 📁 Repository Structure

```
arch-fluttershy-edition/
├── ascii/                      # Fluttershy ASCII art & colorized ANSI banners
│   ├── fluttershy.txt          # Pure text ASCII
│   └── fluttershy_banner.py    # Python ANSI Truecolor generator
├── bin/
│   └── fluttershy-motd         # Shell startup MOTD script
├── configs/                    # Production terminal dotfiles
│   ├── alacritty/              # Alacritty config (alacritty.toml)
│   ├── bash/                   # Bash configuration (.bashrc)
│   ├── fastfetch/              # Fastfetch layout & ASCII logo
│   ├── ghostty/                # Ghostty modern terminal config
│   ├── kitty/                  # Kitty GPU terminal config
│   ├── starship/               # Starship pastel prompt
│   └── zsh/                    # Zsh prompt & aliases
├── cursor/                     # Custom cursor theme definition
│   └── index.theme             # Fluttershy-Pink cursor spec
├── archiso/                    # Declarative Archiso OS build profile
│   ├── profiledef.sh           # Archiso profile definition
│   ├── packages.x86_64         # Minimal & aesthetic package list
│   ├── pacman.conf             # Mirror & repository config
│   └── airootfs/               # Live root filesystem overlay
├── scripts/
│   ├── build-iso-docker.sh     # One-click Docker ISO builder
│   └── install-cursor.sh       # Cursor theme applicator
├── .github/workflows/
│   └── build-iso.yml           # Automated CI/CD Archiso build & release
├── main.py                     # Python TUI & CLI management utility
├── run.sh                      # Zero-dependency launcher
├── install.sh                  # One-line user installer
└── LICENSE                     # MIT License
```

---


---

## ⚙️ Системные требования / System Requirements

### 💻 Реальное железо (ПК / Ноутбук)
| Компонент | Минимум (Live CD) | Минимум (Установка на диск) | Рекомендуется |
|---|---|---|---|
| **Процессор** | 64-bit x86_64 (1 GHz) | 64-bit x86_64 (1 GHz) | 2.0+ GHz Multi-core |
| **ОЗУ (RAM)** | **1024 МБ (1 ГБ)** | **1536 МБ (1.5 ГБ)** | **4096 МБ (4 ГБ)** |
| **Диск (HDD/SSD)** | **0 ГБ** *(работает в RAM)* | **5 ГБ** | **10+ ГБ SSD** |
| **Флешка для записи** | USB 2.0 (>= 4 ГБ) | USB 2.0 (>= 4 ГБ) | USB 3.0+ (>= 8 ГБ) |
| **Режим загрузки** | UEFI или Legacy BIOS | UEFI или Legacy BIOS | UEFI (GPT) |

### 🖥️ Виртуальные машины (UTM / QEMU / VirtualBox / VMware)
| Параметр | Минимум (Live-запуск без установки) | Минимум (Установка в виртуалку) | Рекомендуется |
|---|---|---|---|
| **Режим на Apple Silicon (Mac M1/M2/M3/M4)** | **Emulate (x86_64)** | **Emulate (x86_64)** | **Emulate (x86_64)** |
| **Режим на Intel/AMD ПК** | **Virtualize (x86_64)** | **Virtualize (x86_64)** | **Virtualize (x86_64)** |
| **Ядра процессора (vCPU)** | 1 ядро | 1 ядро | 2–4 ядра |
| **ОЗУ виртуальной машины** | **1024 МБ (1 ГБ)** | **1536 МБ** | **2048–4096 МБ** |
| **Виртуальный диск** | **0 ГБ** *(диск не нужен, грузится с ISO)* | **5 ГБ** *(хватит под систему и TUI)* | **8–10 ГБ** |
| **Видеоадаптер** | VirtIO GPU / Standard VGA | VirtIO GPU / Standard VGA | VirtIO GPU |

> [!NOTE]
> **Хватит ли 5 ГБ хранилища?**
> - **Для Live-окружения (посмотреть, протестировать TUI и тему)**: виртуальный диск **не нужен вовсе (0 ГБ)** — вся система запускается напрямую в оперативную память из ISO.
> - **Для полноценной установки на виртуальный диск**: **5 ГБ достаточно** (установленная база с ядром, Kitty, Alacritty, Fastfetch и Python занимает около 3.1–3.4 ГБ, останется ~1.6 ГБ свободного места). Для долгосрочной работы без частой очистки кэша пакетов рекомендуется выделить 8–10 ГБ.

## 💖 Credits & Acknowledgments
- **Character Design**: Fluttershy belongs to Hasbro & *My Little Pony: Friendship is Magic* (created by Lauren Faust).
- **Arch Linux**: The Arch Linux team for the incredible distribution and `archiso` framework.
- **Crafted with love by**: Autonomous Auto Qwen AI (`mak74ik`).
