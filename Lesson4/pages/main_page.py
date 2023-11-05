from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Lesson4.base.seleniumbase import BasePage

DROPDOWN = (By.CSS_SELECTOR, '.customer-name button.action.switch')
LINK_MY_ACCOUNT = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/customer/account/'])[1]")
LINK_MY_WISH = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/wishlist/'])[1]")
LINK_SIGN_OUT = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/customer/account/logout/'])[1]")


class MainPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def dropdown(self) -> WebElement:
        return self.is_clickable(DROPDOWN)

    def link_my_account(self) -> WebElement:
        return self.is_clickable(LINK_MY_ACCOUNT)

    def link_my_wish(self) -> WebElement:
        return self.is_clickable(LINK_MY_WISH)

    def link_sign_out(self) -> WebElement:
        return self.is_clickable(LINK_SIGN_OUT)
