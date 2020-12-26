#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : wangfei
# @Time     : 2020/12/9 10:54
# @File     : CreateSensitiveData.py
# @Software : PyCharm

# 添加环境变量
import os,sys
ENV_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(ENV_DIR)

import json
import random
from common import ReadJSON
import datetime
from read_document.CreateReadDocumentData import CreateReadDocumentData
import hashlib
import docx
from sxm_alert import ReadPostgreSQL

class CreateSensitiveData(CreateReadDocumentData) :

    def __init__(self):
        super(CreateSensitiveData, self).__init__()
        self.config_data = ReadJSON.readJSON(os.path.abspath('..') + "\\sxm_alert\\config" + "\\data.json")
        self.data_alarm = ReadJSON.readJSON(os.path.abspath('..') + "\\sxm_alert\\params" + "\\data_alarm.json")
        self.data_filedesc = ReadJSON.readJSON(os.path.abspath('..') + "\\sxm_alert\\params" + "\\data_filedesc.json")
        # 公共字段
        self.head = random.choice(ReadPostgreSQL.get_device_id()) # 获取两个txt文件的头部
        self.jxq_id = self.head.split("/")[0][11:] # 检测器id
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # time根据当前时间戳，单独赋值
        self.id = ''.join(random.choices('0123456789',k = 19)) # 取19位随机数
        self.document = self.create_document()  # 首先创建doc，从而可以获取doc的md5，共32位
        # 读取doc
        self.file = docx.Document(os.path.abspath('..') + "\\sxm_alert\\datas\\" + "sensitive.doc")
        # 把doc存入list
        self.all_contents_list = []
        for param in self.file.paragraphs:
            self.all_contents_list.append(param.text)
            # 把list放入str
            self.all_contents = ''.join(self.all_contents_list)
        # 文件前400字节
        self.sm_summary = self.all_contents[0:200]
        # 获取关键所在的位置
        self.index = self.all_contents.find(self.key_words)
        # 关键词上下内容1024字节,相当于500个汉字
        self.sm_desc = self.all_contents[0:self.index] + self.all_contents[self.index:self.index+250]

        # 取alarm的值
        self.list_data_alrm = []
        for i in self.data_alarm:
            if i == "app_opt":
                # 解决json嵌套的值
                for j in self.data_alarm[i]:
                    self.data_alarm[i][j] = random.choice(self.config_data.get(j))
            else:
                self.data_alarm[i] = random.choice(self.config_data.get(i))
                # 更改变量
                self.data_alarm["time"] = self.time
                self.data_alarm["id"] = self.id
                self.data_alarm["sm_zf_highlight"] = self.key_words
                self.data_alarm["sm_summary"] = self.sm_summary
                self.data_alarm["sm_desc"] = self.sm_desc

        self.list_data_alrm.append(self.data_alarm)

        # 取filedesc的值
        for x in self.data_filedesc:
            self.data_filedesc[x] = random.choice(self.config_data.get(x))
            # 更改变量
            self.data_filedesc["time"] = self.time
            self.data_filedesc["id"] = self.id
            # 读取byte，获取md5
            self.data_filedesc["checksum"] = self.get_file_md5(os.path.abspath('..') + "\\sxm_alert\\datas\\" +"sensitive.doc")
            self.data_filedesc["filetype"] = "doc"
            self.data_filedesc["filename"] = "file_" + self.jxq_id + "_" + self.id + "_" + self.data_filedesc["checksum"] + "." + self.data_filedesc["filetype"]

    # 创建doc文件
    def create_document(self):
        run_doc = CreateReadDocumentData()
        # 防止子类重新实例化，直接获取父类的变量
        self.key_words = run_doc.key_words
        run_doc.create_header()
        run_doc.create_big_title()
        run_doc.create_small_title()
        run_doc.create_document_title()
        run_doc.create_document_content()
        run_doc.save("\\sxm_alert\\datas\\" + "sensitive")

    def get_file_md5(self,file_path):
        """
        获取文件md5值
        :param file_path: 文件路径名
        :return: 文件md5值
        """
        with open(file_path, "rb") as f:
            md5obj = hashlib.md5()
            md5obj.update(f.read())
            _hash = md5obj.hexdigest()
        return str(_hash).upper()

    def save_data_alarm(self):
        f = open(os.path.abspath('..') + "\\sxm_alert\\datas\\" + "sensitive_alarm_%s.txt" % self.id, 'w', encoding='utf-8')
        # 暂时部分写死
        f.write(self.head + "\n")
        f.write("Type:sensitive(encryption_file)\n\n")
        f.write((str(self.list_data_alrm)))
        f.close()

    def save_data_filedesc(self):
        f = open(os.path.abspath('..') + "\\sxm_alert\\datas\\" + "sensitive_filedesc_%s.txt" % self.id, 'w', encoding='utf-8')
        # 暂时部分写死
        f.write(self.head  + "\n\n")
        # python的False，变成false，需要序列化
        f.write(json.dumps(self.data_filedesc))
        f.close()

if __name__ == "__main__":

    times = int(input("请输入要造的文件数量(阿拉伯数字):"))

    for i in range(times):
        run = CreateSensitiveData()
        run.save_data_alarm()
        run.save_data_filedesc()
        # 重命名doc文件名
        os.rename(os.path.abspath('..') + "\\sxm_alert\\datas\\" + "sensitive.doc",
                  os.path.abspath('..') + "\\sxm_alert\\datas\\" + "sensitive_" + run.data_filedesc["filename"])