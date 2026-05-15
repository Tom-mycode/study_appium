# from comm.base import *
# driver = Driver().open_app()
import time

# el1 = driver.find_element(by=AppiumBy.ID, value="com.seafile.seadroid2:id/list_item_account_title")
# el1.click()
# el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="More")
# el2.click()
# el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.seafile.seadroid2:id/title\" and @text=\"新建资料库\"]")
# el3.click()
# el4 = driver.find_element(by=AppiumBy.ID, value="com.seafile.seadroid2:id/new_repo_name")
# el4.send_keys("胡显到此一游")
# el5 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
# el5.click()
# el6 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.RelativeLayout[@resource-id=\"com.seafile.seadroid2:id/expandable_toggle_button\"])[1]/android.widget.ImageView")
# el6.click()
# el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.seafile.seadroid2:id/bs_list_title\" and @text=\"删除\"]")
# el7.click()
# el8 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
# el8.click()


from page.seafile import *
driver = Seafile().open_app()
Seafile().login(driver)
time.sleep(3)
Seafile().zlk_add(driver, "呀哈哈~再见！")
time.sleep(3)
Seafile().zlk_delete(driver,"呀哈哈~再见！")
