from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import ItemPageLocators, WishListPageLocators


class ItemToWishList(BasePage):
    URL = 'https://magento.softwaretestingboard.com/breathe-easy-tank.html'
    MESSAGE = 'Breathe-Easy Tank has been added to your Wish List. Click here to continue shopping.'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def add_item_to_wish_list(self):
        return self.is_clickable(ItemPageLocators.ADD_TO_WISH_LIST)

    @property
    def success_message(self) -> str:
        return self.is_visible(WishListPageLocators.SUCCESS_MESSAGE).text








