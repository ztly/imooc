import sys
sys.path.append('/Users/edz/Documents/lab/imooc')
from util.readLocalElement import ReadConfig

class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        filename = '/Users/edz/Documents/lab/imooc/config/LocalElement.ini'
        config = ReadConfig(filename)
        datas = config.get_data(key)
        by, value = datas.split('>')
        try:
            if by == 'id':
                element = self.driver.find_element_by_id(value)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif by == 'css':
                element = self.driver.find_element_by_css_selector(value)
            elif by == 'xpath':
                element = self.driver.find_element_by_xpath(value)
        except:
            element = None
        return element
