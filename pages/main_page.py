from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def dropdown(self) -> WebElement:
        return self.is_clickable(MainPageLocators.DROPDOWN)

    def link_my_account(self) -> WebElement:
        return self.is_clickable(MainPageLocators.LINK_MY_ACCOUNT)

    def link_my_wish(self) -> WebElement:
        return self.is_clickable(MainPageLocators.LINK_MY_WISH)

    def link_sign_out(self) -> WebElement:
        return self.is_clickable(MainPageLocators.LINK_SIGN_OUT)
