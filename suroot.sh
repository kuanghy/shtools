#!/bin/bash

# Author: huoty <sudohuoty@gmail.com>
#   Date: 2016.05.10

# Script starts from here

ROOT_PASSWD="123456"

expect -c "
spawn /bin/su root
expect \"*?Password:*\"
send -- \"$ROOT_PASSWD\r\"
send -- \"\r\"
interact
"

exit 0

