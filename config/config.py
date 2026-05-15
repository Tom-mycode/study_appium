# config/config.py
"""
项目配置管理：设备、App、Appium Server、超时、日志等
"""
import os

# ================== 项目根目录（自动获取，不用改） ==================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ================== 日志配置（全部在这里改！） ==================
# 日志存放目录：可以自由改路径
LOG_DIR = os.path.join(BASE_DIR, "logs")  # 项目根目录/logs

# 日志文件名
LOG_FILE_NAME = "automation.log"

# 日志级别
LOG_LEVEL = "INFO"



# ================== Appium Server 地址 ==================
APPIUM_HOST = "http://127.0.0.1:4723/wd/hub"

# ================== 安卓设备配置 ==================
DEVICE_CONFIG = {
    "platformName": "Android",
    "platformVersion": "7",
    "udid": "127.0.0.1:21503",
    "noReset": False,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "automationName": "UiAutomator2",
    "adbExecTimeout": 60000,  # 解决超时
}

# ================== 被测 APP 配置 ==================
APP_CONFIG = {
    "appPackage": "com.seafile.seadroid2",
    "appActivity": "com.seafile.seadroid2.ui.activity.AccountsActivity"
}

# ================== 元素等待超时 ==================
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20

