from page.registerPage import RegisterPage
class RegisterHandle(object):
	def __init__(self,driver):
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
	def send_code(self, code):
		self.register_p.get_code().send_keys(code)
	# 获取提示信息
	def get_user_text(self, info, userinfo):
		if info == 'email_error':
			text = self.register_p.get_email_error_element().get_attribute('value')
		elif info == 'name_error':
			text = self.register_p.get_name_error_element().get_attribute('value')
		elif info == 'password_error':
			text = self.register_p.get_password_error_element().get_attribute('value')
		elif info == 'code_error':
			text = self.register_p.get_code_error_element().get_attribute('value')
		return text
	# 点击注册按钮
	def click_register_buttton(self):
		self.register_p.get_register_button().click()

	# 获取注册按钮文字
	def get_register_text(self):
		return self.register_p.get_register_button().text