# coding:utf-8
# url link : http://0day5.com/archives/3432/
import requests

class Exploit:

    def attack(self, url):
        response = requests.get(url + '/file.asmx')

        if response.status_code == 200:
            return "{}/file.asmx Maybe Exist!".format(url)

