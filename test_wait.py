from selenium import webdriver

from main import Main


class Test_Wait:
    def setup(self):
        main = Main
        main.click_frist_link().title()