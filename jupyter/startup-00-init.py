#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) Huoty, All rights reserved
# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2021-02-25 13:08:25

def _import_module(name):
    try:
        return __import__(name)
    except ImportError:
        return None


pd = pandas = _import_module("pandas")
np = numpy = _import_module("numpy")


if pandas:
    pd.set_option('precision', 12)
    pd.set_option('display.max_rows', 500)
