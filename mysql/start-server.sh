#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2018-03-23 10:00:48
# Script starts from here:

cd `dirname $0`
echo "currently running in $(pwd)"
exec $(pwd)/bin/mysqld_safe --defaults-file=$(pwd)/my.cnf
