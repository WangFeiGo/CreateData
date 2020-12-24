#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/18 16:52
# @File     : ExcutePostgreSQL.py
# @Software : PyCharm

import psycopg2

def execute_sql(database,user,password,host,port,executesql):
    conn = psycopg2.connect(database=database,user=user,password=password,host=host,port=port)
    cur = conn.cursor()
    cur.execute(executesql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows