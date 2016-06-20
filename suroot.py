#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
#     Filename @  suroot.py
#       Author @  Huoty
#  Create date @  2016-06-20 14:18:39
#  Description @  auto login root
# *************************************************************

import os
import pexpect

ROOT_PASSWD = "123456"

# Script starts from here

if __name__ == "__main__":
    os.system("source activate hua")
    child = pexpect.spawn("/bin/su root")
    child.expect("*?Password:*")
    child.sendline(ROOT_PASSWD)
    child.before
    child.interact()

