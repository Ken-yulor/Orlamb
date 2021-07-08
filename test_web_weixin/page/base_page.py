import select
import time

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver



class BasePage:

    def __init__(self, base_driver=None):
        # 注解,不是赋值，用作IDE的类型提示
        base_driver: WebDriver
        # 初始化实例参数
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.__cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def __cookie_login(self):
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def find(self, by, value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value=None):
        if value is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by=by, value=value)

    def quit(self):
        self.driver.quit()