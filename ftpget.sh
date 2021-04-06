#! /bin/bash

# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2021-04-06 16:11:37
# Script starts from here:

if [ $# -ne 1 ]; then
    echo "Usage: $0 filepath"
fi

dir=$(dirname $1)
file=$(basename $1)

ftp -n -v << EOF        # 关闭自动登录
open 192.168.1.10       # ftp 服务器
user username password  # 账号与密码
binary                  # 设置传输模式为二进制
cd $dir
get "$file"
EOF
