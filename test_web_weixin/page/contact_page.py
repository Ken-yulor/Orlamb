from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    def goto_add_member(self):
        # 避免出发python的循环导入机制
        # 这里使用了函数内引用
        from test_web_weixin.page.add_member_page import AddMember
        """
        添加成员操作
        :return:
        """
        # 添加显示等待，保证按钮可以点击
        WebDriverWait(self.driver, 9).until(
            expected_conditions.element_to_be_clickable(self._location_goto_add_member))
        # 通过层级定位
        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)

    def get_member(self):
        """
        获取成员列表，用来做断言
        :return:
        """

        member_list = self.finds(*self._location_member_list)
        # 列表推导式
        member_list_res = [i.text for i in member_list]
        return member_list_res



