#! /bin/bash

# Filename: shutdown-hnow.sh 2016-09-19
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

PASSWD="xxxxxx"
echo "Shutting down ..."
echo $PASSWD | sudo -S init 0 > /dev/null 2>&1

