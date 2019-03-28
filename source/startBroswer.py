from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register?goto=/')
time.sleep(2)
EC.title_contains('注册')
driver.find_element_by_id('register_email')
# 生成随机邮箱
for i in range(5):
    emails = ''.join(random.sample("1234567890", 5))

# 驱动等待5秒 直到查找的元素在页面展示（5秒之内未显示则返回false）
localter = (By.CLASS_NAME, 'controls')
WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(localter))

# get_attribute方法的使用
email_element = driver.find_element_by_id('register_email')
print(email_element.get_attribute("placeholder"))
email_element.send_keys("1292871494@qq.com")
print(email_element.get_attribute("value"))
time.sleep(2)
driver.close()

'''
# 注册信息填写
driver.find_element_by_id('register_email').send_keys('1292871494@qq.com')
parent_element = driver.find_elements_by_class_name('controls')[1]
user_element = parent_element.find_element_by_class_name(
    'form-control').send_keys('TingJio')
driver.find_element_by_name('password').send_keys('zhouting414')
driver.find_element_by_xpath('//input[@placeholder="验证码"]')
'''
