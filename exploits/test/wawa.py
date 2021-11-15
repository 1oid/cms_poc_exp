from pocsuite3.api import register_poc
from pocsuite3.api import Output, POCBase
from pocsuite3.api import POC_CATEGORY, VUL_TYPE


class TestPOC(POCBase):
    vulID = '0'
    version = '1.0'
    author = 'hancool'
    vulDate = '2018-12-25'
    createDate = '2018-12-25'
    updateDate = '2018-12-25'
    references = ['', ]
    name = 'Apache ZooKeeper unauthorized access'
    appPowerLink = ''
    appName = 'zookeeper'
    appVersion = 'All'
    vulType = VUL_TYPE.UNAUTHORIZED_ACCESS
    category = POC_CATEGORY.EXPLOITS.REMOTE
    desc = '''
        Apache Zookeeper安装部署之后默认情况下不需要身份认证，攻击者可通过该漏洞泄露服务器的敏感信息。
        '''

    def _verify(self):
        output = Output(self)
        output.success({
            "success": "aa"
        })
        return output

    def _attack(self):
        return self._verify()


# register_poc(TestPOC)

# a = TestPOC()
# print(
#     a.execute("http://www.baidu.com", mode="verify").to_dict()
# )

register_poc(TestPOC)

