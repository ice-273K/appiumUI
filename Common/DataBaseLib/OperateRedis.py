#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
连接redis并返回值
"""

import redis
from Common.Conf import ReadConfig

class OperateRedis():
    #读取配置信息
    def __init__(self):
        self.cfg = ReadConfig.ReadConfig().readcfg()['Redis']

    #连接数据库
    def Connect_Redis(self):
        conf = self.cfg
        host = conf['host']
        port = conf['port']
        db = conf['db']
        pool = redis.ConnectionPool(host = host, port = port, db = db, decode_responses=True, encoding_errors='ignore')
        return redis.Redis(connection_pool=pool)

    #获取验证码_登录验证码
    def Get_Login(self,key):
        # 获取配置文件中的值
        conf = self.cfg
        key_LOGIN = conf['key_LOGIN']
        # 调用连接数据库函数
        return self.Connect_Redis().getrange(key_LOGIN+key,-6,-1)

    # 获取验证码_注册验证码
    def Get_Sign(self,key):
        #获取配置文件中的值
        conf = self.cfg
        key_SINGN_UP = conf['key_SINGN_UP']
        #调用连接数据库函数
        self.conn = self.Connect_Redis()
        return self.conn.getrange(key_SINGN_UP+key,-6,-1)

    # 获取验证码_忘记密码验证码
    def Get_ForgetPsw(self,key):
        #获取配置文件中的值
        conf = self.cfg
        key_FORGET_PASSWORD = conf['key_FORGET_PASSWORD']
        # 调用连接数据库函数
        self.conn = self.Connect_Redis()
        return self.conn.getrange(key_FORGET_PASSWORD+key,-6,-1)


# a = OperateRedis()
# # b = a.Connect_Redis()
# c = a.Get_Login("15822608183")
# print(c)
