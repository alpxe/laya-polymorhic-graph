import os
import re
import json

"""
提取laya air 中 所需的加载路径
"""


class Main:
    # 项目路径
    project = "/Users/alpxe/code/h5/laya/laya-duudle"

    def __init__(self):
        ui_url = os.path.join(self.project, "src/ui/layaMaxUI.ts")
        file_url = os.path.join(self.project, "bin/fileconfig.json")

        with open(file_url, 'r') as fp:
            data = json.load(fp)
        self.ext_config(data)

        print('\n')

        with open(ui_url, 'r') as fp:
            lines = fp.readlines()
        self.ext_scene(lines)

    @staticmethod
    def ext_config(data):
        for item in data:
            print('''{{url: "{0}", type: Laya.Loader.ATLAS}},'''.format(item))

    @staticmethod
    def ext_scene(lines):
        links = []
        for line in lines:
            path = re.findall(r"this.loadScene\(\"(.+?)\"\)", line)
            links.extend(path)

        for p in links:
            print('''{{url: "{0}.json", type: Laya.Loader.JSON}},'''.format(p))


if __name__ == "__main__":
    Main()
