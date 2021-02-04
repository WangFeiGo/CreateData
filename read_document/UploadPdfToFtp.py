#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2021/2/4 9:54
# @File     : UploadPdfToFtp.py
# @Software : PyCharm

# 添加环境变量
import os,sys
ENV_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(ENV_DIR)

from read_document.CreateReadDocumentData import CreateReadDocumentData
from common.FtpToFile import FtpToFile
import shutil
from common import Word2Pdf

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
        local_doc = os.path.abspath('..') + local_doc_name + ".doc"

        # 生成pdf
        word_directory = os.path.abspath('..') + "\\read_document\\datas\\word\\"
        pdf_directory = os.path.abspath('..') + "\\read_document\\datas\\pdf\\"
        Word2Pdf.get_pdf(word_directory)
        Word2Pdf.move(word_directory, pdf_directory)
        local_pdf_name = "\\read_document\\datas\\pdf\\" + str(i) + "_" + run_doc.article_title + "_" + run_doc.key_words

        # 删除word
        if os.path.exists(local_doc):
            os.remove(local_doc)
        else:
            print('no such file:%s' % local_doc)

        # 移动pdf到upload文件夹下
        src_pdf_name = "\\read_document\\datas\\upload\\" + str(i) + "_" + run_doc.article_title + "_" + run_doc.key_words
        local_pdf = os.path.abspath('..') + local_pdf_name + ".pdf"
        upload_pdf = os.path.abspath('..') + src_pdf_name + ".pdf"
        shutil.move(local_pdf, upload_pdf)

        # 上传upload文件夹下对应的文件
        my_ftp = FtpToFile("10.20.10.211")
        my_ftp.login("administrator", "Njzf1984!(*$")
        my_ftp.upload_file_tree(os.path.abspath('..')+"\\read_document\\datas\\upload\\", "/wangfei/")
        my_ftp.close()

        # 删除upload文件夹下对应的文件
        if os.path.exists(upload_pdf):
            os.remove(upload_pdf)
        else:
            print('no such file:%s' % upload_pdf)

