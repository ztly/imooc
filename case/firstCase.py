import sys
sys.path.append('/Users/edz/Documents/lab/imooc')
from business.registerBusiness import RegisterBusiness
from selenium import webdriver
class FirstCase:
	def __init__(self):
		driver = webdriver.Chrome()
		driver.get('http://www.5itest.cn/register?goto=/')
		self.login = RegisterBusiness(driver)
	def test_login_email_err(self):
		email_error = self.login.check_email('12','1','1111','qwe23')
		if email_error == True:
			print('注册成功，此条case失败！')

	def test_login_username_err(self):
		name_error = self.login.check_name('12','1','1111','qwe23')
		if name_error == True:
			print('注册成功，此条case失败！')

	def test_password_err(self):
		password_error = self.login.check_password('12','1','1111','qwe23')
		if password_error == True:
			print('注册成功，此条case失败！')

	def test_code_err(self):
		code_error = self.login.check_code('12','1','1111','qwe23')
		if code_error == True:
			print('注册成功，此条case失败！')

	def test_login__sucess(self):
		self.login.base_login('12','1','1111','qwe23')
		if self.login.register_success() == True:
			print('注册成功！')
		else:
			print('注册失败！')
	
	def main(self):
		case = FirstCase()
		case.test_login_email_err()
		case.test_login_username_err()
		case.test_password_err()
		case.test_code_err()
		case.test_login__sucess()


if __name__ == "__main__":
	case = FirstCase()
	case.test_login_email_err()
	case.test_login_username_err()
	case.test_password_err()
	case.test_code_err()
	case.test_login__sucess()
