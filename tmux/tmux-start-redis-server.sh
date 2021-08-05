#! /bin/bash

# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2021-08-05 17:42:24
# Script starts from here:

set -e

cd ~/.local/redis/
tmux new-session -s "redis" -d -n "redis-server" '~/.local/redis/bin/redis-server redis.conf'

exit 0
