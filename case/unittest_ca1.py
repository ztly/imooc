import unittest
class FirstCase_unit(unittest.TestCase):  # 继承unittest类
	# 类前置条件
	@classmethod
	def setUpClass(cls):
		print('FirstCase_unit类所有case执行之前的前置')
	# 类后置条件
	@classmethod
	def tearDownClass(cls):
		print('FirstCase_unit类所有case执行之后的后置')

	def setUp(self):
		print('case的前置条件')

	def testFunFirst(self):  # 以test开头的方法才会main运行
		print('这是第一条case')

	def testFunSecond(self):
		print('这是第二条case')

	def testFunThird(self):
		print('这是第三条case')

	def tearDown(self):
		print('case的后置条件')
	

if __name__ == "__main__":
	# 运行所有test方法
	# unittest.main()
	
	# 运行指定test方法
	suite = unittest.TestSuite()
	suite.addTest(FirstCase_unit('testSecondFun'))
	suite.addTest(FirstCase_unit('testThirdFun'))
	suite.addTest(FirstCase_unit('testFirstFun'))
	unittest.TextTestRunner().run(suite)