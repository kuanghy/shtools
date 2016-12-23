#! /bin/bash

# Filename: sudo.sh 2016-12-23
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

# 让普通用户执行 sudo 时可以继承当前的环境变量

sudo -E PATH=$PATH env "$@"
