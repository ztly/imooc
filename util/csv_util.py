import csv

file_path = '/Users/edz/Documents/lab/imooc/config/csvData.csv'
with open(file_path) as f:
	reader = csv.reader(f)
	for row in reader:
		# 行号从1开始
		print(reader.line_num, row)

