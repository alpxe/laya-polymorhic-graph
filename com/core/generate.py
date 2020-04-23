import os
import numpy as np
import cv2

from com.base.singleton import Singleton


class Generate(Singleton):
    padding = 2
    arrange = "vert"  # 布局方向 hroi vert
    alignH = "M"  # 对齐方式 # 头 中 尾 F M T
    alignV = "M"

    root_path = os.path.abspath(os.path.dirname("."))
    input_file_path = "assets\\input"
    output_file_path = "assets\\output"

    def setting(self, arrange, alignH, alignV, padding):
        self.arrange = arrange
        self.alignH = alignH
        self.alignV = alignV
        self.padding = padding

    def run(self):
        all_files = []
        imgs = []  # 图片数据
        max_height = 0
        max_width = 0

        if not os.path.exists(self.input_file_path):
            os.makedirs(self.input_file_path)

        for root, dirs, files in os.walk(self.input_file_path):
            # self.place_map = files
            all_files = files

        all_files.sort()

        for img_path in all_files:
            img = cv2.imread("{}/{}".format(self.input_file_path, img_path), cv2.IMREAD_UNCHANGED)
            height, width, _ = img.shape
            print("{}x{}".format(width, height))
            if width > max_width:
                max_width = width
            if height > max_height:
                max_height = height

            imgs.append(img)

        max_width += self.padding * 2
        max_height += self.padding * 2

        if self.arrange == "hroi":
            uw = max_width * len(imgs)
            uh = max_height
        elif self.arrange == "vert":
            uw = max_width
            uh = max_height * len(imgs)

        unite = np.zeros([uh, uw, 4], dtype=np.int)
        for i in range(len(imgs)):
            hs = int((max_height - imgs[i].shape[0]) / 2)
            ws = int((max_width - imgs[i].shape[1]) / 2)

            if self.alignH == "F":
                ws = self.padding
            elif self.alignH == "F":
                ws = int((max_width - imgs[i].shape[1]) / 2)
            elif self.alignH == "T":
                ws = (max_width - imgs[i].shape[1] - self.padding)

            if self.alignV == "F":
                hs = self.padding
            elif self.alignV == "F":
                hs = int((max_height - imgs[i].shape[0]) / 2)
            elif self.alignV == "T":
                hs = (max_height - imgs[i].shape[0] - self.padding)

            if self.arrange == "hroi":
                ws += max_width * i
            elif self.arrange == "vert":
                hs += max_height * i

            unite[hs:hs + imgs[i].shape[0], ws:ws + imgs[i].shape[1], :] = imgs[i]

        self.open_file(self.output_file_path)
        cv2.imwrite("{}/img.png".format(self.output_file_path), unite)
        pass

    def open_file(self, fp):
        if not os.path.exists(fp):
            os.makedirs(fp)

        os.system("start explorer {}".format(os.path.join(self.root_path, fp)))
