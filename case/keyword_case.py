import sys
import os
sys.path.append(os.path.join(os.getcwd()))
from util.excel_util import ExcelUtil
from mykeyword.actionMethod import ActionMethod
class KeyWordCase:
    
    def run_main(self):
        self.action_method = ActionMethod()
        file_path = os.path.join(os.getcwd()+'/config/keyword.xlsx')
        handle_excl = ExcelUtil(excl_path = file_path)
        # 拿到行数
        case_lines = handle_excl.get_lines()
        if case_lines:
            # 循环行数，执行每一行的case
            for i in range(1, case_lines):
                # 是否执行
                is_run = handle_excl.get_col_value(i, 3)
                if is_run:
                    # 拿到执行方法
                    method = handle_excl.get_col_value(i, 4)
                    # 输入数据
                    send_value = handle_excl.get_col_value(i, 5)
                    # 操作元素
                    handle_value = handle_excl.get_col_value(i, 6) 
                    # 预期结果
                    except_method = handle_excl.get_col_value(i, 7)
                    # 预期结果值
                    except_result = handle_excl.get_col_value(i, 8)
                    self.run_method(method, send_value, handle_value)
                    if except_result != '':
                        except_value = self.get_except_value(except_result)
                        if except_value[0] == 'text':
                            print('text的except_method------>', except_method)
                            result = self.run_method(except_method)
                            print('action_method中运行的方法名：--------->', getattr(self.action_method, except_method))
                            print('text result------->', result)
                            if except_value[1] in result:
                                handle_excl.write_value(i, 9, 'pass')
                            else:
                                handle_excl.write_value(i, 9, 'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_method, except_value[1])
                            print('element result------->', result)

                            if result:
                                handle_excl.write_value(i, 9, 'pass')
                            else:
                                handle_excl.write_value(i, 9, 'fail')

 
    #获取预期结果值
    def get_except_value(self, data):
        return data.split('=')
    
    # 关联方法和输入值
    def run_method(self, method , send_value='', handle_value=''):
        method_value = getattr(self.action_method, method)
        # 打开浏览器
        if send_value == '' and handle_value != '':
           result = method_value(handle_value)
        # 输入操作
        elif send_value != '' and handle_value != '' :
            result = method_value(handle_value, send_value)
        # 
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        # 关闭浏览器时，方法没有参数
        else:
            result = method_value()
        return result

if __name__ == "__main__":
    test = KeyWordCase()
    test.run_main()