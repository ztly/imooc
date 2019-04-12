import sys
sys.path.append('/Users/edz/Documents/lab/imooc')
from business.registerBusiness import RegisterBusiness
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
import os
import ddt


@ddt.ddt
class FirstDdtCase(unittest.TestCase):
	# 用例的前置条件
	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('disable-infobars') # 取消 chrome正受到自动测试软件的控制的信息栏
		self.driver = webdriver.Chrome(chrome_options=options)
		self.driver.get('http://www.5itest.cn/register?goto=/')
		self.driver.fullscreen_window() # 全屏打开
		self.login = RegisterBusiness(self.driver)
	
	# 后置条件
	def tearDown(self):
		time.sleep(2)
		# 运行报错时保存截图
		for case_name, error in self._outcome.errors:
			if error:
				case_name = self._testMethodName
				self.driver.save_screenshot(os.path.join(os.getcwd()+"/report/"+case_name+".png"))
		print('---------执行后置方法：关闭浏览器----------')
		self.driver.close()
   
	# 邮箱、用户名、密码、验证码/错误信息定位/错误信息提示
	@ddt.data(
		['1', 'zhou', '111111', '/Users/edz/Documents/lab/imooc/img/CropRegister.png', 'email_error','请输入有效的电子邮件地址'],
		['1292871494@qq.com', 'zhou', '111111', '/Users/edz/Documents/lab/imooc/img/CropRegister.png', 'email_error','请输入有效的电子邮件地址']


		)
	
	@ddt.unpack
	def test_register_case(self, email, name, password, file_name, errElement, errText):
		email_error = self.login.register_function(email, name, password, file_name, errElement, errText)
		self.assertFalse(email_error, "测试失败")
		# if email_error == True:
		# 	print('邮箱验证case失败！')


if __name__ == "__main__":
	file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
	# 打开报告文件并写入内容
	f = open(file_path,'wb')
	# 加载测试类中所有标准的测试case
	suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
	runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report", description="第一个测试报告", verbosity=2)
	runner.run(suite)
