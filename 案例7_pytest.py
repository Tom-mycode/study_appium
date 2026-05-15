import time

import allure
import pytest


@allure.description('现在是SIT测试阶段')
class Test_sit:
    @pytest.mark.sit
    @pytest.mark.uat
    def test_001(self, xxx):
        print('我是SIT用例1')

    def test_002(self, xxx):
        print('我是SIT用例2')


@allure.description('现在是UAT测试阶段')
class Test_uat:
    def test_001(self, xxx):
        print('我是UAT用例1')

    def test_002(self, xxx):
        print('我是UAT用例2')


from comm.tools import *

lst = Tools().csv_to_dict_list('data/test_param.csv')


class Test_param:
    @pytest.mark.parametrize('data', lst)
    def test_003(self, data):
        print(f'我是测试用例param，我接收了传进来的参数{data}')
        with allure.step('1.打开app'):
            pass
        with allure.step('2.登陆'):
            pass
        with allure.step('3.添加资料库'):
            pass


from page.seafile import *

zlk_name = '新增资料库测试' + str(time.time())
from page.seafile import *


class Test_seafile:
    def test_004(self):
        dr = Seafile().open_app()  # 打开APP
        Seafile().login(dr)  # 登录
        actual1 = dr.current_activity  # 获取当前的Activity
        expect1 = '.ui.activity.BrowserActivity'  # 设置预期结果
        # Seafile().zlk_add(dr,zlk_name)  #新增资料库
        time.sleep(5)
        try:
            dr.find_element(AppiumBy.XPATH, f'//*[@text="{zlk_name}"]')
            actual2 = True
        except:
            actual2 = False
        expect2 = True
        assert actual2 == expect2
