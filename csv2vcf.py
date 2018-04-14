#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) JoinQuant Development Team
# Author: Huayong Kuang <kuanghuayong@joinquant.com>

"""生成 vCard 通讯录(CSV to vCard）

CSV 文件各列：姓名, 公司(机构), 职位（部门）, 邮箱, 手机号

本程序仅支持 Python3

vCard 文件格式说明：
 - VCard 的每条记录以 BEGIN:VCARD 开头，以 END:VCARD 结尾
 - FN 字段表示记录的名称，一条记录必须包含 FN 字段
 - N 字段表示记录名称(FN)的组成部分，共为 6 个字段
 - ORG 字段表示公司、部门
 - TITLE 字段表示职位
 - TEL 字段表示电话号码
 - EMAIL 字段表示邮箱地址

参考资料：
 - https://baike.baidu.com/item/vCard
 - https://github.com/tech4242/python-csv-to-vcard/
 - https://gist.github.com/alanbosco/210d8a0b778e4ce55051771040ab4f18
"""

import csv
import quopri
import argparse


def _convert(csv_path, vcf_path, no_header=False):
    quopri_encode = lambda s: quopri.encodestring(s.encode("utf-8")).decode("utf-8")
    with open(csv_path, "r") as cf, open(vcf_path, "w") as vf:
        reader = csv.reader(cf)
        if not no_header:
            next(reader)
        for row in reader:
            n = "{};{};;;".format(quopri_encode(row[0][0]), quopri_encode(row[0][1:]))
            fn = quopri_encode(row[0])
            org = quopri_encode(row[1])
            title = quopri_encode(row[2])
            tel = "-".join([row[4][0], row[4][1:4], row[4][4:7], row[4][7:]])

            vf.write('BEGIN:VCARD\n')
            vf.write('VERSION:2.1\n')
            vf.write('N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:' + n + '\n')
            vf.write('FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:' + fn + '\n')
            vf.write('TEL;CELL:' + tel + '\n')
            vf.write('ORG;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:' + org + '\n')
            vf.write('TITLE;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:' + title + '\n')
            vf.write('EMAIL:' + row[3] + '\n')
            vf.write('END:VCARD\n')
            vf.write('\n')


def main():
    parser = argparse.ArgumentParser(description="convert CSV file to vCard file")
    parser.add_argument("csv", help="source file(CSV) path")
    parser.add_argument("vcf", help="destination file(vCard) path")
    parser.add_argument("--no-header", action="store_true",
                        help="csv file doesn't contain column names")
    args = parser.parse_args()
    _convert(args.csv, args.vcf, args.no_header)


if __name__ == "__main__":
    main()
