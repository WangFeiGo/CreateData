#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/18 16:52
# @File     : ReadPostgreSQL.py
# @Software : PyCharm

# 添加环境变量
import os,sys
ENV_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(ENV_DIR)

from common import ExcutePGSQL

def get_device_id():

    dbinfo = {
        "host": "10.20.31.81",  # 内网
        # "host": "10.20.13.20", # 外网
        "user": "postgres",
        "password": "postgres",
        "port": 5432}

    try:
        sql = "SELECT device_id,soft_version FROM public.device_topology_info WHERE device_type = 1"
        db = ExcutePGSQL.DbConnect(dbinfo, database="znids_dc")
        result = db.select(sql)
        db.close()
        head_lsit = []
        for row in result:
            device_id = row[0]
            soft_version = row[1]
            head = "User-Agent:" + device_id + "/" + soft_version + " (ZF)"
            head_lsit.append(head)
        return head_lsit
    except Exception as e:
        print(e.args)