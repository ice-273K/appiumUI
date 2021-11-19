#!/usr/bin/python3
"""
页面元素管理：app启动页
"""

from Common.ConBaseOperate.FindElement import FindElement

class InstallApp(FindElement):

    #首次安装apk
    def installApp(self):
        FindElement.installApp()

# a = InstallApp()
# a.installApp()



