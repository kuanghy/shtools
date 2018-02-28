#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

set -e

tmux_init()
{
    tmux new-session -s "work" -d -n "kict" kict
    tmux new-window -n "local"
    tmux new-window
    tmux new-window
    tmux new-window
    tmux new-window
    tmux select-window -t "local"
    tmux -2 attach-session -d
}

# 判断是否已有开启的 tmux 会话，没有则开启
if which tmux 2>&1 >/dev/null; then
    test -z "$TMUX" && (tmux attach || tmux_init)
fi
