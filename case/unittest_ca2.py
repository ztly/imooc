import unittest
class SecondCase_unit(unittest.TestCase):  # 继承unittest类
	# 类前置条件
	@classmethod
	def setUpClass(cls):
		print('SecondCase_unit类所有case执行之前的前置')
	# 类后置条件
	@classmethod
	def tearDownClass(cls):
		print('SecondCase_unit类所有case执行之后的后置')

	def setUp(self):
		print('case的前置条件')

	def testFun01(self):  # 以test开头的方法才会别main运行
		print('这是第1条case')

	@ unittest.skip('不执行第2条')
	def testFun02(self):
		print('这是第2条case')

	def testFun03(self):
		print('这是第3条case')

	def tearDown(self):
		print('case的后置条件')
	

if __name__ == "__main__":
	# 运行所有test方法
	# unittest.main()
	
	# 运行指定test方法
	suite = unittest.TestSuite()
	suite.addTest(SecondCase_unit('testSecondFun'))
	suite.addTest(SecondCase_unit('testThirdFun'))
	suite.addTest(SecondCase_unit('testFirstFun'))
	unittest.TextTestRunner().run(suite)