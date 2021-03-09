#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2021/2/7 11:42
# @File     : Tqdm.py
# @Software : PyCharm

from time import sleep
from tqdm import trange

# 显示了10个进度条
for i in trange(10):
    sleep(0.5)