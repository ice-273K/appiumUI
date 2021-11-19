#!/usr/bin/python3

import pymysql
from Common.Conf.ReadConfig import ReadConfig

class OperateMySql():

    #读取配置文件
    def __init__(self):
        self.cfg = ReadConfig().readcfg()['MySql']

    #连接数据库
    def Connect_Mysql(self,x):
        """
        :param x: 代表第几个数据库，如0是数据库bp_merchants_test，1是bp_management_center_test
        :return:
        """
        conf = self.cfg
        host = conf['host']
        port = conf['port']
        # database = conf['database']
        user = conf['user']
        password = conf['password']
        database = conf['database_name'][x]
        db = pymysql.connect(host=host ,port=port ,user=user,password=password,database=database)
        return db

    #查询操作
    def Select_Mysql(self,sql,x):
        conn = OperateMySql().Connect_Mysql(x)
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results

# a = OperateMySql()
# # b = a.Connect_Mysql(0)
# sql = "SELECT mobile FROM sys_user WHERE mobile = '18091681804' "
# c = a.Select_Mysql(sql,0)
# cv = c.__str__()
# print(c)
# print(cv)