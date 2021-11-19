#!/usr/bin/python3
from time import sleep

from Common.ConBaseOperate.FindElement import FindElement
from Common.DataBaseLib.OperateRedis import OperateRedis
from ReadTestData.ReadTestdata import ReadTestdata

class LoginByCode(FindElement):

    testdata = ReadTestdata.readtestdata_01()['LoginByCode']

    #选择APP
    def startApp(self):
        return self.findByAccessibilityId(self.testdata['startApp']).click()

    #选择手机登录
    def iv_phone(self):
        self.waitAttriID(self.testdata['iv_phone'])
        return self.findById(self.testdata['iv_phone']).click()

    #点击编辑框
    def et_phone_num(self):
        return self.findById(self.testdata['et_phone_num']).click()

    #输入手机号
    def sendphone(self):
        self.waitAttriID(self.testdata['et_phone_num'])
        return self.sendkeysID(self.testdata['et_phone_num'],self.testdata['sendphone'])

    #点击获取验证码
    def btn_code(self):
        return self.findById(self.testdata['btn_code']).click()

    #点击输入验证码编辑框
    def code_inputfield(self):
        return self.findByXpath(self.testdata['code_inputfield']).click()

    #清除手机验证码
    def clear_code(self):
        self.waitAttriXpath(self.testdata['code_inputfield'])
        return self.findByXpath(self.testdata['code_inputfield']).clear()

    #输入手机验证码
    def sendCode(self):
        sleep(5)
        FindElement().graph_getCode()
        self.code = LoginByCode().getCode()
        return self.sendkeysXpath(self.testdata['code_inputfield'],self.code)

    #输入手机验证码部分
    def sendCodeh(self):
        sleep(5)
        FindElement().graph_getCode()
        self.code = "1"
        return self.sendkeysXpath(self.testdata['code_inputfield'],self.code)

    #获取手机验证码
    @classmethod
    def getCode(cls):
        phone = cls.testdata['sendphone']
        s = OperateRedis()
        return s.Get_Login(phone)

    #退出-点击我的控件
    def ll_user(self):
        self.waitAttriID(self.testdata['ll_user'])
        return self.findById(self.testdata['ll_user']).click()

    #点击退出登录
    def btn_logout(self):
        self.waitAttriID(self.testdata['btn_logout'])
        return self.findById(self.testdata['btn_logout']).click()

    #确定退出
    def btn_confirm(self):
        self.waitAttriID(self.testdata['btn_confirm'])
        return self.findById(self.testdata['btn_confirm']).click()

#调试前置代码
# FindElement().restartApp()
# # testdata = ReadTestdata.readtestdata_01()['LoginByCode']['startApp']
# s = LoginByCode()
# s.startApp()
# s.iv_phone()
# s.sendphone()
# s.btn_code()
# s.graph_code()
# sleep(2)
# sv = s.getCode()
# print(sv)
# s.clear_phone()
# s.sendCode()
# # print(sv)
# FindElement.quite()