# coding:utf-8
# __author__ : Loid
# __Time__ : 2017年09月19日21:05:49

import os
import re
import sys
import requests
from libs.colors import *

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
        # if True:
            if hasattr(md, 'Exploit'):
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

    def setpath(self, cmsfile):
        sys.path.append(cmsfile)

