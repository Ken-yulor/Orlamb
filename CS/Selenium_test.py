import time

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        # 实例化ChromeDriver
        self.driver = webdriver.Chrome()
        # 设置隐性等待10s
        self.driver.implicitly_wait(10)
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
        # sleep(5)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院-软件自动化测试开发培训_接口性能测试").click()
        # self.vars["win9915"] = self.wait_for_window(2000)
        self.driver.close()

class TestWework:

    def test_demo(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = '127.0.0.1:9222'
        driver = webdriver.Chrome(options=opt)
        driver.get("http://www.baidu.com")