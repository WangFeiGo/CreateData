#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/28 15:36
# @File     : ExcutePGSQL.py
# @Software : PyCharm

import psycopg2

class DbConnect():

    def __init__(self, db_cof, database=""):
        self.db_cof = db_cof
        # 建立连接
        self.db = psycopg2.connect(database=database,**db_cof)
        self.cursor = self.db.cursor()

    def select(self, sql):
        # select
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # insert、delete、update
        try:
           self.cursor.execute(sql)
           self.db.commit()
        except:
           # 发生错误时回滚
           self.db.rollback()

    def close(self):
        self.db.close()