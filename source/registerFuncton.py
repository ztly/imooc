from selenium import webdriver
import time
import sys
sys.path.append('/Users/edz/Documents/lab/imooc')
import random
from PIL import Image
from base.findElement import FindElement 
import random


class RegisterFuncton(object):
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    # 打开浏览器
    def get_driver(self, url, i):
        if i == 0:
            driver = webdriver.Chrome()
        elif i == 1:
            driver = webdriver.Firefox()
        elif i == 2:
            driver = webdriver.Safari()
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
        img_final = img_orig.crop((left*2, top*2, right*2, bottom*2))
        img_final.save(filename)

    def main(self):
        nickname = self.getRandom()
        email = nickname + '@163.com'
        code = None #识别后的验证码值
        error_text = self.get_element('captcha_code-error')
        filename = '/Documents/lab/imooc/img/error_screenshot.png'
        self.get_element('register_email').send_keys(email)
        self.get_element('register_nickname').send_keys(nickname)
        self.get_element('register_password').send_keys('111111')
        self.get_element('captcha_code').send_keys(code)
        if error_text is None:
            print('注册成功')
        else:
            print('验证码输入有误')
            self.driver.save_screenshot(filename) # 验证失败后保存截图
        self.get_element('register-btn').click()
        time.sleep(5)
        self.driver.close()



if __name__ == "__main__":
    for i in range(3):
        regist_function = RegisterFuncton('http://www.5itest.cn/register?goto=/', i)
        regist_function.main()







