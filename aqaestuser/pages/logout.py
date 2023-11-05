from time import sleep

from pages.abstract import Page


class LogoutPage(Page):
    URL = "https://magento.softwaretestingboard.com/customer/account/logout/"
    URL_DONE = "https://magento.softwaretestingboard.com/customer/account/logoutSuccess/"

    def __init__(self, driver, url=URL):
        super().__init__(driver)
        self.url = url
        sleep(1)
