#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2021/3/9 13:54
# @File     : Pdf2Picture.py
# @Software : PyCharm

import fitz
import os

def pdf2picture(pdfPath, imagePath):
    print("imagePath=" + imagePath)
    pdfFileList = os.listdir(pdfPath)
    for pdfFile in pdfFileList:
        pdfFilePath = pdfPath + "\\" + pdfFile
        if pdfFilePath.endswith('.pdf'):
            pdfDoc = fitz.open(pdfFilePath)
            for pg in range(pdfDoc.pageCount):
                page = pdfDoc[pg]
                rotate = int(0)
                # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像
                # 此处若是不做设置，默认图片大小为：792X612, dpi=96
                # (1.33333333-->1056x816)   (2-->1584x1224)
                zoom_x = 1.33333333
                zoom_y = 1.33333333
                mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
                pix = page.getPixmap(matrix=mat, alpha=False)
                # 判断存放图片的文件夹是否存在，若图片文件夹不存在就创建
                if not os.path.exists(imagePath):
                    os.makedirs(imagePath)
                # 将图片写入指定的文件夹内
                pix.writePNG(imagePath + '/' + os.path.splitext(pdfFile)[0] + '_%s.png' % pg)