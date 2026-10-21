#!/usr/bin/env python3
"""
Arch Linux Fluttershy Edition - CLI & TUI Rice Manager
Provides theme switching, ASCII banner previews, color palette inspection,
and configuration deployment.
"""

import os
import sys
import argparse
import shutil
import time

VERSION = "1.0.0"

# ANSI TrueColor sequences
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_DIM = "\033[2m"
C_PINK = "\033[38;2;255;182;193m"       # Mane Pastel Pink (#FFB6C1)
C_ROSE = "\033[38;2;244;172;183m"       # Rose Petal (#F4ACB7)
C_CREAM = "\033[38;2;255;249;230m"      # Buttercup Cream (#FFF9E6)
C_CYAN = "\033[38;2;128;206;214m"       # Aqua Teal (#80CED6)
C_WHITE = "\033[38;2;253;251;247m"      # Soft White (#FDFBF7)
C_MUTED = "\033[38;2;180;170;185m"      # Lavender Muted (#B4AAB9)
C_PLUM = "\033[38;2;46;42;54m"          # Velvet Plum (#2E2A36)

ASCII_BANNER = f"""{C_PINK}
          .---.
       ,-'     `-.               {C_BOLD}{C_PINK}Arch Linux{C_RESET} {C_WHITE}Fluttershy Edition{C_RESET}
      /   {C_ROSE}.-^^^-.{C_PINK}  \\            {C_MUTED}────────────────────────────────────{C_RESET}
     /   /   {C_CREAM}____{C_PINK} \\  \\           {C_CYAN}OS:{C_RESET}        {C_WHITE}Arch Linux x86_64{C_RESET}
    |   |   {C_CREAM}/    \\{C_PINK} |  |          {C_CYAN}Theme:{C_RESET}     {C_PINK}Pastel Pink & Butter Cream{C_RESET}
    |   |  {C_CREAM}| {C_CYAN}(o){C_CREAM}  {C_CYAN}(o){C_CREAM} |{C_PINK} |          {C_CYAN}Pony:{C_RESET}      {C_CREAM}Fluttershy (Pegasus){C_RESET}
     \\   \\  {C_CREAM}\\   {C_ROSE}v{C_CREAM}   /{C_PINK} /  /          {C_CYAN}Cursor:{C_RESET}    {C_PINK}Fluttershy-Pink{C_RESET}
      `-. `{C_ROSE}---...---{C_PINK}' .'           {C_CYAN}Motto:{C_RESET}     {C_WHITE}"...yay! ✿"{C_RESET}
{C_CREAM}         /          \\{C_RESET}             {C_MUTED}────────────────────────────────────{C_RESET}
{C_CREAM}        |   {C_CYAN}ƸӜƷ{C_CREAM}     |{C_RESET}            {C_PINK}●{C_RESET} {C_ROSE}●{C_RESET} {C_CREAM}●{C_RESET} {C_CYAN}●{C_RESET} {C_WHITE}●{C_RESET} {C_MUTED}●{C_RESET}
{C_CREAM}        |            |{C_RESET}
{C_CREAM}        (____/\\____){C_RESET}
"""

def print_banner():
    print(ASCII_BANNER)

def print_palette():
    print(f"\n{C_BOLD}🌸 Fluttershy Aesthetic Design Palette:{C_RESET}\n")
    tokens = [
        ("Mane Pastel Pink", "#FFB6C1", C_PINK, "Primary accent, prompt, highlights"),
        ("Rose Petal", "#F4ACB7", C_ROSE, "Secondary accent, active tab, warnings"),
        ("Buttercup Cream", "#FFF9E6", C_CREAM, "Fluttershy coat, light background"),
        ("Aqua Teal", "#80CED6", C_CYAN, "Cutie mark butterflies, links, info"),
        ("Soft Silk White", "#FDFBF7", C_WHITE, "Dark mode text, clean contrast"),
        ("Lavender Muted", "#B4AAB9", C_MUTED, "Inactive tabs, comments, timestamps"),
        ("Velvet Obsidian", "#1E1A24", C_PLUM, "Dark terminal background")
    ]
    for name, hex_c, ansi_c, desc in tokens:
        swatch = f"{ansi_c}████████{C_RESET}"
        print(f"  {swatch}  {ansi_c}{name:<20}{C_RESET} {C_DIM}{hex_c:<10}{C_RESET}  {desc}")
    print()

def deploy_configs(target_dir=None, dry_run=False):
    base_src = os.path.dirname(os.path.abspath(__file__))
    configs_src = os.path.join(base_src, "configs")
    dest_base = target_dir or os.path.expanduser("~/.config")

    print(f"\n{C_BOLD}{C_PINK}🚀 Deploying Fluttershy Rice Configurations...{C_RESET}\n")
    mappings = [
        ("kitty/kitty.conf", os.path.join(dest_base, "kitty", "kitty.conf")),
        ("alacritty/alacritty.toml", os.path.join(dest_base, "alacritty", "alacritty.toml")),
        ("ghostty/config", os.path.join(dest_base, "ghostty", "config")),
        ("fastfetch/config.jsonc", os.path.join(dest_base, "fastfetch", "config.jsonc")),
        ("starship/starship.toml", os.path.join(dest_base, "starship.toml")),
    ]

    for src_rel, dst_path in mappings:
        full_src = os.path.join(configs_src, src_rel)
        if not os.path.exists(full_src):
            continue
        print(f"  {C_CYAN}➜{C_RESET} {src_rel:<28} -> {dst_path}")
        if not dry_run:
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            if os.path.exists(dst_path):
                backup_path = f"{dst_path}.bak.{int(time.time())}"
                shutil.copy2(dst_path, backup_path)
            shutil.copy2(full_src, dst_path)

    bashrc_path = os.path.expanduser("~/.bashrc")
    marker = "# === ARCH FLUTTERSHY MOTD ==="
    if not dry_run and os.path.exists(bashrc_path):
        with open(bashrc_path, "r", encoding="utf-8") as bf:
            content = bf.read()
        if marker not in content:
            with open(bashrc_path, "a", encoding="utf-8") as bf:
                bf.write(f"\n{marker}\n")
                bf.write(f'python3 "{os.path.join(base_src, "main.py")}" --ascii\n')
            print(f"  {C_CYAN}➜{C_RESET} Added startup MOTD to ~/.bashrc")

    print(f"\n{C_BOLD}{C_PINK}✨ All Fluttershy configurations applied successfully! ...yay! ✿{C_RESET}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Arch Linux Fluttershy Edition - Terminal Rice & ISO Suite"
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument("--ascii", action="store_true", help="Print Fluttershy ASCII art banner")
    parser.add_argument("--palette", action="store_true", help="Display aesthetic pastel color palette")
    parser.add_argument("--preview", action="store_true", help="Preview banner, palette and quotes")
    parser.add_argument("--install", action="store_true", help="Deploy dotfiles to current system")
    parser.add_argument("--dry-run", action="store_true", help="Simulate installation without changes")
    parser.add_argument("--theme", choices=["dark", "light"], default="dark", help="Color theme variant")

    args = parser.parse_args()

    if args.ascii:
        print_banner()
    elif args.palette:
        print_palette()
    elif args.preview:
        print_banner()
        print_palette()
    elif args.install:
        deploy_configs(dry_run=args.dry_run)
    else:
        print_banner()
        print(f"Run {C_CYAN}python3 main.py --help{C_RESET} to view available commands.")
        print(f"Run {C_CYAN}python3 main.py --install{C_RESET} to apply the Fluttershy rice.")

if __name__ == "__main__":
    main()
