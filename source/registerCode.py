import time
import random
from PIL import Image
from selenium import webdriver
import pytesseract


driver = webdriver.Chrome()


def initDriver():
    driver.get('http://www.5itest.cn/register?goto=/')
    driver.maximize_window()
    time.sleep(2)


def getElement(info):
    element = driver.find_element_by_id(info)
    return element


def getRandom():
    rand = ''.join(random.sample("1234567890QWERTYUIOP", 8))
    return rand


def getImg(filename):
    element = getElement('getcode_num')
    driver.save_screenshot(filename)
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


def parseImg(filename):
    text = pytesseract.image_to_string(
        '/Users/edz/Documents/VS_Code/SeleniumPython/CropRegister.png')
    return text


def run_main():
    initDriver()
    user_name = getRandom()
    filename = ''
    user_email = user_name + '@163.com'
    getElement('register_email').send_keys(user_email)
    getElement('register_nickname').send_keys(user_name)
    getElement('register_password').send_keys('111111')
    getImg(filename)
    text = parseImg('')
    getElement('captcha_code').send_keys(text)
    getElement('register-btn').click()
    driver.close()

run_main()
