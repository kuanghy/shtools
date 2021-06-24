#! /bin/bash

# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2021-06-10 10:23:09
# Script starts from here:

ip addr |awk '/state UP/{print $2}' | sed 's/://' | while read output
do
    echo $output:
    ethtool $output |grep "Speed:"
done
