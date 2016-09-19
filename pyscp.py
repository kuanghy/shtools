#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
#     Filename @  pyscp.py
#       Author @  Huoty
#  Create date @  2016-09-18 14:10:57
#  Description @  python scp
# *************************************************************

from __future__ import print_function

from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

def scp(src, dest, host="localhost", port=22, user="root", passwd="", action="get"):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(host, port, user, passwd)

    with SCPClient(ssh.get_transport()) as scp:
        {
                "put": scp.put,
                "get": scp.get
        }[action](src, dest, recursive=True)

# Script starts from here

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser("pyscp")
    parser.add_argument("src")
    parser.add_argument("dest")
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=22)
    parser.add_argument("--user", type=str, default="root")
    parser.add_argument("--passwd", type=str, default="")
    parser.add_argument("--action", type=str, default="get")

    options = parser.parse_args()

    scp(**vars(options))

