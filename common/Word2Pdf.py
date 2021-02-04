#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/17 23:10
# @File     : Word2Pdf.py
# @Software : PyCharm

from win32com.client import Dispatch
from os import walk
import os,time,shutil

wdFormatPDF = 17

def doc2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".doc", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

def docx2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

def get_pdf(word_directory):
    for root, dirs, filenames in walk(word_directory):
        for file in filenames:
            try:
                if file.endswith(".docx"):
                    docx2pdf(str(root + "\\" + file))
                elif file.endswith(".doc"):
                    doc2pdf(str(root + "\\" + file))
            except Exception as e:
                print(e.args)
    time.sleep(5)

# 移动word文件夹下的pdf
def move(word_directory,pdf_directory):
    for pdf in os.listdir(word_directory):
        if pdf.endswith('.pdf'):
            try:
                shutil.move(word_directory + pdf, pdf_directory)
            except Exception as e:
                print(e.args)