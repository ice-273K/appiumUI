#!/usr/bin/python3

from Common.ConBaseOperate.FindElement import FindElement
from ReadTestData.ReadTestdata import ReadTestdata

class Register(FindElement):

    testdata = ReadTestdata.readtestdata_01()['Register']

    # 点击app
    def startApp(self):
        return self.findByAccessibilityId(self.testdata['startApp']).click()