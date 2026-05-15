import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

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

#使用Appium Inspector工具，可以定位元素和录制脚本
#把脚本导出到python中就可以直接运行
time.sleep(3)
el1 = driver.find_element(by=AppiumBy.ID, value="com.dangdang.buy2:id/tab_search_iv")
el1.click()
time.sleep(3)
el2 = driver.find_element(by=AppiumBy.ID, value="com.dangdang.buy2:id/tab_category_iv")
el2.click()