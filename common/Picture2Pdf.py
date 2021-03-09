#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2021/3/9 14:48
# @File     : Picture2Pdf.py
# @Software : PyCharm

import glob
import os
import fitz

def pic2pdf(img_dir):
    doc = fitz.open()
    # 读取图片，确保按文件名排序
    for img in sorted(glob.glob("{}/*".format(img_dir))):
        print(img)
        # 打开图片
        imgdoc = fitz.open(img)
        # 使用图片创建单页的 PDF
        pdfbytes = imgdoc.convertToPDF()
        imgpdf = fitz.open("pdf", pdfbytes)
        # 将当前页插入文档
        doc.insertPDF(imgpdf)
    # 获取首个图片的名称
    pictureFileList = os.listdir(img_dir)
    firstImageName = pictureFileList[0]
    pdfFileName = os.path.splitext(firstImageName)[0] + ".pdf"
    # pdf保存的路径
    collect_pdf_path = img_dir + "\\pdf"
    if not os.path.exists(collect_pdf_path):
        os.makedirs(collect_pdf_path)
    pdfFilePath = collect_pdf_path + "\\" + pdfFileName
    # 保存
    if os.path.exists(pdfFilePath):
        os.remove(pdfFilePath)
    doc.save(pdfFilePath)
    doc.close()