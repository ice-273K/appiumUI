#!/usr/bin/python3

import random
from Common.DataBaseLib.OperateMySql import OperateMySql

class RandomPhone():

    #随机生成手机号
    def Random_Num(self):
        num = random.randrange(1000000,9999999)
        phone = "1500" + str(num)
        return phone

    #随机生成未注册的手机号
    def Unregistered_Phone(self):
        phone = RandomPhone().Random_Num()
        sql = 'SELECT mobile FROM sys_user WHERE mobile = %s'%(phone)
        mysql = OperateMySql().Select_Mysql(sql,0)
        i = 0
        while len(mysql)!=0:
            phone = RandomPhone().Random_Num()
            sql = 'SELECT mobile FROM sys_user WHERE mobile = %s' % (phone)
            mysql = OperateMySql().Select_Mysql(sql, 0)
            len(mysql)
            i = i+1
            print(i)
        else:
            return phone

# a = RandomPhone()
# # p = a.Random_Num()
# b = a.Unregistered_Phone()
# print(b)
# print(p)
