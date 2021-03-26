#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) Huoty, All rights reserved
# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2018-01-02 16:57:54

from __future__ import print_function

import sys
import json

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from distutils.version import LooseVersion


name = sys.argv[1]

try:
    pypi_json_url = "https://pypi.org/pypi/{}/json".format(name)
    resp = urlopen(pypi_json_url, timeout=8)
    data = json.load(resp)

    for ver in sorted([LooseVersion(ver) for ver in data["releases"].keys()]):
        print(ver.vstring)

    print("See: https://pypi.org/simple/{}/".format(name))
except Exception as e:
    print(e)
