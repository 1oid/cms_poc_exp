# coding:utf-8
import requests

class Exploit:

    def attack(self, url):
        target = url + "/dede/login.php"
        req = requests.get(target, timeout=5)
        if req.status_code == 200 and "/include/vdimgck.php" in req.content:
            return "后台地址 {}".format(target)
