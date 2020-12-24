#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/6 10:51
# @File     : CreateSensitiveData.py
# @Software : PyCharm

import os, re
import random
from common import ReadJSON

xx = "学生会退会"

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

def 来点中文名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(后面垫话) )
    return xx

def 来点英文名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "After",random.choice(前面垫话) )
    xx = xx.replace(  "Before",random.choice(后面垫话) )
    return xx

# def 另起一段():
#     xx = ". "
#     xx += "\r\n"
#     xx += "    "
#     return xx

if __name__ == "__main__":
    readjson = input("请输入字符串为'中文'或者'英文'字样:")
    if readjson == "中文":
        data = ReadJSON.readJSON("config/data_cn.json")
    elif readjson == "英文":
        data = ReadJSON.readJSON("config/data_en.json")
    else:
        print("请输入字符串为'中文'或者'英文'字样！！！")
        exit(0)

    名人名言 = data["famous"]  # a 代表前面垫话，b代表后面垫话
    前面垫话 = data["before"]  # 在名人名言前面弄点废话
    后面垫话 = data['after']  # 在名人名言后面弄点废话
    废话 = data['bosh']  # 代表文章主要废话来源

    下一句废话 = 洗牌遍历(废话)
    下一句名人名言 = 洗牌遍历(名人名言)

    # 将test.txt中的每个汉字变成list的元素
    file = 'params/datas.txt'
    lists = []
    with open(file, "r", encoding='utf-8') as f:
        for line in f:
            lists.extend(str(i) for i in line)
    # 打印一下汉字list
    print(lists)
    xx = len(lists)
    for i in range(xx):
        for j in lists[i]:
            tmp = str()
            # len(tmp) < 100表示控制在100字以内，否则就继续造字
            while ( len(tmp) < 80 ) :
                分支 = random.randint(0,100)
                # if 分支 < 5:
                #     tmp += 另起一段()
                if 分支 < 20 :
                    if readjson == "中文":
                        tmp += 来点中文名人名言()
                    else:
                        tmp += 来点英文名人名言()
                else:
                    tmp += next(下一句废话)
            # 将末尾加上句号
            # tmp = tmp.replace("Exchange",j)+"。"
            if re.compile(u'[\u4e00-\u9fa5]').search(tmp):
                tmp = tmp.replace(",", "。").replace(".", "。")+"。"
                tmp = tmp.replace("，，", "，").replace("。。", "。")
            # 写入article
            if readjson == "中文":
                f = open(os.path.abspath('..') + "\\article\\datas\\" + "Z_article%s.txt" % i, 'w', encoding='utf-8')
                f.write(tmp)
                f.close()
            elif readjson == "英文":
                f = open(os.path.abspath('..') + "\\article\\datas\\" + "E_article%s.txt" % i, 'w', encoding='utf-8')
                f.write(tmp)
                f.close()
            else:
                exit(0)