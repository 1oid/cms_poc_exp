# coding:utf-8
# __author__ : Loid
import pocsuite3
from libs.func import *

ini = fileOperation()
# 列出所有exploitds下面的所有的文件夹
expFolders = list(ini.exloitsFilesList())


def scan(cms, url,):
    # 输入的cms是否在exploits下面
    if cms in expFolders:
        # 获取 cms 文件夹下所有的插件
        filename, plugins = ini.exploitScriptsList(cms)
        # 设置环境变量
        ini.setpath(filename)

        # 循环调用插件
        for plugin in plugins:
            output = '[*] Load Plugin {}'.format(plugin)
            print(col.OutputBlue(output))
            ini.executePlugin(plugin[:-3], url)


def cmdparse(url, urls, cms, all=None):
    """
    解析 cmd 命令
    :param url:
    :param urls:
    :param cms:
    :param all:
    :return:
    """
    urlList = []
    if url:
        urlList.append(url)
    elif urls:
        urlList = urls
    else:
        pass

    if not all:
        if cms in list(expFolders):
            for _url in urlList:
                scan(cms, _url)
        else:
            print("[??] CMS Not Exist!")
    else:
        for expfolder in expFolders:
            for _url in urlList:
                try:
                    scan(expfolder, _url)
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    from optparse import OptionParser

    usage = '%prog -u http://www.baidu.com -c phpcms\n'
    parser = OptionParser(usage=usage)
    parser.add_option("-u", "--url", dest="url", help="Url Link", default=None)
    parser.add_option("-m", "--urls", dest="urls", help="Url Links", default=None)
    parser.add_option("-c", "--cms", dest='cms', help="Cms Name", default=None)
    parser.add_option("-a", "--all", dest='all', action="store_true", help="All Cms Plugin Load")
    options, args = parser.parse_args()

    cmdparse(options.url, options.urls, options.cms, options.all)

