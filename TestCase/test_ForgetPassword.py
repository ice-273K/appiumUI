#!/usr/bin/python3

from Pages.ForgetPassword import ForgetPassword
from Common.ConBaseOperate.FindElement import FindElement

class Test_ForgetPassword():
    def setup_method(self):
        FindElement.restartApp()

    def teardown_method(self):
        FindElement.quite()

    #点击app-》点击忘记密码-》输入手机号-》点击获取验证码-》图形验证码+输入验证码-》-》输入新密码-》确认新密码-》点击i确定
    def test_forgetpassword(self):
        s = ForgetPassword()
        s.startApp()
        s.tv_forget_password()
        s.send_et_phone_num()
        s.btn_getcode()
        s.sendCodeh()
        s.clear_code()
        s.sendCode()
        s.et_new_password()
        s.new_password_eye()
        s.et_ensure_password()
        s.ensure_password_eye()
        s.btn_ensure()