#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/18 16:52
# @File     : ExcutePostgreSQL.py
# @Software : PyCharm

# 添加环境变量
import os,sys
ENV_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(ENV_DIR)

from common import ExcutePostgreSQL

def get_device_id():

    database = "znids_dc"
    user = "postgres"
    password = "postgres"
    host = ["10.20.31.81","10.20.13.20"]
    port = "5432"
    executesql = "SELECT device_id,soft_version FROM public.device_topology_info WHERE device_type = 1"

    try:
        result = ExcutePostgreSQL.execute_sql(database,user,password,host[0],port,executesql)
    except:
        result = ExcutePostgreSQL.execute_sql(database,user,password,host[1],port,executesql)
    head_lsit = []
    for row in result:
       device_id = row[0]
       soft_version = row[1]
       head = "User-Agent:" + device_id + "/" + soft_version + " (ZF)"
       head_lsit.append(head)
    return head_lsit