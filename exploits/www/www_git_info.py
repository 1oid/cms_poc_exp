import binascii
import os

import requests
import mmap
import struct
import collections


def check(boolean, message):
    if not boolean:
        import sys
        sys.exit(1)


def parse(filename, pretty=True):
    with open(filename, "rb") as o:
        f = mmap.mmap(o.fileno(), 0, access=mmap.ACCESS_READ)

        def read(format):
            # "All binary numbers are in network byte order."
            # Hence "!" = network order, big endian
            format = "! " + format
            bytes = f.read(struct.calcsize(format))
            return struct.unpack(format, bytes)[0]

        index = collections.OrderedDict()

        # 4-byte signature, b"DIRC"
        index["signature"] = f.read(4).decode("ascii")
        # 4-byte version number
        index["version"] = read("I")

        if index['signature'] and index['version']:
            return True

        f.close()


class Exploit(object):

    def attack(self, url):
        r = requests.get(url + "/.git/index")

        if r.status_code == 200 and r.headers.get("Content-type") == "application/octet-stream":
            with open('index', 'wb') as f:
                f.write(r.content)

            if parse('index'):
                if os.path.isfile("index"):
                    os.remove("index")
                return "Git File: {}".format(url + "/.git/")

