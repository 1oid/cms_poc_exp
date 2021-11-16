# coding:utf-8
# __author__ : Loid
# __Time__ : 2017年09月19日21:05:49

import os
import re
import sys

import requests
from libs.colors import *
import inspect

from pocsuite3.lib.core.poc import POCBase

col = Color()


class fileOperation(object):

    '''
    @exploitsFileList 
        列出exploits文件夹下的文件夹
    
    @exploitScriptsList
        列出所有可用插件
    
    @executePlugin
        解析调用插件
    '''
    def __init__(self):
        pass

    def exloitsFilesList(self):
        filename = os.getcwd() + '/exploits'
        fileList = os.listdir(filename)
        return filter(lambda x: (True, False)[x[-3:] == '.py' or x[0] == "."], fileList)

    def exploitScriptsList(self, filen):
        filename = "{}/exploits/{}".format(os.getcwd(), filen)
        fileList = os.listdir(filename)
        return filename, filter(lambda x: (True, False)[x[:2] == '__' or x[-3:] == 'pyc'], fileList)

    def executePlugin(self, expName, url):
        md = __import__(expName)
        try:
            if hasattr(md, 'register_poc'):
                for _class_name, _class in inspect.getmembers(md, inspect.isclass):
                    if _class_name != "POCBase" and inspect.getmro(_class)[1].__name__ == 'POCBase':
                        # print(_class_name)
                        exp = getattr(md, _class_name)()
                        ret = exp.execute(url, mode='verify')

                        output = ret.to_dict()

                        if output and output['error_msg'][0] == 0:
                            print(col.OutputGreen(output))
                        else:
                            print(col.OutputRed(output['error_msg'][1]))

                # print(inspect.getmembers(md, inspect.isclass))
                # print(dir(md))
                # print(hasattr(md, 'register_poc'))
            elif hasattr(md, 'Exploit'):
                exp = getattr(md, 'Exploit')()
                ret = exp.attack(url)
                if ret:
                    output = '[Success!!!] {}'.format(ret)
                    print(col.OutputGreen(output))
                else:
                    output = '[-] Execute Fail!'
                    print(col.OutputRed(output))
        #
        except requests.exceptions.MissingSchema as e:
            print('[!] MissingScheme.')
        except requests.exceptions.ConnectionError as e:
            print("[!] ConnectionError")

    def setpath(self, cmsfile):
        sys.path.append(cmsfile)

