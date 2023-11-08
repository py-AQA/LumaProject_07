from time import sleep

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class Demo(BasePage):
    LOCATOR = (By.CSS_SELECTOR, "div.demo")
    TEXT = ("This is a demo store to test your test automaiton scripts. "
                 "No orders will be fulfilled. If you are facing any issue, "
                 "email us at hello@softwaretestingboard.com.")
    BACKGROUND_COLOR = "rgba(255, 1, 1, 1)"

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def demo(self):
        return self.is_visible(self.LOCATOR)

    def ck_css(self):
        # todo ffox AssertionError
        assert self.demo.value_of_css_property("background-color") == self.BACKGROUND_COLOR

    def ck_text(self):
        assert self.demo.text == self.TEXT


class Copyright(BasePage):
    LOCATOR = (By.CSS_SELECTOR, ".copyright span")
    TEXT = "Copyright © 2013-present Magento, Inc. All rights reserved."
    BACKGROUND_COLOR = "#6e716e"

    def el(self):
        return self.is_visible(self.LOCATOR)

    def ck_css(self):
        print('>>>', self.el().value_of_css_property("background-color"))
        assert self.el().value_of_css_property("background-color") == self.BACKGROUND_COLOR

    def ck_text(self):
        assert self.el().text == self.TEXT


class Page(BasePage):
    URL = "about:blank"
    MSG = (By.CSS_SELECTOR, '[data-ui-id="message-success"]')

    def __init__(self, driver, url=URL):
        super().__init__(driver, url, open_url=False)

        self.demo = Demo(driver)
        # self.footer = Footer(driver)
        self.copyright = Copyright(driver)

    @property
    def msg(self):
        text = self.is_visible(self.MSG).text
        return text
