#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/9 16:13
# @File     : ListDictionary.py
# @Software : PyCharm

keys = []

# 把嵌套字典的key取出来
def list_dictionary(data, n_tab=-1):
    if isinstance(data, list):
        for i in data:
            list_dictionary(i, n_tab)
    elif isinstance(data, dict):
        n_tab += 1
        for key, value in data.items():
            list_dictionary(value, n_tab)
            keys.append(key)
    return keys