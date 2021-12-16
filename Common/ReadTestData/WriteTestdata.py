#!/usr/bin/python3
"""
写入数据
"""
import os
from ruamel import yaml
from Common.ReadTestData.ReadTestdata import ReadTestdata

class WriteTestdata():

    def writetestdata_01(self,key,value,k):
        """
        :param key: 指字典里的键值如Register 里的startApp
        :param value: 指要写入的值
        :param k: 代表全字典里的第1个值，如LoginApp，Register
        :return:
        """
        path = os.path.dirname(__file__)
        yaml_file = os.path.join(path,"testdata01.yaml")
        with open(yaml_file,'r',encoding='utf-8',errors='ignore') as f:
            testdata_01 = yaml.round_trip_load(f)
            testdata_01_new = testdata_01[k]
            testdata_01_new[key] = value
        with open(yaml_file,'w',encoding='utf-8',errors='ignore') as f:
            yaml.round_trip_dump(testdata_01,f, default_flow_style=False)
            return testdata_01





# s = WriteTestdata()
# k = 'Register'
# key = 'phone_num'
# value = '12'
# t = s.writetestdata_01(key=key,value=value,k=k)
# print(t['StartApp']['qqbtn'])
