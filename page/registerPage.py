from base.findElement import FindElement
class RegisterPage:

	def __init__(self, driver):
		self.fd = FindElement(driver)

	def get_email_element(self):
		return self.fd.get_element('email')

	def get_user_name(self):
		return self.fd.get_element('name')

	def get_password(self):
		return self.fd.get_element('password')

	def get_code(self):
		return self.fd.get_element('captcha')

	def get_email_error_element(self):
		return self.fd.get_element('email_error')

	def get_name_error_element(self):
		return self.fd.get_element('name_error')

	def get_password_error_element(self):
		return self.fd.get_element('password_error')

	def get_code_error_element(self):
		return self.fd.get_element('code-text-error')

	def get_register_button(self):
		return self.fd.get_element('register')

	
