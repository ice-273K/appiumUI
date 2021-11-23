#!/usr/bin/python3

from time import sleep
from Common.ConBaseOperate.FindElement import FindElement
from ReadTestData.ReadTestdata import ReadTestdata
from Common.ConBaseOperate.RandomPhone import RandomPhone
from Common.DataBaseLib.OperateRedis import OperateRedis
from ReadTestData.WriteTestdata import WriteTestdata

class Register(FindElement):

    testdata = ReadTestdata.readtestdata_01()['Register']

    # 点击app
    def startApp(self):
        print(self.testdata['startApp'])
        return self.findByAccessibilityId(self.testdata['startApp']).click()

    #点击立即注册
    def tv_register(self):
        self.waitAttriID(self.testdata['tv_register'])
        return self.findById(self.testdata['tv_register']).click()

    #输入手机号
    def et_phone_num(self):
        phone = RandomPhone().Unregistered_Phone()  #随机生成手机号
        print(phone)
        WriteTestdata().writetestdata_01(key='phone_num', value=phone, k='Register')  # 写入
        self.testdata=ReadTestdata().readtestdata_01()['Register']  #重新读取数据（注意：写数据后，必须重新读取，否则读取的是老数据）
        return self.sendkeysID(self.testdata['et_phone_num'],self.testdata['phone_num'])

    #清除手机号
    def clear_phone(self):
        return self.findByXpath(self.testdata['clear_phone']).click()

    #点击获取验证码
    def btn_getcode(self):
        sleep(10)
        return self.findById(self.testdata['btn_getcode']).click()

    #关闭验证码
    def iv_close(self):
        self.waitAttriID(self.testdata['iv_close'])
        return self.findById(self.testdata['iv_close']).click()

    #刷新图形验证码
    def iv_refresh(self):
        self.waitAttriID(self.testdata['iv_refresh'])
        return self.findById(self.testdata['iv_refresh']).click()

    #图形验证码
    def graph_getCode(self):
        FindElement().graph_getCode()

    #填写手机验证码
    def edit_code(self):
        phone = self.testdata['phone_num']
        code = OperateRedis().Get_Sign(phone)       #获取验证码
        WriteTestdata().writetestdata_01(key='code', value=code, k='Register')  # 写入
        self.testdata = ReadTestdata().readtestdata_01()['Register']    #重新读取
        self.waitAttriXpath(self.testdata['edit_code'])
        return self.sendkeysXpath(self.testdata['edit_code'],self.testdata['code'])

    #填写真实姓名
    def et_real_name(self):
        self.waitAttriID(self.testdata['et_real_name'])
        return self.sendkeysID(self.testdata['et_real_name'],self.testdata['real_name'])

    #填写密码
    def et_password(self):
        return self.sendkeysID(self.testdata['et_password'],self.testdata['password'])

    #查看密码
    def iv_eye(self):
        return self.findById(self.testdata['iv_eye']).click()

    #点击注册
    def btn_register(self):
        self.waitAttriID(self.testdata['btn_register'])
        return self.findById(self.testdata['btn_register']).click()

FindElement().restartApp()
a = Register()
a.startApp()
# a.et_phone_num()
# a.btn_getcode()
# a.graph_getCode()
# sleep(3)
# a.edit_code()
FindElement.quite()