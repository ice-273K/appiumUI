#!/usr/bin/python3
from Common.ConBaseOperate.FindElement import FindElement
from ReadTestData.ReadTestdata import ReadTestdata


class LoginByWechat(FindElement):

    testdata = ReadTestdata.readtestdata_01()['LoginByWechat']

    #点击app
    def startApp(self):
        return self.findByAccessibilityId(self.testdata['startApp']).click()

    #选中微信
    def iv_wechat(self):
        self.waitAttriID(self.testdata['iv_wechat'])
        return self.findById(self.testdata['iv_wechat']).click()

    #账号编写框点击
    def et_account(self):
        self.waitAttriXpath(self.testdata['et_account'])
        return self.findByXpath(self.testdata['et_account'])

    #写入账号
    def sendaccount(self):
        return self.sendkeysXpath(self.testdata['et_account'],self.testdata['sendaccount'])

    #密码编写框
    def et_password(self):
        return self.findByXpath(self.testdata['et_password'])

    #输入密码
    def sendpsw(self):
        return self.sendkeysXpath(self.testdata['et_password'],self.testdata['sendpsw'])

    #删除账号
    def clear_account(self):
        pass

    #删除密码
    def clear_password(self):
        pass

    #点击登录
    def erp(self):
        return self.findById(self.testdata['erp']).click()

    #用户名密码错误后点确定
    def ffp(self):
        self.waitAttriID(self.testdata['ffp'])
        return self.findById(self.testdata['ffp']).click()

    # 获取文案：用户名密码错误
    def msg_wrong(self):
        self.waitAttriID(self.testdata['ffp'])
        return self.getAttributeSingle(self.testdata['msg_wrong'],"text")

# a = LoginByWechat()
# a.iv_wechat()