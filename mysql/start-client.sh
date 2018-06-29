#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2018-03-23 10:00:48
# Script starts from here:

cd `dirname $0`
exec $(pwd)/bin/mysql -h 127.0.0.1 -P 3306 -u root -p123456
