from selenium import webdriver
import time
from PIL import Image
import pytesseract
from ShowapiRequest import ShowapiRequest
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys

'''options = webdriver.ChromeOptions()
# options.add_argument('--kiosk') # Mac全屏窗口
# options.add_argument('--start-maximized') # Windows全屏窗口
options.add_argument('disable-infobars') # 取消 chrome正受到自动测试软件的控制的信息栏
driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register?goto=/')
driver.fullscreen_window()
time.sleep(5)
# 截取原图
element = driver.find_element_by_id('getcode_num')
driver.save_screenshot(
    '/Users/edz/Documents/lab/imooc/img/Register.png')
point = element.location  # 验证码图片左上角点的坐标
left = point['x']
top = point['y']
print('验证码图片左上角点的坐标：',point)
size = element.size  # 验证码图片的大小
right = left + size['width'] 
bottom = top + size['height']
print('验证码图片的大小', size)
# 打开原图
img_orig = Image.open(
    '/Users/edz/Documents/lab/imooc/img/Register.png')
# 在原截图上截取验证码图片
img_final = img_orig.crop((left*2, top*2, right*2, bottom*2))
# img_final = img_orig.crop((680, 563, 809, 563))
img_final.save('/Users/edz/Documents/lab/imooc/img/CropRegister.png')
# 图片转换文字
#pytesseract.image_to_string(
#    '/Documents/lab/imooc/img/CropRegister.png')
time.sleep(5)
'''
r = ShowapiRequest("http://route.showapi.com/184-5","91267","1dbeca97548a4923adea21e917b3df8b" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"/Users/edz/Documents/lab/imooc/img/CropRegister.png") #文件上传时设置
res = r.post()
print(res.text) # 返回信息


# driver.close()

