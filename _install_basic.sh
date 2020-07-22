#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2019-10-14 11:10:18
# Script starts from here:

PRO_DIR=~/Aboutme

mkdir -p $PRO_DIR
mkdir -p ~/.local/bin

cd $PRO_DIR

git clone https://github.com/kuanghy/shtools.git
TOOL_DIR=$PRO_DIR/shtools
cd $TOOL_DIR
ln -s $TOOL_DIR/shrc ~/.shrc
ln -s $TOOL_DIR/gitconfig ~/.gitconfig

git clone https://github.com/kuanghy/kictor.git
ln -s $PRO_DIR/kictor/kict.py ~/.local/bin/kict

git clone https://github.com/kuanghy/vimconfig.git
(cd vimconfig/vim-pro && make install)

exit 0
