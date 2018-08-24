#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2018-08-24 21:54:22
# Script starts from here:

# Aria2 RPC #
/Users/huayong/.local/aria2/bin/aria2c \
    --enable-rpc=true \
    --input-file=/Users/huayong/.aria2/aria2.session \
    --conf-path=/Users/huayong/.aria2/aria2.conf \
    "$@"
