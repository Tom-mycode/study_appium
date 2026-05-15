import time

from comm.base import *

driver = Driver().open_app('com.microvirt.launcher2','com.microvirt.launcher.Launcher')

#--------------------------先解决广告问题--------------------------------#
time.sleep(3)
driver.find_element(AppiumBy.ID,'com.microvirt.market:id/btn_dismiss').click()


#----------------------------------------------------------#
#定位要操作的元素
el = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Appium Settings"]')

#导包
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

#创建手指对象，用于执行滑动操作
touch_input = PointerInput(interaction.POINTER_TOUCH, "finger")
#创建动作对象，用于定义操作的指令
actions = ActionBuilder(driver, mouse=touch_input)

actions.pointer_action.move_to(el) \
    .pointer_down() \
    .pause(1) \
    .move_by(x=0, y=200) \
    .pointer_up()
time.sleep(3)
actions.perform()


actions.pointer_action.move_to(el) \
    .pointer_down() \
    .pause(1) \
    .move_by(x=0, y=-300) \
    .pointer_up()
time.sleep(3)
actions.perform()