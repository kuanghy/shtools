#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2018-11-01 22:47:56
# Script starts from here:

for ip in $@; do
    curl https://ip.cn/index.php?ip=$ip
done
