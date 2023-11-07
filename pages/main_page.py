from selenium.webdriver.common.by import By
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

    def link_bags_catalog(self) -> WebElement:
        return self.is_clickable(MainPageLocators.LINK_BAGS_CATALOG)

    def item_add_to_cart_button(self, item_number):
        return self.is_clickable((By.XPATH,
                                  f"(//div[@class='product details product-item-details']//button[@title='Add to Cart'])[{item_number}]"))

    def add_item_from_gear_watches_catalog_to_cart(self, item_number):
        """1 ЧАСЫ ЗАБАГОВАНЫ"""
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.link_watches_catalog().click()
        self.hold_mouse_on_element((By.XPATH, f"(//div[@class='product details product-item-details'])[{item_number}]"))
        self.item_add_to_cart_button(item_number).click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)
        return self

    def add_item_from_gear_bags_catalog_to_cart(self, item_number):
        """1,8,9 СУМКИ ЗАБАГОВАНЫ """
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.link_bags_catalog().click()
        self.hold_mouse_on_element((By.XPATH, f"(//div[@class='product details product-item-details'])[{item_number}]"))
        self.item_add_to_cart_button(item_number).click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)
        return self
    # ДОБАВИЛ ДАНЯ КОНЕЦ
