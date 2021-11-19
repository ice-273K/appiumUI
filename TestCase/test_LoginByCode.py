#!/usr/bin/python3
from time import sleep
from Pages.LoginByCode import LoginByCode
from Common.ConBaseOperate.FindElement import FindElement

class Test_LoginByCode():

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


