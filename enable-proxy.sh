#! /bin/bash

# Filename: enable_proxy.sh 2016-07-14
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

proxy=http://127.0.0.1:12380

export http_proxy=$proxy
export https_proxy=$proxy
export HTTP_PROXY=$proxy
export HTTPS_PROXY=$proxy
export ftp_proxy=$proxy
export FTP_PROXY=$proxy

export all_proxy=socks://127.0.0.1:12389
export ALL_PROXY=$all_proxy

export no_proxy=localhost,127.0.0.0/8,::1
export NO_PROXY=$no_proxy

exec $*
