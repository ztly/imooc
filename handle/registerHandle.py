import sys
sys.path.append('/Users/edz/Documents/lab/imooc')
from page.registerPage import RegisterPage
from util.getCode import GetCode
import time
class RegisterHandle(object):

	def __init__(self, driver):
		self.driver = driver
		self.register_p = RegisterPage(driver)

	# 输入邮箱
	def send_user_email(self, email):
		self.register_p.get_email_element().send_keys(email)

	# 输入用户名
	def send_user_name(self, username):
		self.register_p.get_user_name().send_keys(username)

	# 输入密码
	def send_user_password(self, password):
		self.register_p.get_password().send_keys(password)

	# 输入验证码
	def send_code(self, file_name):
		get_code = GetCode(self.driver)
		get_code.getImg(file_name)  # 保存验证码图片
		code = get_code.parseImg(file_name) # 解析验证码
		time.sleep(2)
		self.register_p.get_code_element().send_keys(code)	

	# 获取提示信息
	def get_user_text(self, info, user_info=None):
		
			if info == 'email_error':
				element = self.register_p.get_email_error_element()
			elif info == 'name_error':
				element = self.register_p.get_name_error_element()
			elif info == 'password_error':
				element = self.register_p.get_password_error_element()
			elif info == 'code_error':
				element = self.register_p.get_code_error_element()
	 		# 输入后的错误提示与参数一致时，返回错误信息
			if element != None:
				err = element.text
				err_message = err if user_info == err else None
			else:
				err_message = None
			
			return err_message
		

	# 点击注册按钮
	def click_register_buttton(self):
		self.register_p.get_register_button().click()

	# 获取注册按钮文字
	def get_register_text(self):
		return self.register_p.get_register_button().text