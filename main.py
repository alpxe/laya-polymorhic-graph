import os
import cv2
import numpy as np

arrange = "vert"  # 布局方向 hroi vert
alignH = "M"  # 对齐方式 # 头 中 尾 F M T
alignV = "M"

padding = 2  # 边距

all_files = []
imgs = []  # 图片数据
max_height = 0
max_width = 0

for root, dirs, files in os.walk("assets"):
    # self.place_map = files
    all_files = files

all_files.sort()

for img_path in all_files:
    img = cv2.imread("assets/{0}".format(img_path), cv2.IMREAD_UNCHANGED)
    height, width, _ = img.shape
    print("{}x{}".format(width, height))
    if width > max_width:
        max_width = width
    if height > max_height:
        max_height = height

    imgs.append(img)

max_width += padding * 2
max_height += padding * 2

print("max_wdith: {}".format(max_width))
print("max_height: {}".format(max_height))

if arrange == "hroi":
    uw = max_width * len(imgs)
    uh = max_height
elif arrange == "vert":
    uw = max_width
    uh = max_height * len(imgs)

unite = np.zeros([uh, uw, 4], dtype=np.int)
for i in range(len(imgs)):
    hs = int((max_height - imgs[i].shape[0]) / 2)
    ws = int((max_width - imgs[i].shape[1]) / 2)

    if alignH == "F":
        ws = padding
    elif alignH == "F":
        ws = int((max_width - imgs[i].shape[1]) / 2)
    elif alignH == "T":
        ws = (max_width - imgs[i].shape[1] - padding)

    if alignV == "F":
        hs = padding
    elif alignV == "F":
        hs = int((max_height - imgs[i].shape[0]) / 2)
    elif alignV == "T":
        hs = (max_height - imgs[i].shape[0] - padding)

    if arrange == "hroi":
        ws += max_width * i
    elif arrange == "vert":
        hs += max_height * i

    unite[hs:hs + imgs[i].shape[0], ws:ws + imgs[i].shape[1], :] = imgs[i]

cv2.imwrite("out/img.png", unite)
