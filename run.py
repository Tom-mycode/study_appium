# import pytest
# if __name__ == '__main__':
#     # pytest.main(['-sv','案例6_pytest.py','--clean-alluredir','--alluredir','./allure_result'])
#     pytest.main(['-sv','test_cases/test_001_zlk.py','--clean-alluredir','--alluredir','./allure_result'])
#
# import os
# os.system('allure generate ./allure_result -o ./report --clean')


import pytest

# # 只跑文件
# pytest.main(['案例7_pytest.py'])
#
# # 跑文件 + 显示print
# pytest.main(['-s', '案例7_pytest.py'])
#
# # 跑文件 + 详细日志
# pytest.main(['-v', '案例7_pytest.py'])
#
# # 跑文件 + 详细+print + 只跑uat标记用例
# pytest.main(['-sv', '-m uat', '案例7_pytest.py'])
#
# # 跑文件 + 详细+print + 只跑名字带002的用例
# pytest.main(['-sv', '-k 002', '案例7_pytest.py'])

pytest.main([
    '案例7_pytest.py',
    '--clean-alluredir',  # 清空上一次allure报告内容
    '--alluredir', './allure_result'  # 指定allure目录
])

import os
os.system('allure generate ./allure_result -o ./report --clean')
