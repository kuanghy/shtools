#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) Huoty, All rights reserved
# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2018-04-19 19:14:09

# Forked From https://gist.github.com/spulec/1364640

from __future__ import print_function

import os
import re
import sys
import subprocess


if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")


CHECKS = [
    {
        'output': 'Checking for pdb and ipdbs...',
        'command': r'grep -n "import [i]*pdb" %s',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*pre-commit', '.*__main__.py'],
        'print_filename': True,
        'exists': False,
        'package': ''
    },
    {
        'output': 'Checking for print statements...',
        'command': r'grep -n "^\s*\bprint" %s',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*migrations.*', '.*management/commands.*',
                         '.*manage[r]?.py', '.*/scripts/.*', '.*/test[s]?/.*',
                         '.*__main__.py'],
        'print_filename': True,
        'exists': False,
        'package': ''
    },
    {
        'output': 'Running PyCodeStyle...',
        'command': 'pycodestyle -r --ignore=E402,E501,E731,W293 %s',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*migrations.*'],
        'print_filename': False,
        'exists': True,
        'package': 'pycodestyle'
    },
    {
        'output': 'Running PyFlakes...',
        'command': 'pyflakes %s',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*migrations.*', '.*/terrain/.*'],
        'print_filename': False,
        'exists': True,
        'package': 'pyflakes'
    }
]


def highlight(text, status):
    attrs = []
    colors = {
        'green': '32', 'red': '31', 'yellow': '33'
    }
    if not sys.stdout.isatty():
        return text
    attrs.append(colors.get(status, 'red'))
    attrs.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attrs), text)


def exists(cmd, error=True):
    devnull = open(os.devnull, 'w')
    params = {'stdout': devnull, 'stderr': devnull, }
    query = 'which %s' % cmd
    code = subprocess.call(query.split(), **params)
    if code != 0 and error:
        print(highlight('not installed %(command)s' % {'command': cmd}, 'red'))
        sys.exit(1)


def matches_file(file_name, match_files):
    return any(re.compile(match_file).match(file_name) for match_file in match_files)


def system(*args, **kwargs):
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, err = proc.communicate()
    out = out if out is None or isinstance(out, str) else out.decode("utf-8")
    err = err if err is None or isinstance(err, str) else err.decode("utf-8")
    return out, err


def check_files(files, check):
    result = 0
    print(highlight(check['output'], 'yellow'))

    if check['exists'] and check['package']:
        exists(check['package'])

    for file_name in files:
        if 'match_files' not in check or matches_file(
                file_name, check['match_files']):
            if 'ignore_files' not in check or not matches_file(
                    file_name, check['ignore_files']):
                out, err = system(check['command'] % file_name,
                                  stderr=subprocess.PIPE, shell=True)
                if out or err:
                    if check['print_filename']:
                        prefix = '\t%s:' % file_name
                    else:
                        prefix = '\t'
                    output_lines = ['{}{}'.format(prefix, line) for line in
                                    out.splitlines()]
                    print(highlight('\n'.join(output_lines), 'red'))
                    if err:
                        print(highlight(err, 'red'))
                    result = 1
    return result


def main():
    out, err = system('git', 'status', '--porcelain', stderr=subprocess.PIPE)
    if err:
        print(highlight(err, 'red'), end='')
        return 1

    modified = re.compile('^[MA]\s+(?P<name>.*)$')

    files = []
    for line in out.splitlines():
        match = modified.match(str(line))
        if match:
            files.append(match.group('name'))

    if not files:
        return 0

    result = 0
    for check in CHECKS:
        result = check_files(files, check) or result

    return result


if __name__ == '__main__':
    sys.exit(main())
