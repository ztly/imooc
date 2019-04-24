from xlutils.copy import copy
import xlrd
import os


class ExcelUtil:
    def __init__(self, excl_path=None, index=None):
        if excl_path == None:
            self.excel_path = os.path.join(os.getcwd()+'/config/casedata.xlsx')
        else:
            self.excel_path = excl_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]
        # 行数
        self.rows = self.table.nrows
        # [[],[],[]]
    
    # 获取表格行数
    def get_lines(self):
        rows = self.table.nrows
        if rows>=1:
            return rows
        return None

    # 获取指定单元格数据
    def get_col_value(self, row, col):
        if self.get_lines()>row:
            data = self.table.cell(row, col).value
            return data
        return None
    
    # 获取表格数据
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None
    
    # 写入数据
    def write_value(self, row, col, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, col, value)
        write_data.save(self.excel_path)

if __name__ == "__main__":
    ex = ExcelUtil()
    print(ex.get_data())
    ex.write_value(0,8,"test")
