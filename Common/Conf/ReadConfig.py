#!/usr/bin/python3
"""
读取配置信息等
"""

import os
import yaml


class ReadConfig():
    @classmethod
    def readcfg(cls):
        path = os.path.dirname(__file__)
        yaml_file = os.path.join(path,"config.yaml")
        with open(yaml_file,'r',encoding='utf-8',errors='ignore') as f:
            cfg = yaml.safe_load(f)
            return cfg


# a = ReadConfig()
# b = a.readRedis()
# c = a.readAndroidClient()
# print(b)
# print(c)

