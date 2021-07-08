from selenium.webdriver.common.by import By
from test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    def add_member(self):
        """
        添加成员操作
        :return:
        """
        pass

    def get_member(self):
        """
        获取成员列表，用来做断言
        :return:
        """

        member_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # 列表推导式
        member_list_res = [i.text for i in member_list]
        return member_list_res



