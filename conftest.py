import pytest
from page.seafile import *

@pytest.fixture(scope='class')
def f1():
    print('前置脚本')
    yield
    print('后置脚本')


@pytest.fixture(scope='class')
def init():
    driver = Seafile()
    dr = driver.open_app()
    driver.login(dr)
    yield driver,dr
    dr.quit()

# @pytest.fixture(scope='function')
@pytest.fixture(scope='class')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='package')
# @pytest.fixture(scope='session')
def xxx():
    print('我是前置脚本')
    yield '我是返回值'
    print('我是后置脚本')