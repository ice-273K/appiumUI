#!/usr/bin/python3
"""
查找元素的方法，及其他方法
"""
import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Driver.AndroidClient import AndroidClient
from selenium.webdriver.support import expected_conditions as ec

class FindElement():

    driver:WebDriver

    #重启app
    @classmethod
    def restartApp(cls):
        cls.driver = AndroidClient.restartapp()
        return cls.driver

    # 安装app并启动appium服务
    @classmethod
    def installApp(cls):
        cls.driver = AndroidClient.install()
        return cls.driver

    #退出
    @classmethod
    def quite(cls):
        return cls.driver.quit()

    # 根据Xpath查找
    def findByXpath(self,xpath):
        """
        :param xpath入参个数:
         1）'//android.widget.TextView[@content-desc="QQ"and @index="7"]'
         2）//android.widget.TextView[@content-desc="QQ"]
        """
        return self.driver.find_element_by_xpath(xpath)

    def findByXpaths(self,xpaths):
        return self.driver.find_elements_by_xpath(xpaths)

    # 根据accessibility_id查找
    def findByAccessibilityId(self, accessid):
        # return self.driver.find_element_by_accessibility_id(accessid)
        return self.driver.find_element_by_accessibility_id(accessid)

    # 根据id查找
    def findById(self,id):
        return self.driver.find_element_by_id(id)

    # 根据LINK_TEXT查找
    def findByLinkText(self,linktext):
        return self.driver.find_element_by_link_text(linktext)

    # 根据CLASS_NAME查找
    def findByClassName(self,classname):
        return self.driver.find_element_by_class_name(classname)

    #根据TAG_NAME查找
    def findByTagName(self,tagname):
        return self.driver.find_element_by_tag_name(tagname)

    #根据PARTIAL_LINK_TEXT查找
    def findByPartial(self,partialname):
        return self.driver.find_element_by_partial_link_text(partialname)

    #根据CSS_SELECTOR查找
    def findByCss(self,cssselect):
        return self.driver.find_elements_by_css_selector(cssselect)


    #输入文字:xpaht
    def sendkeysXpath(self,xpath,val1):
        self.xpath = xpath
        self.val1 = val1
        return self.driver.find_element(By.XPATH,self.xpath).send_keys(self.val1)

    # 输入文字:ID
    def sendkeysID(self,ID,val):
        return self.driver.find_element(By.ID,ID).send_keys(val)

    #返回节点里的属性值_多层级
    def getAttribute(self,xpaths,i,attribute):
        """
        :param xpaths: xpath的路径
        :param i: 列表的位置数，即第几个节点
        :param attribute: 要获取的属性值，如content-desc，resource-id等
        :return: 返回当前节点的某个属性的值
        入参形式举例：getAttribute("//android.widget.TextView[@content-desc='暂不使用按钮']",0,"content-desc")
        """
        return self.driver.find_elements_by_xpath(xpaths)[i].get_attribute(attribute)

    #返回节点里的属性值_单层级
    def getAttributeSingle(self,xpath,attribute):
        """
        :param xpaths: xpath的路径
        :param i: 列表的位置数，即第几个节点
        :param attribute: 要获取的属性值，如content-desc，resource-id等
        :return: 返回当前节点的某个属性的值
        入参形式举例：getAttribute("//android.widget.TextView[@content-desc='暂不使用按钮']",0,"content-desc")
        """
        return self.driver.find_element_by_xpath(xpath).get_attribute(attribute)

    ##等待元素出现:ID
    def waitAttriID(self,ID):
        try:
            WebDriverWait(self.driver, poll_frequency=2, timeout=60).until(ec.presence_of_element_located((By.ID, ID)))
            print("已出现")
        except:
            print("超时未出现")

    ##等待元素出现:xpath
    def waitAttriXpath(self,xpath):
        try:
            WebDriverWait(self.driver, poll_frequency=2, timeout=60).until(ec.presence_of_element_located((By.XPATH, xpath)))
        except:
            print("超时未出现")


    #####图形验证码_获得屏幕大小
    def graph_getSize(self):
        self.size = (self.driver.get_window_size()['width'], self.driver.get_window_size()['height'])
        return self.size

    #图形验证码_按屏幕比例进行拖拽
    def graph_getCode(self):
        x1 = self.graph_getSize()[0] * 0.16
        x2 = self.graph_getSize()[0] * 0.71
        y1 = self.graph_getSize()[1] * 0.59
        y2 = self.graph_getSize()[1] * 0.59
        text = "验证失败!"
        while text =="验证失败!":
            try:
                self.driver.swipe(x1, y1, x2, y2, duration=500)
                time.sleep(1)
                text = self.driver.find_element_by_id('com.tcsl.operateplatform:id/tv_error').get_attribute("text")
            except:
                break

# s = FindElement()
# s.restartApp()
# s.getCode()





