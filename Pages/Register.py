#!/usr/bin/python3

from time import sleep
from Common.ConBaseOperate.FindElement import FindElement
from Common.ReadTestData.ReadTestdata import ReadTestdata
from Common.ConBaseOperate.RandomPhone import RandomPhone
from Common.DataBaseLib.OperateRedis import OperateRedis
from Common.ReadTestData.WriteTestdata import WriteTestdata
from Common.ConBaseOperate.Screenshot import Screenshot

class Register(FindElement):

    testdata = ReadTestdata.readtestdata_01()['Register']

    # 点击app
    def startApp(self):
        print(self.testdata['startApp'])
        return self.findByText(self.testdata['startApp']).click()

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
        self.waitAttriID(self.testdata['et_phone_num'])
        return self.sendkeysID(self.testdata['et_phone_num'],self.testdata['phone_num'])

    #输入手机号：已注册
    def et_phone_num_registered(self):
        self.waitAttriID(self.testdata['et_phone_num'])
        self.testdata = ReadTestdata().readtestdata_01()['Register']
        return self.sendkeysID(self.testdata['et_phone_num'],self.testdata['phone_num_registered'])

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

    #截图
    def get_screen(self):
        # return Screenshot().get_screenshot(image='UserExist.png')
        return self.get_screenshot_string(image='UserExist.png')

