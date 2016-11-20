#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
#     Filename @  blogseo.py
#       Author @  Huoty
#  Create date @  2016-04-04 18:13:54
#  Description @  博客自动搜索引擎优化
# *************************************************************

"""
手动向百度搜索引擎提交链接
"""

import os
import sys
import re
import json
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

log = get_logger("BlogSEO")

def send_mail():
    # from mailer import Mailer, Message
	# mail_msg = Message(From="监听者<%s>"%(os.environ["MAIL_ADDR"]),
	# 	To=["1346632121@qq.com"],
	# 	charset="utf-8")
	# mail_msg.Subject = "Baidu push report"
	# mail_msg.Html = "<strong>Report: </strong><p>%s</p>" % (msg)
	# sender = Mailer(host="smtp.yeah.net", usr=os.environ["MAIL_ADDR"], pwd=os.environ["MAIL_PASS"])
	# sender.send(mail_msg)
    pass


class KeepAliveRequest(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
        })

    def __request_text(self, url, payload=None, method="GET"):
        if method not in ("GET", "POST"):
            log.error("Not support '%s' request type" % method)
            return None

        try:
            res = self.session.get(url, params=payload) if method == "GET" else \
                self.session.post(url, data=payload)
            res.raise_for_status()
            return res.text
        except Exception as e:
            log.exception(e)

    def get(self, url, payload=None):
        return self.__request_text(url, payload=payload, method="GET")

    def post(self, url, payload=None):
        return self.__request_text(url, payload=payload, method="POST")


def push_urls():
    sitemap_url = "http://blog.konghy.cn/sitemap.xml"
    baidu_push_api = "http://data.zz.baidu.com/urls?site=blog.konghy.cn&token=NXXQ0TnjAq8mt7mw"

    request = KeepAliveRequest()
    sitemap = request.get(sitemap_url)
    urls = re.findall(r"<loc>(.*)</loc>", sitemap)

    if urls:
        data = "\n".join(urls)

        request.session.headers.update({"content-type": "text/plain"})
        res_text = request.post(baidu_push_api, payload=data)
        res_data = json.loads(res_text)

        if "error" in res_data and res_data["success"] == 0:
            log.error(res_text)
        elif res_data.get("not_valid", None):
            log.error("There are some not-valid urls: %s" % res_data["not_valid"])
        else:
            log.info("Url number of successful push is {success}, remain {remain}".format(**res_data))
    else:
        log.error("Did not get to any url!")


# Script starts from here

if __name__ == "__main__":
	push_urls()

# Crontab Configuration:
#   0 18    * * *    baidu-push.py >>/tmp/baidu-push.log 2>&1
