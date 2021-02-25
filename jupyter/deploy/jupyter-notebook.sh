#! /bin/bash

# Filename: run.sh 2017-04-29
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

source /home/notebook/.virtualenvs/py3/bin/activate
export PS1="$ "
exec jupyter-notebook "$*"
