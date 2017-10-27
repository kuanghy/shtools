#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
#  Copyright (c) JoinQuant Development Team
#
#  Author: Huayong Kuang <kuanghuayong@joinquant.com>
#  CreateTime: 2017-10-27 10:06:32 Friday
# *************************************************************

from __future__ import print_function

from prettytable import PrettyTable

def main():
    suffixes = [
        ["XSHG", "上海证券交易所"],
        ["XSHE", "深圳证券交易所"],
        ["CCFX", "中国金融期货交易所"],
        ["XDCE", "大连商品交易所"],
        ["XSGE", "上海期货交易所"],
        ["XZCE", "郑州商品交易所"],
        ["XHKG", "香港证券交易所"],
    ]

    rows = PrettyTable()
    rows.field_names = ["code", "explain"]
    rows.align["code"] = 'l'
    rows.align["explain"] = 'l'
    for suffix in suffixes:
        rows.add_row(suffix)
    print(rows)


# Script starts from here

if __name__ == "__main__":
    main()
