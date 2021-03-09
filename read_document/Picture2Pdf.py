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

from common import Picture2Pdf

if __name__ == "__main__":
    imagePath = os.path.abspath('..')+"\\read_document\\datas\\image"
    Picture2Pdf.pic2pdf(imagePath)