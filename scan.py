from libs.core import Color, Output, Module, Folder
import os


class Runner(object):

    def __init__(self):
        self.folders = []

        self.init()

    def _check_cms(self, cms):
        if cms not in self.folders:
            raise ValueError("not correct cms")

    def init(self):
        """
        1. load exploit folders
        """
        self.folders = list(Folder.get_folders(os.path.join(Module.get_abs_path(), "exploits")))
        Output.log_info("loaded exploits folder {}".format(len(self.folders)))

    def init_exploit_scripts(self, path):
        scripts = list(Folder.get_folders(os.path.join(Module.get_abs_path(), "exploits", path)))
        Output.log_info("loaded {} plugins for {}".format(len(scripts), path))
        return scripts

    def check(self, url, cms):
        self._check_cms(cms)

        scripts = self.init_exploit_scripts(cms)

        for script in scripts:
            Module.set_path(os.path.join(Module.get_abs_path(), "exploits", cms))
            script = script[:-3]
            module = Module.import_mod(script)

            try:
                if hasattr(module, 'register_poc'):
                    Module.load_poc4pocsuite(module, url, script)
                elif hasattr(module, 'Exploit'):
                    Module.load_poc4self(module, url, script)
            except Exception as e:
                Output.log_error(str(e))

    def run(self, urls, module, is_all=False):
        urls = [urls] if isinstance(urls, str) else urls
        modules = [module] if not is_all else self.folders

        for module in modules:
            [self.check(url, module) for url in urls]


if __name__ == '__main__':
    from optparse import OptionParser

    usage = '%prog -u http://www.baidu.com -m phpcms\n'
    parser = OptionParser(usage=usage)
    parser.add_option("-u", "--url", dest="url", help="URL链接", default=None)
    parser.add_option("-f", "--urls", dest="urls", help="urls文件", default=None)
    parser.add_option("-m", "--module", dest='module', help="cms模块名", default=None)
    parser.add_option("-a", "--all", dest='all', action="store_true", help="All Cms Plugin Load")
    options, args = parser.parse_args()

    # Runner().check(options, cms)
    if not any([options.module, options.all]):
        raise ValueError("missing parameters")

    runner = Runner()
    if not options.url and options.urls is not None:
        with open(options.urls) as f:
            runner.run([url.strip() for url in f.readlines()], options.module, is_all=options.all)
    else:
        runner.run(options.url, options.module, is_all=options.all)
