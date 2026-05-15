# comm/base.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import logging
from comm.tools import Tools

# 导入统一配置
from config.config import (
    BASE_DIR,
    APPIUM_HOST,
    DEVICE_CONFIG,
    APP_CONFIG,
    IMPLICIT_WAIT,
    EXPLICIT_WAIT,
    LOG_DIR,
    LOG_FILE_NAME,
    LOG_LEVEL
)

class Driver:
    def __init__(self):
        self.logger = self._setup_logging()

    def _setup_logging(self):
        """从 config.py 读取日志配置，完全可配置化"""
        # 日志文件完整路径
        log_file = os.path.join(LOG_DIR, LOG_FILE_NAME)

        # 自动创建目录
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

        # 设置日志级别
        level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
        logger = logging.getLogger(__name__)
        logger.setLevel(level)

        # 避免重复添加 handler
        if not logger.handlers:
            # 文件输出
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(level)

            # 控制台输出
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

            # 日志格式
            formatter = logging.Formatter(
                '%(asctime)s [%(levelname)s] %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger

    def open_app(self, appPackage=None, appActivity=None):
        caps = DEVICE_CONFIG.copy()
        caps["appPackage"] = appPackage or APP_CONFIG["appPackage"]
        caps["appActivity"] = appActivity or APP_CONFIG["appActivity"]
        print(caps)

        options = UiAutomator2Options().load_capabilities(caps)
        driver = webdriver.Remote(
            command_executor=APPIUM_HOST,
            options=options
        )
        driver.implicitly_wait(IMPLICIT_WAIT)
        self.logger.info("✅ 应用启动成功")
        return driver

    def find_element(self, driver, by, value, timeout=EXPLICIT_WAIT):
        try:
            return WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except:
            self.logger.error(f"❌ 元素未找到: {by}={value}")
            return None

    def element_click(self, driver, by, value):
        el = self.find_element(driver, by, value)
        if el:
            el.click()
            self.logger.info(f"✅ 点击元素: {by}={value}")

    def element_send_keys(self, driver, by, value, text):
        el = self.find_element(driver, by, value)
        if el:
            el.clear()
            el.send_keys(text)
            self.logger.info(f"✅ 输入内容: {text}")

    def http_get(url, params=None, headers=None):
        """
        封装 GET 请求
        :param url: 请求地址
        :param params: URL 参数
        :param headers: 请求头
        :return: 打印状态码、响应体、响应时间
        """
        try:
            start = time.time()
            response = requests.get(url, params=params, headers=headers, timeout=10)
            end = time.time()

            print("=" * 50)
            print(f"【GET 请求】{url}")
            print(f"状态码：{response.status_code}")
            print(f"响应时间：{round((end - start) * 1000, 2)} ms")
            print("-" * 30)
            print("响应体：")
            try:
                # 尝试 JSON 格式化输出
                print(response.json())
            except:
                # 普通文本输出
                print(response.text[:500])  # 只输出前500字符，避免太长
            print("=" * 50)
            return response

        except Exception as e:
            print(f"请求失败：{str(e)}")



if __name__ == '__main__':
    driver = Driver()
    dr = driver.open_app()
    driver.element_click(dr, AppiumBy.ID, "com.seafile.seadroid2:id/list_item_account_title2")