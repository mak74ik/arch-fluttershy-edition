# Fluttershy Edition ZSH Configuration

if [ -t 0 ] && [[ $(tty) =~ /dev/tty[0-9]+ ]]; then
    /usr/local/bin/fluttershy-theme light >/dev/null 2>&1
fi

alias theme='/usr/local/bin/fluttershy-theme'
alias menu='python3 /usr/local/bin/fluttershy-menu'
alias install-arch='bash /usr/local/bin/fluttershy-install'
alias fastfetch='fastfetch -c /etc/fastfetch/config.jsonc'

PROMPT='%F{1}✿ %F{5}%n%f@%F{6}%m%f %F{3}%~%f %F{1}🌸%f %# '

if [ -t 0 ] && [ -z "$FLUTTERSHY_INITIALIZED" ]; then
    export FLUTTERSHY_INITIALIZED=1
    fastfetch -c /etc/fastfetch/config.jsonc
    echo ""
    echo -e "\033[38;2;194;24;91m🌸 Добро пожаловать в Arch Linux Fluttershy Edition! ✿\033[0m"
    echo -e "Команды: \033[1;36mmenu\033[0m (меню) | \033[1;35mtheme dark\033[0m (тёмная тема) | \033[1;35mtheme light\033[0m (светлая тема) | \033[1;33minstall-arch\033[0m"
    echo ""
fi
