#! /bin/bash

# Filename: ksudo.sh 2016-12-23
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

# 让普通用户执行 sudo 时可以继承当前的环境变量
# -E 选项可以将当前用户的环境变量应用到 sudo 启动的程序
# sudo 支持用 VAR=value 的形式形式制定额外的环境变量
# env 命令会输出当前所有的环境变量

sudo -E PATH=$PATH env "$@"
