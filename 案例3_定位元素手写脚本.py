import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from attr.converters import default_if_none

#定义一个变量，用于存储连接信息
desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "7",
    "appium:deviceName": "127.0.0.1:21503",
    "appium:appPackage": "com.dangdang.buy2",
    "appium:appActivity": ".activity.ActivityMainTab",
    "appium:noReset": True,
    "appium:fullReset": False,
    "automationName": "UiAutomator2"
}
#把配置项装进option配置中
options = UiAutomator2Options().load_capabilities(desired_caps)
#定义AppiumServer的地址
appium_server = "http://127.0.0.1:4723/wd/hub"
#创建对象，用于控制APP
driver = webdriver.Remote(command_executor=appium_server,
                          options=options)
#设置隐式等待
driver.implicitly_wait(20)

driver.find_element(AppiumBy.ID,'com.dangdang.buy2:id/research_flipper_textview').click()
driver.find_element(AppiumBy.ID,'com.dangdang.buy2:id/et_search').send_keys("三国演义")
driver.find_element(AppiumBy.ID,'com.dangdang.buy2:id/tv_search').click()
