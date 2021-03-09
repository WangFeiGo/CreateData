#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2021/3/8 16:12
# @File     : GetBaiDuDownloadUrl.py
# @Software : PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re,os

def excute_get_url():
    theme = str(input("请输入关键字:"))
    document_type = int(input("请输入要造的文件类型(阿拉伯数字): \n 0-->全部 \n 1-->doc \n 2-->pdf \n 3-->ppt \n 4-->xls \n 5-->txt \n"))
    times = int(input("请输入要造的文件数量(阿拉伯数字): \n >=20，且必须是10的整数倍 \n"))

    # 无头
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)

    url_all_list = []
    try:
        for i in range(0,times,10):
            browser.get('https://wenku.baidu.com/search?word=%s&org=0&fd=0&lm=%d&od=0&ie=gbk&fr=searchBox&pn=%d' %(theme,document_type,i))
            html = browser.page_source
            url_list = re.findall('https://wenku.baidu.com/view(.*?)search',html)
            url_list = [ "https://wenku.baidu.com/view" + url + 'search' for url in url_list ]
            url_all_list = url_all_list + url_list
    except:
        print("已经超出文库的范围了")
    finally:
        browser.close()
    # 写入
    with open(os.path.abspath('..') + '\\utils\\GetBaiDuDownloadUrl\\urls.txt', 'w') as f:
        for url in url_all_list:
            f.write(url)
            f.write('\n')

if __name__ == '__main__':
    excute_get_url()