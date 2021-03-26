#! /bin/bash

# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2021-03-26 18:46:46
# Script starts from here:

path=$1
for i in `iconv -l`
do
   echo $i
   iconv -f $i -t UTF-8 $path | grep "hint to tell converted success or not"
done
