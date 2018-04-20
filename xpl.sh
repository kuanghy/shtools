#! /bin/bash

# Filename: xpl.sh 2017-10-30
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

# 打开文件或者文件夹

cygwin=false;

case "`uname`" in
    CYGWIN*) cygwin=true ;;
esac

if [ "$1" = "" ]; then
    XPATH=.  # 缺省是当前目录
else
    XPATH=$1
	if $cygwin; then
        XPATH="$(cygpath -C ANSI -w "$XPATH")";
	fi
fi

explorer '/select,' $XPATH
