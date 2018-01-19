#!/usr/bin/env python

"""
Forked From https://gist.github.com/spulec/1364640#file-pre-commit
"""

from __future__ import print_function

import os
import re
import subprocess
import sys

modified = re.compile('^[MA]\s+(?P<name>.*)$')

CHECKS = [
    {
        'output': 'Checking for pdb and ipdbs...',
        'command': r'grep -n "import [i]*pdb" %s',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*pre-commit'],
        'print_filename': True,
        'exists': False,
        'package': ''
    },
    {
        'output': 'Checking for print statements...',
        'command': r'grep -n "^\s*\bprint" %s',
        'match_files': ['.*\.py$'],
        'ignore_files': ['.*migrations.*', '.*management/commands.*',
                         '.*manage.py', '.*/scripts/.*', '.*/test[s]?/.*',
                         '.*__main__.py'],
        'print_filename': True,
        'exists': False,
        'package': ''
    },
    {
        'output': 'Running PyCodeStyle...',
        'command': 'pycodestyle -r --ignore=E402,E501,W293 %s',
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
        print(highlight('not installed %(command)s' % {'command': cmd}, 'yellow'))
        sys.exit(1)


def matches_file(file_name, match_files):
    return any(
        re.compile(match_file).match(file_name) for match_file in match_files)


def system(*args, **kwargs):
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, err = proc.communicate()
    return out, err


def check_files(files, check):
    result = 0
    print(highlight(check['output'], 'yellow'))

    if check['exists'] and check['package']:
        exists(check['package'])

    for file_name in files:
        if 'match_files' not in check or matches_file(file_name,
                                                      check['match_files']):
            if 'ignore_files' not in check or not matches_file(
                    file_name, check['ignore_files']):
                out, err = system(check['command'] % file_name,
                                  stderr=subprocess.PIPE, shell=True)
                if out or err:
                    if check['print_filename']:
                        prefix = '\t%s:' % file_name
                    else:
                        prefix = '\t'
                    output_lines = ['%s%s' % (prefix, line) for line in
                                    out.splitlines()]
                    print(highlight('\n'.join(output_lines), 'red'))
                    if err:
                        print(highlight(err, 'red'))
                    result = 1
    return result


def main():
    # Stash any changes to the working tree that are not going to be committed
    subprocess.call(['git', 'stash', '-u', '--keep-index'],
                    stdout=subprocess.PIPE)

    files = []
    out, err = system('git', 'status', '--porcelain')
    for line in out.splitlines():
        match = modified.match(str(line))
        if match:
            files.append(match.group('name'))

    for check in CHECKS:
        result = check_files(files, check)

    # Unstash changes to the working tree that we had stashed
    subprocess.call(['git', 'reset', '--hard'], stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
    subprocess.call(['git', 'stash', 'pop', '--quiet', '--index'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sys.exit(result)


if __name__ == '__main__':
    main()
