#!/usr/bin/python3
"""
启动Aappium,安装app
"""
import os
from appium import webdriver
from Common.Conf import ReadConfig



class AndroidClient():
    # 读取文件
    cfg = ReadConfig.ReadConfig.readcfg()['AndroidClient']
    # print(cfg)

    #安装APP
    @classmethod
    def install(cls):
        path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        path2 = os.path.join(path1, "Attachments", "Apks", cls.cfg['apk'])
        #启动服务
        caps = {}
        caps["platformName"] = cls.cfg['platformName']
        caps["appium:deviceName"] = cls.cfg['deviceName']
        caps["appium:app"] = (path2)  # 后期修改动态获取路径
        caps["appium:autoLaunch"] = False
        caps["appium:automationName"] = "UiAutomator2"
        caps["autoGrantPermissions"] = True        #自动授权
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        return cls.driver

    #重启app
    @classmethod
    def restartapp(cls):
        #启动服务
        caps = {}
        caps["platformName"] = cls.cfg['platformName']
        caps["appium:deviceName"] = cls.cfg['deviceName']
        caps["appPackage"] = cls.cfg['appPackage']
        caps["appium:automationName"] = "UiAutomator2"
        caps["newCommandTimeout"] = cls.cfg['newCommandTimeout']    #超时设置，单位秒
        caps["appium:noReset"] = True       # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        return cls.driver

# a = AndroidClient()
# s= a.restartapp()
# a.driver.find_element_by_android_uiautomator('new UiSelector().text("前一日")').click()
#
