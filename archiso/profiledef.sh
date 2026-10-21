#!/usr/bin/env bash
# shellcheck disable=SC2034

iso_name="archlinux-fluttershy"
iso_label="ARCH_FLUTTERSHY_$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y%m)"
iso_publisher="mak74ik <https://github.com/mak74ik>"
iso_application="Arch Linux Fluttershy Edition Live/Rescue Media"
iso_version="$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y.%m.%d)"
install_dir="arch"
bootmodes=('bios.syslinux'
           'uefi.systemd-boot')
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'zstd')
bootstrap_tarball_compression=('zstd' '-c' '-T0' '--auto-threads=logical' '--long' '-19')
kernel_params_aarch64="clk_ignore_unused pd_ignore_unused arm64.nopauth"
file_permissions=(
  ["/usr/local/bin/fluttershy-menu"]="0:0:755"
  ["/usr/local/bin/fluttershy-install"]="0:0:755"
  ["/usr/local/bin/fluttershy-motd"]="0:0:755"
  ["/etc/shadow"]="0:0:400"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/root/.gnupg"]="0:0:700"
  ["/usr/local/bin/choose-mirror"]="0:0:755"
  ["/usr/local/bin/Installation_guide"]="0:0:755"
  ["/usr/local/bin/livecd-sound"]="0:0:755"
)
