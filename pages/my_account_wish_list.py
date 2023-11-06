from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import MyAccountPageLocators, WishListPageLocators


class MyAccountWishListPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/wishlist/'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def check_item_present(self):
        return self.is_visible(WishListPageLocators.ITEM_13740)


