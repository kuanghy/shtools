#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) Huoty, All rights reserved
# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2020-04-28 09:39:25

import sys
import time
import logging
import datetime


if sys.version_info.major < 3:
    import pyttsx
else:
    import pyttsx3 as pyttsx


log = logging
get_now = datetime.datetime.now


def speak(text):
    pyttsx.speak(text)


def start_timer():
    now = get_now()
    hour = now.hour
    minute = now.minute
    passed_minute = minute % 30
    if (8 <= hour <= 12 or 14 <= hour <= 22) and passed_minute == 0:
        current_time = now.strftime('%H:%M')
        text = "现在时间 {}".format(current_time)
        log.info("Telling time, current time: %s", current_time)
        speak(text)
        time.sleep(60)
    else:
        next_clock = now.replace(second=0, microsecond=0)
        if 0 < minute < 30:
            next_clock = next_clock.replace(minute=30)
        elif 30 < minute:
            next_clock = next_clock.replace(minute=0)
            next_clock += datetime.timedelta(hours=1)
        log.info("Next clock: %s", next_clock)
        rest_of_time = (next_clock - now).total_seconds()
        log.info("Began to sleep, the rest of time: %s",
                 datetime.timedelta(seconds=rest_of_time))
        time.sleep(rest_of_time)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    log.info("Starting timer, in loop")
    while True:
        start_timer()


if __name__ == "__main__":
    main()
