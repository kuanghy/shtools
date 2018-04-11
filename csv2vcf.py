#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) JoinQuant Development Team
# Author: Huayong Kuang <kuanghuayong@joinquant.com>

"""生成 vCard 通讯录(CSV to vCard）

CSV 文件各列：姓名, 公司(机构), 职位（部门）, 邮箱, 手机号

参考资料：
- https://gist.github.com/alanbosco/210d8a0b778e4ce55051771040ab4f18
- https://github.com/tech4242/python-csv-to-vcard/
"""

import quopri
