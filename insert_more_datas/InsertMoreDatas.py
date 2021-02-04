#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/28 22:05
# @File     : InsertMoreDatas.py
# @Software : PyCharm

import os,sys
ENV_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(ENV_DIR)

from common import ExcutePGSQL
import csv

if __name__ == '__main__':

    import time

    dbinfo = {
        "host": "10.20.31.81",
        "user": "postgres",
        "password": "postgres",
        "port": 5432}

    insert_sql = 'INSERT INTO "public"."alert_log_audit_domain"("id", "alert_id", "device_id", "rule_id", "risk", "cap_time", "cap_date", "sip", "sport", "smac", "dip", "dport", "dmac", "module_type", "sub_type", "alert_judge", "disposal_opinion", "disposal_time", "disposer", "insert_time", "judge_verify", "verify_opinion", "verify_time", "verifier", "repeat_num", "mark", "hash", "is_look", "audit_desc", "dns", "domain_ip", "random_key", "inspect_user", "inspect_suggestion", "inspect_time", "dispose_user", "dispose_suggestion", "dispose_time", "operation_status") VALUES '
    values = "(%d, '1603707502440171671', '190801010132', '7016643412405256193', 3, '2020-12-01 18:18:22', '2020-12-01', '10.20.27.31', '55290', '60:08:10:d2:c2:af', '114.114.114.114', '53', '34:6a:c2:67:44:56', 3, 2, -1, NULL, NULL, '', '2020-12-25 09:50:19.544', -1, NULL, '1970-01-01 08:00:00', '', 0, '0', 'a9add315946a5b74046fa65122e4d3b4', 0, NULL, '%s', '{0.0.0.0}', '1608861018558434581', NULL, NULL, NULL, NULL, NULL, '1970-01-01 08:00:00', 0), \n"

    # 读取csv文件内容
    dga_list = []
    with open('dga_black.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dga_list.append(row[0])

    time1 = time.time()
    # 控制插入的数据量，以及id的起始值
    # insert into table ("id", "alert_id") values (1,111),(2,222),(3,333) 高效
    insert_values = "".join([values %(i, dga_list[i]) for i in range(10000)])
    # 拼接sql，把最后的逗号去掉
    sql = insert_sql + insert_values[:-3]+";"
    # print(sql)
    db = ExcutePGSQL.DbConnect(dbinfo, database="threat_status")
    db.execute(sql)
    db.close()
    time2 = time.time()
    print("总过耗时：%s" % (time2-time1))