#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2021/2/4 9:54
# @File     : UploadDocToFtp.py
# @Software : PyCharm

# 添加环境变量
import os,sys
ENV_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(ENV_DIR)

from read_document.CreateReadDocumentData import CreateReadDocumentData
from common.FtpToFile import FtpToFile
import shutil

if __name__ == "__main__":

    times = int(input("请输入要造的文件数量(阿拉伯数字):"))

    for i in range(times):
        run_doc = CreateReadDocumentData()
        # 防止子类重新实例化，直接获取父类的变量
        key_words = run_doc.key_words
        run_doc.create_header()
        run_doc.create_big_title()
        run_doc.create_small_title()
        run_doc.create_document_title()
        run_doc.create_document_content()
        local_doc_name = "\\read_document\\datas\\word\\" + str(i) + "_" + run_doc.article_title + "_" + run_doc.key_words
        run_doc.save(local_doc_name)

        # 移动word到upload文件夹下
        src_doc_name = "\\read_document\\datas\\upload\\" + str(i) + "_" + run_doc.article_title + "_" + run_doc.key_words
        local_doc = os.path.abspath('..') + local_doc_name + ".doc"
        upload_doc = os.path.abspath('..') + src_doc_name + ".doc"
        shutil.move(local_doc, upload_doc)

        # 上传upload文件夹下对应的文件
        my_ftp = FtpToFile("10.20.10.211")
        my_ftp.login("administrator", "Njzf1984!(*$")
        my_ftp.upload_file_tree(os.path.abspath('..')+"\\read_document\\datas\\upload\\", "/wangfei/")
        my_ftp.close()

        # 删除upload文件夹下对应的文件
        if os.path.exists(upload_doc):
            os.remove(upload_doc)
        else:
            print('no such file:%s' % upload_doc)