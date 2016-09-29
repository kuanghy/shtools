#! /bin/bash

# Filename: tmux-init.sh 2016-09-29
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

set -e

tmux_init()
{
    tmux new-session -s "huoty" -d -n "local"    # 开启一个会话
    tmux new-window -n "other"          # 开启一个新窗口
    tmux select-window -t "local"       # 切换窗口到 local
    tmux -2 attach-session -d           # tmux -2 强制启用 256color，连接已开启的 tmux
}

# 判断是否已有开启的tmux会话，没有则开启
if which tmux 2>&1 >/dev/null; then
    test -z "$TMUX" && (tmux attach || tmux_init)
fi

