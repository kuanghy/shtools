#! /bin/bash

# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2021-06-10 10:26:52
# Script starts from here:

hostname
echo "-------------"
for iname in $(ip addr |awk '/state UP/{print $2}')
do
    echo "$iname"
    ip addr show $iname | grep inet | awk '{printf "%s:\t%s\n",$1,$2}'
    ip link show $iname | grep link | awk '{printf "MAC:\t%s\n",$2}'
    ethtool ens33 | awk '/Speed/{printf "%s\t%s\n",$1,$2}'
done
