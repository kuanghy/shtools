#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2019-10-14 11:10:18
# Script starts from here:

usage()
{
    echo -e "Install shell basic configuration\n"
    echo "--"
}

SCRIPT_DIR="$( cd $(dirname $0); pwd )"

mkdir -p ~/.local/bin

ln -s $SCRIPT_DIR/userc ~/.userc
ln -s $SCRIPT_DIR/gitconfig ~/.gitconfig

while test $# -gt 0
do
    case "$1" in
        --opt1) echo "option 1"
            ;;
        --opt2) echo "option 2"
            ;;
        --*) echo "bad option $1"
            ;;
        *) echo "argument $1"
            ;;
    esac
    shift
done

exit 0
