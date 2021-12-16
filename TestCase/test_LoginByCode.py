#!/usr/bin/python3
from time import sleep
from Pages.LoginByCode import LoginByCode
from Common.ConBaseOperate.FindElement import FindElement
from Common.ReadTestData.ReadTestdata import ReadTestdata

class Test_LoginByCode():

    testdata = ReadTestdata().readtestdata_01()['LoginByCode']

    def setup_method(self):
        FindElement.restartApp()

    def teardown_method(self):
        FindElement.quite()

    #点击app-》选择手机号登录-》点击输入手机号栏-》填写手机号-》点击获取验证码-》输入验证码-》我的-》退出登录
    def test_login_code(self):
        s = LoginByCode()
        s.startApp()
        s.iv_phone()
        s.sendphone()
        s.btn_code()
        s.sendCodeh()
        s.clear_code()
        s.sendCode()
        s.ll_user()
        s.btn_logout()
        s.btn_confirm()

    #未注册:点击app-》选择手机号登录-》点击输入手机号栏-》填写手机号(未注册)-》点击获取验证码-》图形验证码->截图
    def test_unregister(self):
        s = LoginByCode()
        s.startApp()
        s.iv_phone()
        s.send_unregister_phone()
        s.btn_code()
        s.graph_getCode()
        t = s.get_screenshot()
        #断言（暂时获取不到弹窗信息）
        text = '用户不存在'
        assert text in t
