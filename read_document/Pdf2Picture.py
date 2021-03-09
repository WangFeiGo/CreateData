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

from common import Pdf2Picture

if __name__ == "__main__":
    pdfPath = os.path.abspath('..')+"\\read_document\\datas\\pdf"
    imagePath = os.path.abspath('..')+"\\read_document\\datas\\image"
    Pdf2Picture.pdf2picture(pdfPath, imagePath)