#! /usr/bin/env zsh

# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2022-03-04 09:28:13
# Script starts from here:

mv ~/.zsh_history /tmp/zsh_history_bad
strings -eS /tmp/zsh_history_bad > ~/.zsh_history
fc -r ~/.zsh_history
rm /tmp/.zsh_history_bad
