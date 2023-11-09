# -*- coding: utf-8 -*-
import requests

version_url = 'https://ultronsandbox.oss-cn-hangzhou.aliyuncs.com/version/ultron.json'

__all__ = ['__version__']

__version__ = "1.3.2"


def get_version():
    res = requests.get('https://pypi.org/pypi/finance-ultron/json').json()
    if res.get('code') != 200:
        return '', ''

    remote_version = res['info']['version']
    content = res['info']['summary']

    return remote_version, content


def check_version():
    remote_version, content = get_version()
    if not remote_version or remote_version <= __version__:
        return
    print(
        "New pypi version: {0} (current: {1}) | pip install -U Finance-Ultron".
        format(remote_version, __version__))


check_version()