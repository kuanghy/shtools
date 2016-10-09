#! /bin/bash

# Filename: logoff.sh 2016-10-08
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

# 注销桌面

set -e

echo "Desktop logging off ..."

if [ $USER = "root" ]; then
    pkill Xorg
else
    sudo pkill Xorg
fi

