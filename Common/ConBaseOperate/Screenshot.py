import time

from PIL import ImageGrab, Image
from pytesseract import pytesseract
import os


class Screenshot():

    #简单截图方法（未选定窗口进行截图）
    def get_screenshot(self,image):
        path1 = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        path = os.path.join(path1,'Attachments','Image',image)
        ImageGrab.grab().save(path)  # 截图
        a = pytesseract.image_to_string(Image.open(path),lang="chi_sim") #识别图上文字
        b = a.replace(' ','').replace('\n','')  #处理掉空格和换行
        return b

# Screenshot().get_screenshot(image='2.png')
# str1 = '1 2 3 '
# print(type(str1))
# print(str1.replace(' ',''))