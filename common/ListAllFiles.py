#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/21 18:07
# @File     : ListAllFiles.py
# @Software : PyCharm

import os

def get_file_and_dir(current_address):
    directory = []
    files = []
    for parent, dirnames, filenames in os.walk(current_address):
        # 当前代码的平级文件夹以及子文件夹
        for dirname in dirnames:
            directorypath = parent + "\\" + dirname
            directory.append(directorypath)
        # 当前代码的平级文件以及子文件夹文件
        for filename in filenames:
            filepath = parent + "\\" + filename
            files.append(filepath)
    return  directory,files