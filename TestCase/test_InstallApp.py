#!/usr/bin/python3
"""
用例设计：StarAapp页面
"""
from time import sleep
from Common.ConBaseOperate.FindElement import FindElement
from Pages.InstallApp import InstallApp
import pytest

class Test_InstallApp():

    # 后置条件：退出app，清除
    def teardown_method(self):
        # print("结束")
        FindElement.quite()

    #安装app
    def test_case01(self):
        InstallApp().installApp()


