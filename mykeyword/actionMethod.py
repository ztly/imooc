from selenium import webdriver
import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from base.findElement import FindElement
import time
class ActionMethod:

    # 打开浏览器
    def openBroswer(self,broswer):
        if broswer == 'chrome':
            self.driver = webdriver.Chrome()
        elif broswer == 'firefox':
            self.driver = webdriver.Firefox()
    # 输入地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element
        
    # 输入元素
    def element_send_keys(self, key, value):
        element = self.get_element(key)
        element.send_keys(value)
    
    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()
    
    # 等待
    def sleep_time(self):
        time.sleep(10)
        
    # 关闭浏览器
    def close_driver(self):
        self.driver.close()

    # 获取title
    def get_title(self):
        title = self.driver.title
        print('title--------->', title)
        return title
