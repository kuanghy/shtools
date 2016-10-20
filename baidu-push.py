#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
#     Filename @  baidu_push.py
#       Author @  Huoty
#  Create date @  2016-04-04 18:13:54
#  Description @  Baidu Push
# *************************************************************

import os
import sys
import re
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

log = get_logger("BaiduPush")

def get_site_urls(sitemap_url):
	try:
		r = requests.get(sitemap_url, timeout=30)
	except requests.exceptions.Timeout:
		log.exception("Connection timeout")
	except requests.exceptions.ConnectionError:
		log.exception("Connection error")
	except requests.exceptions.HTTPError:
		log.exception("Invalid HTTP response")

	return_code = r.status_code
	return_content = r.text

	if return_code == requests.codes.ok:
		log.info("Request was successful")
		urls = re.findall(r"<loc>(.*)</loc>", return_content)
	else:
		log.error("Request was aborted, status code is %s" % return_code)

	return urls

def push_urls():
	sitemap_url = "http://blog.konghy.cn/sitemap.xml"
	baidu_api = "http://data.zz.baidu.com/urls"
	payload = {"site": "blog.konghy.cn", "token": "NXXQ0TnjAq8mt7mw"}
	headers = {"content-type": "text/plain"}

	urls = get_site_urls(sitemap_url)
	count = len(urls)
	if count > 0:
		data = "\n".join(get_site_urls(sitemap_url))
	else:
		log.warning("Did not get to any url!")
		return

	try:
		r = requests.post(baidu_api, params=payload, headers=headers, data=data, timeout=30)
	except requests.exceptions.Timeout:
		log.exception("Connection timeout")
	except requests.exceptions.ConnectionError:
		log.exception("Connection error")
	except requests.exceptions.HTTPError:
		log.exception("Invalid HTTP response")

	response_msg = eval(r.text)  # Evaluate dict

	if "success" in response_msg:
		msg = "Url number of successful push is %s, remain %s" % \
			(response_msg["success"], response_msg["remain"])
	elif "error" in response_msg:
		msg = "Failed to push, " + response_msg['message']
		log.error(msg)
	else:
		msg = "Unknown response message!"

	log.info(msg)

	# from mailer import Mailer, Message
	# mail_msg = Message(From="监听者<%s>"%(os.environ["MAIL_ADDR"]),
	# 	To=["1346632121@qq.com"],
	# 	charset="utf-8")
	# mail_msg.Subject = "Baidu push report"
	# mail_msg.Html = "<strong>Report: </strong><p>%s</p>" % (msg)
	# sender = Mailer(host="smtp.yeah.net", usr=os.environ["MAIL_ADDR"], pwd=os.environ["MAIL_PASS"])
	# sender.send(mail_msg)


# Script starts from here

if __name__ == "__main__":
	push_urls()

# Crontab Configuration:
#   0 18    * * *    baidu-push.py >>/tmp/baidu-push.log 2>&1
