#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) JoinQuant Development Team
# Author: Huayong Kuang <kuanghuayong@joinquant.com>

"""
监控目录变化并自动同步，基于 watchdog 模块和 rsync （SSH认证）工具
"""

import os
import sys
import time
import logging
import subprocess
import logging as log
from importlib import import_module
from argparse import ArgumentParser
from distutils.spawn import find_executable

from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler


class Config(object):

    def __init__(self, **kwargs):
        self._mapping = {key.upper(): val for key, val in kwargs.items()}

    def __getattr__(self, name):
        try:
            return self._mapping[name.upper()]
        except KeyError:
            raise AttributeError("'{}' object has no attribute '{}'".format(
                self.__class__.__name__, name
            ))

    def load(self, path):
        yaml = import_module("yaml")
        with open(os.path.expanduser(path), encoding="utf-8") as fp:
            _config = yaml.safe_load(fp)
        self._mapping.update({key.upper(): val for key, val in _config.items()})

    def update(self, **kwargs):
        self._mapping.update({key.upper(): val for key, val in kwargs.items()})


class FileChangeHandler(RegexMatchingEventHandler):

    def __init__(self, config):
        self.config = config
        super().__init__(
            ignore_regexes=config.IGNORE_REGEXES,
            ignore_directories=config.IGNORE_DIRECTORIES
        )

    def _cmd_format(self, src_path):
        config = self.config
        cmd_tpl = getattr(self, "_cmd_tpl", None)
        if not cmd_tpl:
            if config.RSYNC_PATH:
                rsync_exe = config.RSYNC_PATH
            else:
                rsync_exe = find_executable("rsync")
            # rsync 的参数说明：
            #  -r 对子目录以递归模式处理
            #  -l 保留软链结
            #  -t 保持文件时间信息
            #  -z 对文件在传输时进行压缩处理
            cmd_tpl = f"{rsync_exe} -rltz"
            if config.ENABLE_GITIGNORE:
                gitignore_path = os.path.join(config.src_path, ".gitignore")
                if os.path.exists(gitignore_path):
                    cmd_tpl += f" --exclude-from={gitignore_path}"
            if config.SSH_PORT or config.SSH_KEY:
                ssh_param = 'ssh'
                if config.SSH_PORT:
                    ssh_param += f" -p {config.SSH_PORT}"
                if config.SSH_KEY:
                    ssh_key = os.path.expanduser(config.SSH_KEY)
                    ssh_param += f" -i {ssh_key}"
                cmd_tpl += f" -e '{ssh_param}'"
            cmd_tpl += " {}" + f" {config.SSH_USER}@{config.SSH_HOST}:" + "{}"
            setattr(self, "_cmd_tpl", cmd_tpl)

        dest_path = os.path.join(
            config.DEST_PATH,
            src_path.replace(config.SRC_PATH, "").lstrip(os.sep)
        )
        return cmd_tpl.format(src_path, dest_path)

    def _sync_path(self, src_path):
        cmd = self._cmd_format(src_path)
        log.info("Starting: %s", cmd)
        proc = subprocess.Popen(
            cmd,
            shell=True,
            cwd=self.config.SRC_PATH,
            env=None,
            stdout=None,
            stderr=subprocess.STDOUT
        )
        proc.wait(600)
        proc.kill()

    def _on_change(self, event):
        log.debug("%s %s: %s", event.event_type.title(),
                  "directory" if event.is_directory else "file",
                  event.src_path)
        self._sync_path(event.src_path)

    def on_created(self, event):
        self._on_change(event)

    def on_deleted(self, event):
        self._on_change(event)

    def on_modified(self, event):
        self._on_change(event)


def main():
    parser = ArgumentParser(description="Folder automatic synchronization tool")
    parser.add_argument("-c", "--config", help="Config path")
    parser.add_argument(
        "--loglevel",
        choices=["debug", "info", "warning", "error", "fatal", "critical"],
        help="Log level (default: info)"
    )
    parser.add_argument("-s", "--src-path", help="Source path")
    parser.add_argument("-d", "--dest-path", help="Destination path")
    parser.add_argument("--rsync-path", help="Rsync tool path")
    # parser.add_argument("--ssh-path", help="SSH path")
    parser.add_argument("--ssh-host", help="SSH host")
    parser.add_argument("--ssh-port", help="SSH port")
    parser.add_argument("--ssh-user", help="SSH user")
    parser.add_argument("--ssh-key", help="SSH Private key")

    args = parser.parse_args()

    config = Config()
    if args.config:
        config.load(args.config)
    kwargs = vars(args)
    kwargs.pop("config")
    config.update(**{key: val for key, val in kwargs.items() if val})

    loglevel = getattr(logging, (config.LOGLEVEL).upper())
    logging.basicConfig(
        stream=sys.stdout,
        level=loglevel,
        format="%(asctime)s - %(thread)d - %(levelname)s - %(message)s",
    )

    event_handler = FileChangeHandler(config)
    observer = Observer()
    observer.schedule(event_handler, config.SRC_PATH, recursive=True)
    log.info("Start watch %s", config.SRC_PATH)
    observer.start()
    try:
        while True:
            time.sleep(10)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()


# 配置文件示例
"""
# Rsync 同步工具路径
rsync_path: ''

# 同步的源目录与目的目录
src_path: ~/test
dest_path: ~/test

# SSH 相关配置
ssh_host: dev00
ssh_port: 23456
ssh_user: huoty
ssh_key: ~/.ssh/id_rsa

# 如果源目录下有 ..gitignore，则同步时排除其列出的文件
enable_gitignore: true

# 是否忽略目录
ignore_directories: true

# 文件忽略规则
ignore_regexes:
    - '.*[/\\]\.git$'
    - '.*[/\\]\.git[/\\].*'
    - '.*[/\\]\.DS_Store$'
    - '.*[/\\].*\.swp$'
    - '.*[/\\]\.vscode$'
    - '.*[/\\]\.vscode[/\\].*'
    - '.*[/\\]\.idea'
    - '.*[/\\]\.idea[/\\].*'
    - '.*[/\\]\.ftpconfig'
    - '.*[/\\]sftp-config\.json'
    - '.*[/\\]sftp-config-*\.json'
    - '.*[/\\].*\.pyc$'
    - '.*[/\\]__pycache__$'
    - '.*[/\\]__pycache__[/\\].*'
    - '.*[/\\]\.cache$'
    - '.*[/\\]\.cache/.*'

# 日志级别
loglevel: info
"""
