#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

import os
import sys
import re
import datetime
from subprocess import check_call
from distutils.spawn import find_executable
import logging as log


def xz(filepath, keep=False):
    xz_exe = find_executable("xz")
    if not xz_exe:
        raise Exception("Command `xz` not found")
    args = "-zfk" if keep is True else "-zf"
    return check_call([xz_exe, args, filepath])

def extract_logfiles(logregs):
    if not isinstance(logregs, (tuple, list, set)):
        raise Exception("Parameters logregs must be in (tuple, list, set)")

    paths = {}
    for logreg in logregs:
        dirname = os.path.abspath(os.path.dirname(logreg))
        reg = r"^" + os.path.basename(logreg).strip() + r"$"
        regs = paths.get(dirname, [])
        regs.append(reg)
        paths[dirname] = regs

    logfiles = []
    for dirname, regs in paths.items():
        for filename in os.listdir(dirname):
            filepath = os.path.join(dirname, filename)
            if not os.path.isfile(filepath):
                continue
            for reg in regs:
                if re.match(reg, filename):
                    logfiles.append(filepath)
            pass
        pass

    return logfiles

def main(logregs, size=20, pridian=True, keep=False, debug=False):
    if debug:
        log.info("Start debug mode")
    logfiles = extract_logfiles(logregs)
    log.info("Handling %s logs" % len(logfiles))
    for logfile in logfiles:
        log_size = os.path.getsize(logfile) / (1000 * 1000)
        log_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(logfile))
        log.info("Considering log: %s" % logfile)
        if log_size < size:
            log.warning("Log don't be compressed because too small")
            continue
        if pridian and log_mtime.date() >= datetime.date.today():
            log.warning("Log don't be compressed because too new")
            continue
        if not debug:
            xz(logfile, keep)
        log.info("Compress `%s` done." % logfile)

def test():
    """Test this script by pytest"""
    logregs = [
        r"/home/server/logs/research-uwsgi.log.\d{10,}",
        r"/home/server/logs/public-service-uwsgi.log.\d{10,}",
        r"/home/server/logs/tools-uwsgi.log.\d{10,}",
        r"/home/huayong/logs/daily_unittest.log"
    ]
    logfiles = extract_logfiles(logregs)
    print(logfiles)
    assert len(logregs) > 1

    # compare the two files
    xz("/home/huayong/logs/test.log", keep=True)
    from shutil import move
    move("/home/huayong/logs/test.log.xz", "/home/huayong/logs/test.log.py.xz")
    os.system("xz -k /home/huayong/logs/test.log")
    from hashlib import md5
    with open('/home/huayong/logs/test.log.py.xz', 'rb') as f1, \
            open('/home/huayong/logs/test.log.xz', 'rb') as f2:
        hash1 = md5(f1.read()).hexdigest()
        hash2 = md5(f2.read()).hexdigest()
        print(hash1, hash2)
        assert hash1 == hash2


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Compresses logs")
    parser.add_argument("-r", "--reg", action='append', help="Regulation")
    parser.add_argument("-c", "--regfile", help="Regulations file")
    parser.add_argument("-l", "--list", action="store_true", help="List all matched files")
    parser.add_argument("-s", "--size", type=float, help="Compress only if greater than size(M)")
    parser.add_argument("-p", "--pridian", action="store_true", help="Only compress pridian logs")
    parser.add_argument("-d", "--debug", action="store_true", help="Don't do anything, just test")
    parser.add_argument("-k", "--keep", action="store_true", help="Keep (don't delete) source files")
    parser.add_argument("-v", "--verbose", action="store_true", help="Display messages during compresstion")

    options = parser.parse_args()

    import logging
    logging.basicConfig(
        level=(logging.INFO if options.verbose or options.debug else logging.CRITICAL),
        datefmt='%y%m%d %H:%M:%S',
        format='[%(levelname)1.1s %(asctime)s] %(message)s',
    )

    if options.reg:
        logregs = options.reg
    elif options.regfile:
        log.info("Reading regulations file %s" % options.regfile)
        with open(options.regfile) as f:
            logregs = [s.strip() for s in f]
    else:
        logregs = [r"/var/log/.*\.log.\d*"]

    if options.list:
        list(map(print, extract_logfiles(logregs)))
        sys.exit(0)

    main(logregs,
         size=options.size if options.size else 20.0,
         pridian=options.pridian,
         keep=options.keep,
         debug=options.debug)
