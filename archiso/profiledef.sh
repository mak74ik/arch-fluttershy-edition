#!/usr/bin/env bash
# Arch Linux Fluttershy Edition Profile Definition

iso_name="archlinux-fluttershy"
iso_label="ARCH_FLUTTERSHY_$(date +%Y%m)"
iso_publisher="mak74ik <https://github.com/mak74ik>"
iso_application="Arch Linux Fluttershy Edition Live/Rescue Media"
iso_version="$(date +%Y.%m.%d)"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito'
           'uefi-x64.systemd-boot.esp' 'uefi-x64.systemd-boot.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'zstd')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/root"]="0:0:750"
  ["/usr/local/bin/fluttershy-motd"]="0:0:755"
)
