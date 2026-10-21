
/usr/local/bin/fluttershy-motd

alias menu='python3 /usr/local/bin/fluttershy-menu'
alias install-arch='bash /usr/local/bin/fluttershy-install'
if [ -z "$FLUTTERSHY_NO_MENU" ] && [ -t 0 ]; then
    python3 /usr/local/bin/fluttershy-menu
fi
