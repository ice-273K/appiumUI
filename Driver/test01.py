#!/usr/bin/python3
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "MI 9 transport_id:1"
caps["appPackage"] = "com.tcsl.operateplatform"
caps["appium:automationName"] = "UiAutomator2"
caps["newCommandTimeout"] =  120  #超时设置，单位秒
caps["appium:noReset"] = True       # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# v1 = driver.find_element_by_id("com.tencent.mm:id/erh")
# x1 = driver.get_window_size()['width']
# y1 = driver.get_window_size()['height']
# print(x1)
# print(y1)
# #
# size = (driver.get_window_size()['width'],driver.get_window_size()['height'])
# print(size)
# #
# x1 = size[0]*0.16
# x2 = size[0]*0.71
# y1 = size[1]*0.59
# y2 = size[1]*0.59
# #
# # for i in range(10):
# #     size0 = driver.swipe(x1,y1,x2,y2,duration = 500)
# #     sleep(5)
# #     print(size0)
# # driver.swipe(x1,y1,x2,y2,duration = 500)
# text = "验证失败!"
# # text =driver.find_element_by_id('com.tcsl.operateplatform:id/tv_error').get_attribute("text")
# # text = "验证码已发送"
# while text =="验证失败!":
#     try:
#         driver.swipe(x1, y1, x2, y2, duration=500)
#         sleep(1)
#         text = driver.find_element_by_id('com.tcsl.operateplatform:id/tv_error').get_attribute("text")
#     except:
#         break



# text = driver.find_element_by_id('com.tcsl.operateplatform:id/tv_error').get_attribute("text")
# print(text)

#
# TouchAction(driver).press(x=148, y=947).move_to(x=509, y=947).release().perform()
# TouchAction(driver).press(x=142, y=950).move_to(x=661, y=950).release().perform()
# TouchAction(driver).press(x=137, y=945).move_to(x=520, y=952).release().perform()
# TouchAction(driver).press(x=144, y=949).move_to(x=621, y=945).release().perform()
# TouchAction(driver).press(x=142, y=950).move_to(x=540, y=950).release().perform()
# TouchAction(driver).press(x=144, y=949).move_to(x=680, y=950).release().perform()
# TouchAction(driver).press(x=144, y=950).move_to(x=477, y=950).release().perform()
# TouchAction(driver).press(x=144, y=950).move_to(x=657, y=950).release().perform()
# TouchAction(driver).press(x=144, y=950).move_to(x=653, y=950).release().perform()
# TouchAction(driver).press(x=144, y=950).move_to(x=664, y=949).release().perform()
# TouchAction(driver).press(x=146, y=950).move_to(x=632, y=950).release().perform()
# TouchAction(driver).press(x=142, y=950).move_to(x=601, y=950).release().perform()
# TouchAction(driver).press(x=144, y=950).move_to(x=427, y=950).release().perform()
# TouchAction(driver).press(x=146, y=949).move_to(x=589, y=949).release().perform()
# TouchAction(driver).press(x=144, y=952).move_to(x=562, y=950).release().perform()
# TouchAction(driver).press(x=142, y=950)   .move_to(x=335, y=949)   .release()   .perform()
# TouchAction(driver).press(x=142, y=950)   .move_to(x=551, y=950)   .release()   .perform()
# TouchAction(driver).press(x=144, y=950)   .move_to(x=463, y=950)   .release()   .perform()
# TouchAction(driver).press(x=144, y=949)   .move_to(x=484, y=950)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=949)   .move_to(x=562, y=950)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=949)   .move_to(x=533, y=950)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=949)   .move_to(x=671, y=949)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=950)   .move_to(x=650, y=950)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=950)   .move_to(x=493, y=949)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=949)   .move_to(x=637, y=950)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=952)   .move_to(x=425, y=947)   .release()   .perform()
# TouchAction(driver)   .press(x=142, y=950)   .move_to(x=603, y=950)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=950)   .move_to(x=515, y=950)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=950)   .move_to(x=445, y=950)   .release()   .perform()
# TouchAction(driver)   .press(x=144, y=949)   .move_to(x=686, y=949)   .release()   .perform()


# driver.quit()