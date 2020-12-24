#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/22 9:28
# @File     : LargeDoc.py
# @Software : PyCharm

from read_document.CreateReadDocumentData import CreateReadDocumentData
import time,hashlib

# 根据时间戳，生成md5
def create_md5():
    # hash前必须把数据转换成bytes类型
    now = str(time.time()).encode("utf-8")
    md5hash = hashlib.md5(now)
    md5 = md5hash.hexdigest()
    return md5

# 创建doc文件
def create_document():
    run_doc = CreateReadDocumentData()
    run_doc.create_header()
    run_doc.create_big_title()
    run_doc.create_small_title()
    run_doc.create_document_title()
    # 1000 ，word 047K，pdf 01M
    # 10000，word 129K，pdf 07M
    # 20000，word 209K，pdf 14M
    # 30000，word 295K，pdf 21M
    # 40000，word 402K，pdf 28M
    for i in range(10000):
        run_doc.create_document_content()
    run_doc.save("\\word2pdf\\datas\\word\\"+create_md5()+"_"+str(i))

if __name__ == "__main__":
    create_document()