#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
#  Copyright (c) Huoty - All rights reserved
#
#      Author: Huoty <sudohuoty@gmail.com>
#  CreateTime: 2016-11-24 23:43:37
# *************************************************************

"""手动向百度搜索引擎提交链接"""

import os
import sys
import re
import json
import time
import functools
import requests


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
            mailhost='smtp.yeah.net',
            fromaddr=os.environ["MAIL_ADDR"],
            toaddrs=('loveqing2013@foxmail.com',),
            subject='%(name)s Error: %(message)s',
            credentials=(os.environ["MAIL_ADDR"], os.environ["MAIL_PASS"]))
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


log = get_logger("BlogSEO")


def retry_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        run_count = 0
        while 1:
            try:
                run_count += 1
                return func(*args, **kw)
            except Exception as e:
                if run_count > 100:  # 重试 100 次
                    raise
                log.warn("func(%s) run error, error: %s, run_count: %s",
                         func.__name__, e, run_count)
                time.sleep(2)
            else:
                break
    return wrapper


class KeepAliveRequest(object):

    def __init__(self):
        user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0"
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": user_agent,
        })

    @retry_decorator
    def __request_text(self, url, payload=None, method="GET"):
        if method not in ("GET", "POST"):
            log.error("Not support '%s' request type" % method)
            return None


        res = (self.session.get(url, params=payload, timeout=6) if method == "GET" else
            self.session.post(url, data=payload, timeout=6))
        res.raise_for_status()
        return res.text

    def get(self, url, payload=None):
        return self.__request_text(url, payload=payload, method="GET")

    def post(self, url, payload=None):
        return self.__request_text(url, payload=payload, method="POST")


def push_urls(site):
    sitemap_url = "http://{site}/sitemap.xml".format(site=site)
    baidu_push_api = "http://data.zz.baidu.com/urls?site={site}&token=NXXQ0TnjAq8mt7mw"
    baidu_push_api = baidu_push_api.format(site=site)

    try:
        request = KeepAliveRequest()
        sitemap = request.get(sitemap_url)
        urls = re.findall(r"<loc>(.*)</loc>", sitemap)
    except Exception as e:
        log.exception(e)
        return

    if urls:
        data = "\n".join(urls)

        try:
            request.session.headers.update({"content-type": "text/plain"})
            res_text = request.post(baidu_push_api, payload=data)
            res_data = json.loads(res_text)
        except Exception as e:
            log.exception(e)
            return

        if "error" in res_data and res_data["success"] == 0:
            log.error(res_text)
        elif res_data.get("not_valid", None):
            log.error("There are some not-valid urls: %s", res_data["not_valid"])
        else:
            log.info("Push successfully for %s, success: %s, remain: %s",
                site, res_data["success"], res_data["remain"])
    else:
        log.error("Did not get to any url!")


# Script starts from here

if __name__ == "__main__":
    for site in ("www.konghy.cn", "blog.konghy.cn", "opus.konghy.cn"):
        push_urls(site)

# Crontab Configuration:
#   0 18    * * *    siteseo.py >>/tmp/baidu-push.log 2>&1
