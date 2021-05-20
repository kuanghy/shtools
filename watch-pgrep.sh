#! /bin/bash

# Filename: watch-grep.sh 2016-09-28
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

set -e

watch-grep()
{
    psa="ps ax -o user,pid,ppid,pgid,ni,tty,stat,pcpu,pmem,start,time,cmd --sort -pcpu,-pmem"
    cmd="$psa | grep -v grep | grep -E 'USER|$@'"
    watch -d -n1 $cmd
}

watch-grep $*

exit 0

