from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import MainPageLocators, MyAccountPageLocators


class MainPage(BasePage):
    def __init__(self, driver, url=MainPageLocators.URL , open = True):
        super().__init__(driver, url, open)

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

    def link_fitness_catalog(self) -> WebElement:
        return self.is_clickable(MainPageLocators.LINK_FITNESS_CATALOG)

    def go_to_men_jacket_catalog(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_MEN_CATALOG)
        self.hold_mouse_on_element(MainPageLocators.LINK_MEN_TOPS_CATALOG)
        self.is_clickable(MainPageLocators.LINK_MEN_JACKETS_CATALOG).click()

    def go_to_fitness_catalog(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.is_clickable(MainPageLocators.LINK_FITNESS_CATALOG).click()

    def item_add_to_cart_button(self, item_number):
        return self.is_clickable((By.XPATH,
                                  f"(//div[@class='product details product-item-details']//button[@title='Add to Cart'])[{item_number}]"))

    def driven_backpack(self):
        self.hold_mouse_on_element(MainPageLocators.HOLD_LINK_DRIVEN_BACKPACK)
        return self.is_clickable(MainPageLocators.ADD_TO_CART_DRIVEN_BACKPACK_BUTTON)

    def clamber_watch(self):
        self.hold_mouse_on_element(MainPageLocators.HOLD_LINK_CLAMBER_WATCH)
        return self.is_clickable(MainPageLocators.ADD_TO_CART_CLAMBER_WATCH_BUTTON)

    def select_green_m_montana_jacket(self):
        self.is_clickable(MainPageLocators.MONTANA_JACKET_SIZE_M_BUTTON).click()
        self.is_clickable(MainPageLocators.MONTANA_JACKET_GREEN_COLOR_BUTTON).click()
        self.hold_mouse_on_element(MainPageLocators.HOLD_LINK_MONTANA_JACKET)
        self.is_clickable(MainPageLocators.ADD_TO_CART_MONTANA_JACKET_BUTTON).click()


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

    def add_driven_backpack_from_backpacks_catalog_to_cart(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.link_bags_catalog().click()
        self.driven_backpack().click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)
        return self

    def add_clamber_watch_from_watches_catalog_to_cart(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.link_watches_catalog().click()
        self.clamber_watch().click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)
        return self

    def add_montana_wind_jacket_from_men_jacket_to_cart(self):
        self.go_to_men_jacket_catalog()
        self.select_green_m_montana_jacket()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)
        return self

    def add_yoga_kit_from_gear_fitness_to_cart(self):
        self.is_clickable(MainPageLocators.CUSTOMIZE_AND_ADD_TO_CART_BUTTON).click()
        self.is_clickable(MainPageLocators.BALL_65_CM).click()
        self.is_clickable(MainPageLocators.YOGA_STRAP_10_FOOT).click()
        self.is_clickable(MainPageLocators.ADD_TO_CART_FROM_ITEM_BUTTON).click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)
        return self
    # ДОБАВИЛ ДАНЯ КОНЕЦ
