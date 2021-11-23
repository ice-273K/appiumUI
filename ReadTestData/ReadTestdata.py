#!/usr/bin/python3

"""
读取测试数据
"""

import os
import yaml
# from ruamel import yaml
class ReadTestdata():
    @classmethod
    def readtestdata_01(cls):
        path = os.path.dirname(__file__)
        yaml_file = os.path.join(path,"testdata01.yaml")
        with open(yaml_file,'r',encoding='utf-8',errors='ignore') as f:
            testdata_01 = yaml.safe_load(f)
            # print('testdata_01aa')
            return testdata_01

    @classmethod
    def readtestdata_02(cls):
        path = os.path.dirname(__file__)
        yaml_file = os.path.join(path,"testdata02.yaml")
        with open(yaml_file,'r',encoding='utf-8',errors='ignore') as f:
            testdata_02 = yaml.safe_load(f)
            return testdata_02






# a = ReadTestdata()
# b = a.readtestdata_01()
# c = a.readtestdata_02()
# print(b)
# print(c)
