import unittest
import os

'''
所有case的运行总类
'''

class RunCase(unittest.TestCase):
	def test_case01(self):
		case_path = os.path.join(os.getcwd(), 'case') # 添加case路径,os.getcwd()获取当前路径
		suite = unittest.defaultTestLoader.discover(case_path, 'unittest_*.py')
		unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
	unittest.main()
