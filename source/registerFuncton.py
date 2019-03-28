from selenium import webdriver
import time
import random
from PIL import Image
import registerCode
from findElement import FindElement 
import random


class RegisterFuncton(object):
    def __init__(self, url):
        self.driver = self.get_driver(url)

    # 打开浏览器
    def get_driver(self, url):
       driver = webdriver.Chrome()
       driver.get(url)
       driver.maximize_window()
       return driver

    def get_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element
    # 输入值
    def input_value(self, key, value):
        self.get_element(key).send_keys(value)
    # 生成随机数
    def getRandom(self):
        rand = ''.join(random.sample("1234567890QWERTYUIOP", 8))
        return rand

    # 获取验证码图片
    def getImg(self, filename):
        element = self.get_element('getcode_num')
        self.driver.save_screenshot(filename)
        point = element.location  # 验证码图片左上角点的坐标
        left = point['x']
        top = point['y']
        print(point)
        size = element.size  # 验证码图片的大小
        right = left + size['width']
        bottom = top + size['height']
        print(size)
        img_orig = Image.open(filename)
        # 在原截图上截取验证码图片
        img_final = img_orig.crop((left, top, right, bottom))
        img_final.save(filename)



