#!/usr/bin/python3
from time import sleep

from Common.ConBaseOperate.FindElement import FindElement
from Common.DataBaseLib.OperateRedis import OperateRedis
from ReadTestData.ReadTestdata import ReadTestdata

class ForgetPassword(FindElement):

    testdata = ReadTestdata.readtestdata_01()['ForgetPassword']
    # 选择APP
    def startApp(self):
        return self.findByAccessibilityId(self.testdata['startApp']).click()

    #选择忘记密码
    def tv_forget_password(self):
        self.waitAttriID(self.testdata['tv_forget_password'])
        return self.findById(self.testdata['tv_forget_password']).click()

    #输入手机号
    def send_et_phone_num(self):
        self.waitAttriID(self.testdata['et_phone_num'])
        return self.sendkeysID(self.testdata['et_phone_num'],self.testdata['phone_num'])

    #点击获取验证码
    def btn_getcode(self):
        return self.findById(self.testdata['btn_getcode']).click()

    #输入手机验证码
    def sendCode(self):
        FindElement().graph_getCode()
        self.code = ForgetPassword().getCode()
        sleep(5)
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
        phone = cls.testdata['phone_num']
        s = OperateRedis()
        return s.Get_ForgetPsw(phone)

    #清除手机验证码
    def clear_code(self):
        return self.findByXpath(self.testdata['code_inputfield']).clear()

    #输入新密码
    def et_new_password(self):
        self.waitAttriID(self.testdata['et_new_password'])
        return self.sendkeysID(self.testdata['et_new_password'],self.testdata['new_password'])

    #查看新密码
    def new_password_eye(self):
        return self.findById(self.testdata['new_password_eye']).click()

    #确认新密码输入
    def et_ensure_password(self):
        return self.sendkeysID(self.testdata['et_ensure_password'],self.testdata['ensure_password'])

    #查看确认的密码
    def ensure_password_eye(self):
        return self.findById(self.testdata['ensure_password_eye']).click()

    #点击确定
    def btn_ensure(self):
        return self.findById(self.testdata['btn_ensure']).click()


