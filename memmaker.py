#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
#  Copyright (c) Huoty - All rights reserved
#
#      Author: Huoty <sudohuoty@gmail.com>
#  CreateTime: 2016-10-20 17:23:55
# *************************************************************

"""监控进程内存

利用 crontab 每分钟执行一次，将内存占用超过指定限制的进程杀掉

Crontab 设置：

- 每分钟执行一次：
    */1 * * * * memmaker --ignore=atom,terminator --min-pid=1000 >>/tmp/memmaker.log 2>&1

- 每 30 秒执行一次
    * *    * * *   memmaker --ignore=atom,terminator --min-pid=1000 >>/tmp/memmaker.log 2>&1
    * *    * * *   sleep 30; memmaker --ignore=atom,terminator --min-pid=1000 >>/tmp/memmaker.log 2>&1
"""

from __future__ import absolute_import, division

import os
import sys
import time

from psutil import process_iter, NoSuchProcess, virtual_memory


error_mail_template = '''\
Logger Name:        %(name)s
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Host:               %(host)s
Time:               %(asctime)s

Message:

%(message)s
'''

def get_logger(name):
    import logging
    from logging.handlers import SMTPHandler

    class CustomSMTPHandler(SMTPHandler):
        def emit(self, record):
            # add extra record
            record.host = __import__("socket").gethostname()
            super(CustomSMTPHandler, self).emit(record)

        def getSubject(self, record):
            formatter = logging.Formatter(fmt=self.subject)
            return formatter.format(record)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # add main log handler for error
    mail_handler = CustomSMTPHandler(
            mailhost = 'smtp.yeah.net',
            fromaddr = os.environ["MAIL_ADDR"],
            toaddrs  = ('loveqing2013@foxmail.com',),
            subject  = '%(name)s Error: %(message)s',
            credentials = (os.environ["MAIL_ADDR"], os.environ["MAIL_PASS"]))
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(error_mail_template))
    logger.addHandler(mail_handler)

    # add stream log handler for info
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(logging.Formatter(
        '[%(levelname)s %(asctime)s] %(message)s'
    ))
    logger.addHandler(stdout_handler)

    return logger

log = get_logger("MemMaker")

def scanner(mem_limit=30,  min_pid=0, ignore=None, debug=False):
    """扫描系统中正在运行的进程"""
    if debug:
        log.info("Start Scanning ...")

    ignore = ignore if ignore else []
    for proc in process_iter():
        # 忽略掉 ID 小的进程
        if proc.pid < min_pid:
            continue

        # 进程运行命令
        cmd = " ".join(proc.cmdline())
        if debug:
            log.info("Scanning: %s %s" % (proc.pid, cmd))

        # 忽略掉指定的进程
        for pname in ignore:
            if pname in cmd:
                continue

        try:
            proc_mem_percent = proc.memory_percent()
            total_mem_percent = virtual_memory().percent
            if proc_mem_percent > mem_limit and total_mem_percent > 80:
                proc.terminate()
                time.sleep(0.1)
                if proc.is_running:
                    proc.kill()  # 如果进程还没有结束就强制杀掉
                log.info("killed: %s, mem: %s, total_mem:%s" % (cmd, proc_mem_percent, total_mem_percent))
        except NoSuchProcess:
            pass
        except Exception as e:
            log.exception(e)


# Script starts from here

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(prog="memmaker",
                        description="scanning process memory usage",
                        epilog="Example: memmaker --ignore=atom,terminator --min-pid=1000")
    parser.add_argument("--mem-limit", type=float, default=30.0, help="Memory limit")
    parser.add_argument("--min-pid", type=int, default=0, help="Lower limit of the process id")
    parser.add_argument("--ignore", help="Ignore some proces")
    parser.add_argument("--debug", action="store_true", help="Debug mode")

    options = parser.parse_args()

    options.ignore = options.ignore.split(",") if options.ignore else []
    scanner(**vars(options))

    if options.debug:
        log.info("executed successfully")
