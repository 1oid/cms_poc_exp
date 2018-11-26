import re
import os
import sys


def listTargetFolder(folder_name="."):
    ret = []
    if folder_name == ".":
        for folder in os.listdir("."):
            if folder[0] == ".":
                continue
            if os.path.isdir(folder):
                for plugin in os.listdir(folder):
                    ret.append(folder+"/"+plugin)

        return ret
    return os.listdir(folder_name)


def search(pluginName, regx):

    with open(pluginName) as f:
        if re.search(regx, f.read()):
            return True


# for plugin in listTargetFolder(cms):
#     path = cms + "/" + plugin
#     if search(path, key):
#         print("find {} in {}".format(key, path))


if __name__ == '__main__':
    cms = None
    key = None

    args = sys.argv
    if len(args) == 3:
        _, cms, key = args
    elif len(args) == 2:
        _, key = args
        cms = "."
    else:
        print("使用方法: ")
        print("python {script} dedecms \"login.php\"".format(script=args[0]))
        print("python {script} \"login.php\"".format(script=args[0]))
        exit()

    # print(listTargetFolder(cms))
    for plugin in listTargetFolder(cms):
        path = cms + "/" + plugin
        if search(path, key):
            print("find {} in {}".format(key, path))
