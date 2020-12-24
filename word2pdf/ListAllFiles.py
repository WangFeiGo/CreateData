#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/21 18:07
# @File     : ListAllFiles.py
# @Software : PyCharm

import os
from common import ListAllFiles

if __name__ == "__main__":
    # 当前文件所在的文件夹的位置
    current_address = os.path.dirname(os.path.abspath(__file__))
    files = ListAllFiles.get_file_and_dir(current_address)[1]
    # 重命名文件夹下所有doc文件，且移动到当前目录
    [os.rename(doc,doc[47:].replace("\\","_")) for doc in files if doc.endswith('.doc')]