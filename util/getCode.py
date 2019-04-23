from PIL import Image

from util.ShowapiRequest import ShowapiRequest
import time

class GetCode:
	def __init__(self, driver):
		self.driver = driver

	def getImg(self, file_name):
		element = self.driver.find_element_by_id('getcode_num')
		self.driver.save_screenshot(file_name)
		point = element.location  # 验证码图片左上角点的坐标
		left = point['x']
		top = point['y']
		size = element.size  # 验证码图片的大小
		right = left + size['width']
		bottom = top + size['height']
		img_orig = Image.open(file_name)
		# 在原截图上截取验证码图片
		img_final = img_orig.crop((left*2, top*2, right*2, bottom*2))
		img_final.save(file_name)
		time.sleep(3)

	# 解析验证码图片
	def parseImg(self, file_name):
		self.getImg(file_name)
		return 'dek23'
'''		r = ShowapiRequest("http://route.showapi.com/184-5","91267","1dbeca97548a4923adea21e917b3df8b" )
		r.addBodyPara("typeId", "35")
		r.addBodyPara("convert_to_jpg", "0")
		r.addBodyPara("needMorePrecise", "0")
		r.addFilePara("image", file_name) #文件上传时设置
		res = r.post()
		text = res.json()['showapi-res_body']['Result']
		return text'''




