import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from util.excel_util import ExcelUtil
from keyword.actionMethod import ActionMethod
class KeyWordCase:
    def run_main(self):
        file_path = os.path.join(os.getcwd()+'/config/keyword.xlsx')
        handle_excl = ExcelUtil(excl_path = file_path)
        case_lines = handle_excl.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excl.get_col_value(i, 3)
                if is_run:
                   method = handle_excl.get_col_value(i, 4)
                   send_value = handle_excl.get_col_value(i, 5)
                   handle_value = handle_excl.get_col_value(i, 6) 
                   self.run_method(method, send_value, handle_value)
                       
    def run_method(self, method , send_value, handle_value):
        action_method = ActionMethod()
        method_value = getattr(action_method, method)
        if send_value:
            method_value(send_value, handle_value)
        else:
            method_value(handle_value)


        # 拿到行数
        # 循环行数，执行每一行的case
        # if是否执行
            # 拿到执行方法
            # 拿到操作元素
            # 拿到输入数据
            # if 是否有输入数据
                # 执行方法（输入数据，操作元素）
            # if 没有输入数据
                # 执行方法（操作元素）