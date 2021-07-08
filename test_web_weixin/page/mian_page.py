from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web_weixin.page.add_member_page import AddMember
from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contact_page import ContactPage


class MainPage(BasePage):
    _location_goto_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    def goto_add_member(self):
        """跳转到添加成员页面
        """
        # 解元组操作，把元组内的元素拆分作为不同的参数传入
        self.driver.find_element(*self._location_goto_member).click()
        return AddMember(self.driver)

    def goto_contact(self):
        """跳转到通讯录页面
        """
        return ContactPage()

