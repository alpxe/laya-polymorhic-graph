# -*- coding: utf-8 -*-
from __future__ import print_function
from glob import glob

import os
import sys


def protoc(src_dir, dst_dir):
    """编译协议文件

     :param src_dir  .proto 文件目录
     :param dst_dir  python 输出目标目录
     """
    # 检查源目录
    if not os.path.exists(src_dir):
        print(repr(src_dir), 'does not exists.')
        sys.exit(1)

    # 准备目标目录
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

        initpy = os.path.join(dst_dir, '__init__.py')
        if not os.path.exists(initpy):
            with open(initpy, 'w'):
                pass

    # 编译 .proto 文件
    srcfiles = glob(os.path.join(src_dir, '*.proto'))
    command = ' '.join([
        'protoc',
        '-I ' + src_dir,
        '--python_out=' + dst_dir,
        ' '.join(srcfiles),
    ])

    print(command)  # protoc 编译protobuf文件
    os.system(command)

    # sed -i "" -E "s/import ([^ ]*)_pb2/import haha.haha.\1_pb2/g" test.txt
    command = ' '.join([
        "sed",
        "-i ''",
        "-E 's/import ([^ ]*)_pb2/import {0}.\\1_pb2/g'".format(dst_dir.replace('/', '.')),
        dst_dir + '''/*_pb2.py'''
    ])

    print(command)  # sed 命令 替换文件字符串  mac os 命令
    os.system(command)


if __name__ == '__main__':
    outfile = os.path.join('src', 'proto')

    protoc('protofile', outfile)
