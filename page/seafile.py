from comm.base import *

# 封装页面元素，封装页面操作
class Seafile(Driver):
    #账号
    account = (AppiumBy.ID,"com.seafile.seadroid2:id/list_item_account_title")
    #3个点
    menu_overflow = (AppiumBy.ID,"com.seafile.seadroid2:id/menu_overflow")
    #新建资料库
    zlk_new = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.seafile.seadroid2:id/title" and @text="新建资料库"]')
    #新建资料库名称
    zlk_name = (AppiumBy.ID,"com.seafile.seadroid2:id/new_repo_name")
    #确定按钮
    button_ok = (AppiumBy.ID,"android:id/button1")

    #类方法，登录
    def login(self,dr):
        self.element_click(dr,*self.account)
    def zlk_add(self,dr,name):
        self.element_click(dr,*self.menu_overflow)
        self.element_click(dr,*self.zlk_new)
        self.element_send_keys(dr,*self.zlk_name,name)
        self.element_click(dr,*self.button_ok)


    #商品对应的按钮
    def button_zlk(self,name):
        string = f'(//*[contains(@text,"{name}")]/../..//android.widget.ImageView)[3]'
        return (AppiumBy.XPATH,string)
    #删除按钮
    button_zlk_delete = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.seafile.seadroid2:id/bs_list_title" and @text="删除"]')


    #删除资料库
    def zlk_delete(self,dr,name):
        self.element_click(dr,*self.button_zlk(name))
        self.element_click(dr,*self.button_zlk_delete)
        self.element_click(dr,*self.button_ok)

if __name__ == '__main__':
    #创建driver对象
    driver = Seafile()
    #打开app
    dr = driver.open_app()
    #登录
    driver.login(dr)
    #新建资料库
    driver.zlk_delete(dr,'自动化测试2026-04-15 13:53:11')