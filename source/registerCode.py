import time
import random
from PIL import Image
from selenium import webdriver
import os
import sys
sys.path.append('/Users/edz/Documents/lab/imooc')
from util.ShowapiRequest import ShowapiRequest



driver = webdriver.Chrome()


def initDriver():
    driver.get('http://www.5itest.cn/register?goto=/')
    driver.fullscreen_window()
    time.sleep(2)


def getElement(info):
    element = driver.find_element_by_id(info)
    return element


def getRandom():
    rand = ''.join(random.sample("1234567890QWERTYUIOP", 8))
    return rand

# 截取并保存验证码图片
def getImg(file_name):
    element = getElement('getcode_num')
    driver.save_screenshot(file_name)
    point = element.location  # 验证码图片左上角点的坐标
    left = point['x']
    top = point['y']
    print(point)
    size = element.size  # 验证码图片的大小
    right = left + size['width']
    bottom = top + size['height']
    print(size)
    img_orig = Image.open(file_name)
    # 在原截图上截取验证码图片
    img_final = img_orig.crop((left*2, top*2, right*2, bottom*2))
    img_final.save(file_name)

# 解析验证码图片
def parseImg(self, file_name):
    self.getImg(file_name)
    r = ShowapiRequest("http://route.showapi.com/184-5","91267","1dbeca97548a4923adea21e917b3df8b" )
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    r.addFilePara("image", file_name) #文件上传时设置
    res = r.post()
    return res.json()['showapi-res_body']['Result']


def run_main():
    initDriver()
    user_name = getRandom()
    img = os.path.join(os.getcwd()+'img/CropRegister.png')
    user_email = user_name + '@163.com'
    getElement('register_email').send_keys(user_email)
    getElement('register_nickname').send_keys(user_name)
    getElement('register_password').send_keys('111111')
    getImg(img)
    text = parseImg(img)
    getElement('captcha_code').send_keys(text)
    getElement('register-btn').click()
    driver.close()

run_main()
