import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
	def setUp(self):
		print('前置函数')
	def tearDown(self):
		print('后置函数')
	# 邮箱、用户名、密码、验证码/错误信息定位/错误信息提示
	@ddt.data(
		[1,2],
		[3,4],
		[5,6],
		[7,8]
	)
	@ddt.unpack
	def test_add(self, a, b):
		print(a+b)
if __name__ == "__main__":
	unittest.main()
