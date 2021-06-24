#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) JoinQuant Development Team
# Author: Huayong Kuang <kuanghuayong@joinquant.com>

"""
获取代理

基于 https://github.com/constverum/ProxyBroker
"""

import asyncio
import requests
from proxybroker import Broker


requests.adapters.DEFAULT_RETRIES = 0


async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        try:
            resp = requests.get("https://google.com", timeout=5, proxies={
                'http': f'socks5://{proxy.host}:{proxy.port}',
                'https': f'socks5://{proxy.host}:{proxy.port}'
            })
            resp.raise_for_status()
        except Exception as e:
            continue
        print('Found proxy: %s' % proxy)


proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['SOCKS5'], limit=1<<20),
    show(proxies)
)

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
