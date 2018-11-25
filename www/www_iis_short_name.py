# coding:utf-8
# 常规web目录扫描
import requests

class Exploit:

    def attack(self,url):
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
        req1 = requests.get(url+'/*~1****/a.aspx', headers=headers)
        req2 = requests.get(url+'/loidair*~1****/a.aspx', headers=headers)
        if req1.status_code == 404 and req2.status_code == 400:
            return "{} has IIS Short Exploit.".format(url)