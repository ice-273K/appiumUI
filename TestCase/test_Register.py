#!/usr/bin/python3
from time import sleep

from Pages.Register import Register
from Common.ConBaseOperate.FindElement import FindElement
import pytest

class Test_Register():

    def setup_method(self):
        FindElement().restartApp()

    def teardown_method(self):
        FindElement().quite()


    #点击app-》选立即注册-》输入手机号-》清除手机号-》输入手机号-》点击获取验证码-》关闭验证码-》点击获取验证码-》刷新验证码-》图形验证码-》输入验证码-》填写真实姓名-》填写密码-》明文密码-》点击注册
    def test_register(self):
        s = Register()
        s.startApp()
        s.tv_register()
        s.et_phone_num()
        s.clear_phone()
        s.et_phone_num()
        s.btn_getcode()
        s.iv_close()
        s.btn_getcode()
        s.iv_refresh()
        s.graph_getCode()
        s.edit_code()
        s.et_real_name()
        s.et_password()
        s.iv_eye()
        s.btn_register()
