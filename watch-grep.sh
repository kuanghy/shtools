#! /bin/bash

# Filename: watch-grep.sh 2016-09-28
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

set -e

watch-grep()
{
    cmd="ps aux | grep -v grep | grep '$@'"
    watch -d -n1 $cmd
}

watch-grep $*

exit 0

