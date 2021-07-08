import pytest
from test_web_weixin.page.mian_page import MainPage

class TestAddMember:

    def setup_class(self):
        self.main = MainPage()


    def test_add_member(self):
        """
        添加成员测试用例
        :return:
        """
        # 1.跳转添加成员页面
        # 2.添加成员
        # 3.自动跳转到通讯录页面
        res = self.main.goto_add_member().add_member().get_member()
        assert "xx" in res
    @pytest.mark.parametrize("acctid, phone, expect_res",
                             [{"赫敏", "13688889999", "该账号已被'xx'占有"}])
    def test_add_member_fail(self, acctid, phone, expect_res):
        """
        :param acctid: ID信息
        :param phone: 手机信息
        :return:
        """
        res = self.main.goto_add_member().add_member_fail()
        assert res == expect_res

    def test_add_member_by_contact(self):
        """
        通过通讯录页面添加成员
        :return:
        """
        # 判断是否添加成功的断言
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        assert "xx" in res

    def teardown_class(self):
        self.main.quit()