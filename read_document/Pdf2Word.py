#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2021/3/9 13:54
# @File     : Pdf2Picture.py
# @Software : PyCharm

# 添加环境变量
import os,sys
ENV_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(ENV_DIR)

from common import Pdf2Word

if __name__ == "__main__":
    pdf_folder = os.path.abspath('..')+"\\read_document\\datas\\pdf"
    word_folder = os.path.abspath('..')+"\\read_document\\datas\\word"
    Pdf2Word.main(pdf_folder,word_folder)