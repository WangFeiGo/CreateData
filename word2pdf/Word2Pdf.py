#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/17 23:10
# @File     : Word2Pdf.py
# @Software : PyCharm

import os
from common import Word2Pdf

if __name__ == "__main__":
    word_directory = os.path.abspath('..')+"\\word2pdf\\datas\\word\\"
    pdf_directory = os.path.abspath('..')+"\\word2pdf\\datas\\pdf\\"
    Word2Pdf.get_pdf(word_directory)
    Word2Pdf.move(word_directory,pdf_directory)