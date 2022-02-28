import inspect
import sys
import importlib
import os
from pathlib import Path


import colorama
colorama.init(autoreset=True)


class Color:
    RED = colorama.Fore.RED
    BLUE = colorama.Fore.BLUE
    GREEN = colorama.Fore.GREEN
    YELLOW = colorama.Fore.YELLOW


class Output(object):

    @staticmethod
    def color(color=None, string=None):
        if not color or not string:
            raise ValueError("Value Empty")

        return color + string

    def erase(self):
        sys.stdout.write("\r")

    def print(self, string):
        self.erase()
        sys.stdout.write(string)
        sys.stdout.flush()

    @staticmethod
    def log_error(string, label="[ERROR]"):
        print(
            Output.color(Color.RED, "{}{}".format(label, string))
        )

    @staticmethod
    def log_info(string, label="[INFO]"):
        print(
            Output.color(Color.BLUE, "{}{}".format(label, string))
        )

    @staticmethod
    def log_success(string, label="[SUCCESS]"):
        print(
            Output.color(Color.GREEN, "{}{}".format(label, string))
        )

    @staticmethod
    def log_warning(string, label="[WARNING]"):
        print(
            Output.color(Color.YELLOW, "{}{}".format(label, string))
        )


class Module(object):

    @staticmethod
    def set_path(path):
        sys.path.append(path)

    @staticmethod
    def import_mod(mod):
        return importlib.import_module(mod)

    @staticmethod
    def get_abs_path():
        return os.path.abspath(Path(__file__).parent.parent)

    @staticmethod
    def get_plugins():
        return [
            x.strip().split(".")[0]
            for x in os.listdir(Module.get_abs_path() + "/plugins")
            if "__" not in x.strip()
        ]

    @staticmethod
    def load_poc4pocsuite(module, url, pocscript):
        for _class_name, _class in inspect.getmembers(module, inspect.isclass):
            if _class_name != "POCBase" and inspect.getmro(_class)[1].__name__ == 'POCBase':
                # print(_class_name)
                exp = getattr(module, _class_name)()
                ret = exp.execute(url, mode='verify')

                output = ret.to_dict()

                if output and output['error_msg'][0] == 0:
                    if output['error_msg'][1] == "not vulnerability" or output['error_msg'][1] != "None":
                        Output.log_warning("check {} not vulnerability".format(pocscript), label="[NOT] ")
                    else:
                        for output_verify_key, output_verify_value in output['result']['VerifyInfo'].items():
                            # print(col.OutputGreen())
                            Output.log_success(output_verify_key + ": " + output_verify_value, label="[FIND] ")

                        Output.log_success("[{}] {}".format(pocscript, output['name']), label="[FIND]")
                        Output.log_success(output['poc_attrs']['desc'].strip(), label="[FIND] ")
                else:
                    Output.log_error(output['error_msg'][1])

    @staticmethod
    def load_poc4self(module, url, pocscript):
        poctest = getattr(module, 'Exploit')()
        ret = poctest.attack(url)

        if ret:
            Output.log_success("[{}] {}".format(pocscript, ret), label="[FIND]")
        else:
            Output.log_warning("check {} not vulnerability".format(pocscript), label="[NOT] ")


class Folder(object):

    @staticmethod
    def get_folders(path):
        return filter(lambda x: (True, False)[x[:2] == '__' or x[-3:] == 'pyc' or x[0] == '.'], os.listdir(path))

