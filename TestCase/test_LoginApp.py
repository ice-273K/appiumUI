#!/usr/bin/python3

from Pages.LoginApp import LoginApp
from Common.ConBaseOperate.FindElement import FindElement
from ReadTestData.ReadTestdata import ReadTestdata

class Test_LoginApp():
    testdata = ReadTestdata.readtestdata_01()['LoginApp']
    def setup_method(self):
        FindElement.restartApp()

    def teardown_method(self):
        FindElement.quite()

    #用户名密码登录
    def test_login_psw(self):
        s = LoginApp()
        s.startApp()
        s.et_phone_num()
        s.sendPhone()
        s.btn_clearphone()
        s.sendPhone()
        s.et_password()
        s.sendPsw()
        s.btn_clearpws()
        s.sendPsw()
        s.iv_eye()
        s.btn_login()
        s.ll_user()
        s.btn_logout()
        s.btn_cancel()
        s.btn_logout()
        s.btn_confirm()

    # # 手机号错误
    # def test_wrong_phone(self):
    #     s = LoginApp()
    #     s.startApp()
    #     s.et_phone_num()
    #     s.sendPhoneW()
    #     s.sendPsw()
    #     s.btn_login()
    #     text = "请输入正确手机号"
    #     t = s.toast(self.testdata['Toastxpath'],"text")
    #     assert t == text
    #
    # # 密码格式错误
    # def test_wrong_password(self):
    #     s = LoginApp()
    #     s.startApp()
    #     s.et_phone_num()
    #     s.sendPhone()
    #     s.sendPswW()
    #     s.btn_login()
    #     text = "请输入正确密码格式"
    #     t = s.toast(self.testdata['Toastxpath'],"text")
    #     assert t == text
    #
    # #手机号不存在
    # def test_wrong(self):
    #     s = LoginApp()
    #     s.startApp()
    #     s.et_phone_num()
    #     s.sendPhoneWA()
    #     s.sendPsw()
    #     s.btn_login()
    #     text = "请输入正确密码格式"
    #     t = s.toast(self.testdata['Toastxpath'],"text")
    #     assert t == text

