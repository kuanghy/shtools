#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2018-01-06 17:21:28
# Script starts from here:

while [ 1 ] ; do
	clear
	echo "Command: $*"
	date
	echo ""
	( $* )
	sleep 2
done
