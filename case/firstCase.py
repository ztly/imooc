import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from business.registerBusiness import RegisterBusiness
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
from log.user_log import UserLog




'''
unittest前/后置方法、断言、报告生成、运行失败后截图
'''
class FirstCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.log = UserLog()
		cls.logger = cls.log.get_log()
	@classmethod
	def tearDownClass(cls):
		cls.log.close_handle()

	# 前置条件
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.fullscreen_window()
		self.driver.get('http://www.5itest.cn/register?goto=/')
		self.logger.info("tihs is my first log")
		self.login = RegisterBusiness(self.driver)
		self.file_name = os.path.join(os.getcwd()+'/img/'+'CropRegister.png')
	# 后置条件
	def tearDown(self):
		# 运行报错时保存截图
		for case_name, error in self._outcome.errors:
			if error:
				case_name = self._testMethodName
				self.driver.save_screenshot(os.path.join(os.getcwd()+"/report/"+case_name+".png"))
		print('---------执行后置方法：关闭浏览器----------')
		self.driver.close()


	def test_login_email_err(self):
		email_error = self.login.check_email('12', 'tingJio', '1111234', self.file_name)
		self.assertFalse(email_error, '邮箱验证成功')
		# if email_error == True:
		# 	print('邮箱验证case失败！')

	def test_login_username_err(self):
		name_error = self.login.check_name('1292871494@qq.com','-','1111234',self.file_name)
		self.assertFalse(name_error, '用户名验证成功')

	def test_password_err(self):
		password_error = self.login.check_password('1292871494@qq.com','-','3',self.file_name)
		self.assertFalse(password_error, '密码验证成功')

	def test_code_err(self):
		code_error = self.login.check_code('1292871494@qq.com','tingJio','1111234',self.file_name)
		self.assertFalse(code_error, '验证码验证成功')

	def test_login__sucess(self):
		self.login.base_login('1292341234@qq.com','tingJio','1111sd2',self.file_name)
		self.assertFalse(self.login.register_success(), '正常流程验证失败！')
		self.assertTrue(self.login.register_success(), '正常流程验证成功！')
	
	'''def main(self):
		case = FirstCase()
		case.test_login_email_err()
		case.test_login_username_err()
		case.test_password_err()
		case.test_code_err()
		case.test_login__sucess()'''


if __name__ == "__main__":
	# unittest.main()
	# 报告存放位置
	file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
	# 打开报告文件并写入内容
	f = open(file_path,'wb')
	suite = unittest.TestSuite()
	suite.addTest(FirstCase('test_login_email_err'))
	suite.addTest(FirstCase('test_password_err'))
	suite.addTest(FirstCase('test_login_username_err'))
	# suite.addTest(FirstCase('test_code_err'))
	# unittest.TextTestRunner().run(suite)
	runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report", description="第一个测试报告", verbosity=2)
	runner.run(suite) 