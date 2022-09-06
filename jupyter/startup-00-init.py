#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) Huoty, All rights reserved
# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2021-02-25 13:08:25

import os
import sys
import random
import datetime
from pprint import pprint as pp
from datetime import (
    datetime as DateTime,
    date as Date,
    timedelta as TimeDelta,
)


get_today = datetime.date.today
get_now = datetime.datetime.now


def _import_module(name):
    try:
        return __import__(name)
    except ImportError:
        return None


pd = pandas = _import_module("pandas")
np = numpy = _import_module("numpy")


if pandas:
    pd.set_option('display.precision', 12)
    pd.set_option('display.max_columns', 50)
    pd.set_option('display.max_rows', 200)
    pd.set_option('display.max_colwidth', 100)
