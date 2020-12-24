#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/6 10:51
# @File     : ReadJSON.py
# @Software : PyCharm

def readJSON(fileName=""):
    import json
    if fileName!='':
        strList = fileName.split(".")
        if strList[len(strList)-1].lower() == "json":
            with open(fileName,mode='r',encoding="utf-8") as file:
                return json.loads(file.read())