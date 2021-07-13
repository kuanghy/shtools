#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2019-10-14 11:10:18
# Script starts from here:

# 自动构建环境，可用下列方式一件安装：
#   sh -c "$(curl -fsSL https://gitee.com/konghy/shtools/raw/master/_install_basic.sh)"
#   sh -c "$(wget https://gitee.com/konghy/shtools/raw/master/_install_basic.sh -O -)"

PRO_DIR=~/Aboutme

mkdir -vp $PRO_DIR
mkdir -vp ~/.local/{bin,etc}

cd $PRO_DIR

git clone https://gitee.com/konghy/shtools.git

TOOL_DIR=$PRO_DIR/shtools
cd $TOOL_DIR

ln -s $TOOL_DIR/shrc ~/.shrc
ln -s $TOOL_DIR/gitconfig ~/.gitconfig

git clone https://gitee.com/konghy/kictor.git
ln -s $PRO_DIR/kictor/kict.py ~/.local/bin/kict

git clone https://gitee.com/konghy/vimconfig.git
(cd vimconfig/vim-pro && make install)

sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
ln -s $TOOL_DIR/zsh/konyon.zsh-theme ~/.oh-my-zsh/custom/themes/

exit 0
