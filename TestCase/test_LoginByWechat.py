#!/usr/bin/python3
from time import sleep

from Pages.LoginByWechat import LoginByWechat
from Common.ConBaseOperate.FindElement import FindElement

class Test_LoginByWechat():

    def setup_method(self):
        FindElement.restartApp()

    def teardown_method(self):
        FindElement.quite()

    #正常登录
    def test_login(self):
        s = LoginByWechat()
        s.startApp()
        s.iv_wechat()
        s.et_account()
        s.sendaccount()
        s.et_password()
        s.sendpsw()
        s.erp()
        sleep(5)

    #用户名密码错误
    def test_login_err(self):
        s = LoginByWechat()
        s.startApp()
        s.iv_wechat()
        s.et_account()
        s.sendaccount()
        s.et_password()
        s.sendpsw()
        s.erp()
        assert s.msg_wrong()=="帐号或密码错误，请重新填写。"
        s.ffp()