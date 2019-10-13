#! /bin/bash

# Filename: enable_proxy.sh 2016-07-14
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

proxy=localhost:12380

export http_proxy=$proxy
export https_proxy=$proxy
export HTTP_PROXY=$proxy
export HTTPS_PROXY=$proxy

exec $*

