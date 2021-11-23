#!/usr/bin/python3


from Common.ConBaseOperate.FindElement import FindElement
from ReadTestData.ReadTestdata import ReadTestdata

class LoginApp(FindElement):
    #读取测试数据
    testdata = ReadTestdata.readtestdata_01()['LoginApp']
    print(testdata)

    #点击app
    def startApp(self):
        return self.findByAccessibilityId(self.testdata['startApp']).click()

    #点击手机号输入栏
    def et_phone_num(self):
        self.waitAttriID(self.testdata['et_phone_num'])
        return self.findById(self.testdata['et_phone_num']).click()

    #输入手机号_正确
    def sendPhone(self):
        return self.sendkeysID(self.testdata['et_phone_num'],self.testdata['sendPhone'])

    #输入手机号_错误
    def sendPhoneW(self):
        return self.sendkeysID(self.testdata['et_phone_num'],self.testdata['sendPhoneW'])

    #输入手机号_不存在误
    def sendPhoneWA(self):
        return self.sendkeysID(self.testdata['et_phone_num'],self.testdata['sendPhoneWA'])

    #点击密码输入栏
    def et_password(self):
        return self.findById(self.testdata['et_password']).click()

    #输入密码_格式正确
    def sendPsw(self):
        return self.sendkeysID(self.testdata['et_password'],self.testdata['sendPsw'])

    #输入密码_格式不正确
    def sendPswW(self):
        return self.sendkeysID(self.testdata['et_password'],self.testdata['sendPswW'])

    #点击登录控件
    def btn_login(self):
        return self.findById(self.testdata['btn_login']).click()

    #退出-点击我的控件
    def ll_user(self):
        self.waitAttriID(self.testdata['ll_user'])
        return self.findById(self.testdata['ll_user']).click()

    #点击退出登录
    def btn_logout(self):
        self.waitAttriID(self.testdata['btn_logout'])
        return self.findById(self.testdata['btn_logout']).click()

    #确定退出
    def btn_confirm(self):
        self.waitAttriID(self.testdata['btn_confirm'])
        return self.findById(self.testdata['btn_confirm']).click()

    #取消退出
    def btn_cancel(self):
        self.waitAttriID(self.testdata['btn_cancel'])
        return self.findById(self.testdata['btn_cancel']).click()

    #清除文本_手机号
    def btn_clearphone(self):
        self.waitAttriXpath(self.testdata['btn_clearphone'])
        return self.findByXpath(self.testdata['btn_clearphone']).click()


    #清除文本_清除密码
    def btn_clearpws(self):
        self.waitAttriXpath(self.testdata['btn_clearpws'])
        return self.findByXpath(self.testdata['btn_clearpws']).click()

    #显示密码
    def iv_eye(self):
        return self.findById(self.testdata['iv_eye'])

    #获取toast
    def toast(self,xpath,attribute):
        self.waitAttriXpath(xpath)
        return self.getAttributeSingle(xpath,attribute)


# #调试前置代码
# FindElement.restartApp()
# s = LoginApp()
# s.startApp()