import time

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    # def wait_for_window(self, timeout = 2):
    #     time.sleep(round(timeout / 1000))
    #     wh_now = self.driver.window_handles
    #     wh_then = self.vars['window_handles']
    #     if len(wh_now) > len(wh_then):
    #         return set(wh_now).difference(set(wh_then)).pop()
    def test_demo(self):
        self.driver.get("https://www.baidu.com")
        self.driver.set_window_size(1680, 939)
        self.driver.find_element(By.ID, "kw").clear()
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "su").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 - 测试开发工程师的黄埔军校").click()
        self.vars["win9915"] = self.wait_for_window(2000)
        self.driver.close()

