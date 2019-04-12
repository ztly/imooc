import xlrd

class ExcelUtil:
	def __init__(self, excl_path=None, index=None):
		if excl_path == None:
			excel_path = "/Users/edz/Documents/lab/imooc/config/casedata.xls"
		if index == None:
			index = 0
		self.data = xlrd.open_workbook(excel_path)
		self.table = self.data.sheets()[index]
		# 行数
		self.rows = self.table.nrows
		#[[],[],[]]

	def get_data(self):
		result = []
		for i in range(self.rows):
			col = 	self.table.row_values(i)
			result.append(col)
		return result

if __name__ == "__main__":
	ex = ExcelUtil()
	print(ex.get_data())
