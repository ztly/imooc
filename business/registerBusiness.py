import sys
sys.path.append('/Users/edz/Documents/lab/imooc')
from handle.registerHandle import RegisterHandle
class RegisterBusiness:
	def __init__(self, driver):
		self.register_h = RegisterHandle(driver)
	def base_login(self, email, name, password, captcha):
		self.register_h.send_user_email(email)
		self.register_h.send_user_name(name)
		self.register_h.send_user_password(password)
		self.register_h.send_code(captcha)
		self.register_h.click_register_buttton()
	
	def register_success(self):
		if self.register_h.get_register_text() == None:
			return True
		else:
			return False


	def check_email(self, email, name, password, captcha):
		self.base_login(email, name, password, captcha)
		if self.register_h.get_user_text( 'email_error', '请输入有效的电子邮箱地址！') == None:
			print('邮箱验证不成功！')
			return True
		else:
			return False

	def check_name(self, email, name, password, captcha):
		self.base_login(email, name, password, captcha)
		if self.register_h.get_user_text('name_error', '字符长度必须大于等于4，一个中文字算2个字符') == None:
			print('用户名验证不成功！')
			return True
		else:
			return False

	def check_password(self, email, name, password, captcha):
		self.base_login(email, name, password, captcha)
		if self.register_h.get_user_text('password_error', '最少需要输入 5 个字符') == None:
			print('密码验证不成功！')
			return True
		else:
			return False

	def check_code(self, email, name, password, captcha):
		self.base_login(email, name, password, captcha)
		if self.register_h.get_user_text('code_error', '验证码错误') == None:
			print('验证码验证不成功！')
			return True
		else:
			return False