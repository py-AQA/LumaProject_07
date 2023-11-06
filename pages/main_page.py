from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import MainPageLocators, MyAccountPageLocators


class MainPage(BasePage):
    def __init__(self, driver, url=MainPageLocators.URL):
        super().__init__(driver, url)

    def dropdown(self) -> WebElement:
        return self.is_clickable(MainPageLocators.DROPDOWN)

    def link_my_account(self) -> WebElement:
        return self.is_clickable(MainPageLocators.LINK_MY_ACCOUNT)

    def link_my_wish(self) -> WebElement:
        return self.is_clickable(MainPageLocators.LINK_MY_WISH)

    def link_sign_out(self) -> WebElement:
        return self.is_clickable(MainPageLocators.LINK_SIGN_OUT)

    # ДОБАВИЛ ДАНЯ , НУЖНА ПРОВЕРКА
    def link_cart(self) -> WebElement:
        return self.is_visible(MainPageLocators.LINK_CART)

    def checkout_button_from_link_cart(self):
        return self.is_clickable(MainPageLocators.CHECKOUT_BUTTON_LINK_CART)

    def link_watches_catalog(self) -> WebElement:
        return self.is_clickable(MainPageLocators.LINK_WATCHES_CATALOG)

    def bolo_sport_watch_add_to_cart_button(self):
        return self.is_clickable(MainPageLocators.ADD_TO_CART_BOLO_SPORT_WATCH_BUTTON)

    def add_bolo_sport_watch_to_cart(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.link_watches_catalog().click()
        self.hold_mouse_on_element(MainPageLocators.HOLD_LINK_BOLO_SPORT_WATCH)
        self.bolo_sport_watch_add_to_cart_button().click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)
        return self
    # ДОБАВИЛ ДАНЯ КОНЕЦ