from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import MainPageLocators, MyAccountPageLocators, CartLocators, ItemPageLocators, BasePageLocators


class MainPage(BasePage):
    def __init__(self, driver, url=MainPageLocators.URL , open_url=True):
        super().__init__(driver, url, open_url)

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

    def go_to_men_jacket_catalog(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_MEN_CATALOG)
        self.hold_mouse_on_element(MainPageLocators.LINK_MEN_TOPS_CATALOG)
        self.is_clickable(MainPageLocators.LINK_MEN_JACKETS_CATALOG).click()

    def go_to_women_pants_catalog(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_WOMEN_CATALOG)
        self.hold_mouse_on_element(MainPageLocators.LINK_WOMEN_BOTTOMS_CATALOG)
        self.is_clickable(MainPageLocators.LINK_WOMEN_BOTTOMS_PANTS_CATALOG).click()

    def item_add_to_cart_button(self, item_number):
        return self.is_clickable((By.XPATH,
                                  f"(//div[@class='product details product-item-details']//button[@title='Add to Cart'])[{item_number}]"))

    def driven_backpack(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_DRIVEN_BACKPACK)
        return self.is_clickable(MainPageLocators.ADD_TO_CART_DRIVEN_BACKPACK_BUTTON)

    def clamber_watch(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_CLAMBER_WATCH)
        return self.is_clickable(MainPageLocators.ADD_TO_CART_CLAMBER_WATCH_BUTTON)

    def success_add_to_cart_message(self):
        return self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)

    def text_success_message(self, item_name):
        return f'You added {item_name} to your shopping cart.'

    def quantity_field_item(self, quantity):
        self.is_clickable(ItemPageLocators.QUANTITY_OF_ITEM).clear()
        return self.is_clickable(ItemPageLocators.QUANTITY_OF_ITEM).send_keys(quantity)

    def cart_counter(self):
        self.success_add_to_cart_message()
        return self.is_visible(CartLocators.CART_COUNTER_ICON)

    def error_quantity_msg(self):
        return self.is_visible(ItemPageLocators.QUANTITY_ERROR_MSG)

    def error_qty_is_not_available(self):
        return self.is_visible(BasePageLocators.MSG_ERROR)

    def select_green_m_montana_jacket(self):
        self.is_clickable(MainPageLocators.MONTANA_JACKET_SIZE_M_BUTTON).click()
        self.is_clickable(MainPageLocators.MONTANA_JACKET_GREEN_COLOR_BUTTON).click()
        self.hold_mouse_on_element(MainPageLocators.LINK_MONTANA_JACKET)
        self.is_clickable(MainPageLocators.ADD_TO_CART_MONTANA_JACKET_BUTTON).click()

    def select_blue_28_portia_capri_pants(self):
        self.is_clickable(MainPageLocators.PORTIA_CAPRI_PANTS_BLUE_COLOR_BUTTON).click()
        self.is_clickable(MainPageLocators.PORTIA_CAPRI_PANTS_SIZE_28_BUTTON).click()
        self.hold_mouse_on_element(MainPageLocators.LINK_PORTIA_CAPRI_PANTS)
        self.is_clickable(MainPageLocators.ADD_TO_CART_PORTIA_CAPRI_PANTS_BUTTON).click()

    def add_item_from_gear_watches_catalog_to_cart(self, item_number):
        """1 ЧАСЫ ЗАБАГОВАНЫ"""
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.link_watches_catalog().click()
        self.hold_mouse_on_element((By.XPATH, f"(//div[@class='product details product-item-details'])[{item_number}]"))
        self.item_add_to_cart_button(item_number).click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)


    def add_item_from_gear_bags_catalog_to_cart(self, item_number):
        """1,8,9 СУМКИ ЗАБАГОВАНЫ """
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.link_bags_catalog().click()
        self.hold_mouse_on_element((By.XPATH, f"(//div[@class='product details product-item-details'])[{item_number}]"))
        self.item_add_to_cart_button(item_number).click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)

    def add_driven_backpack_from_backpacks_catalog_to_cart(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.link_bags_catalog().click()
        self.driven_backpack().click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)

    def add_clamber_watch_from_watches_catalog_to_cart(self):
        self.hold_mouse_on_element(MainPageLocators.LINK_GEAR_CATALOG)
        self.link_watches_catalog().click()
        self.clamber_watch().click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)

    def add_montana_wind_jacket_from_men_jacket_to_cart(self):
        self.go_to_men_jacket_catalog()
        self.select_green_m_montana_jacket()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)

    def add_yoga_kit_from_gear_fitness_to_cart(self, quantity: int = 1):
        '''МОЖНО УКАЗАТЬ КОЛИЧЕСТВО И ДОБАВИТЬ СРАЗУ НЕСКОЛЬКО'''
        self.is_clickable(MainPageLocators.CUSTOMIZE_AND_ADD_TO_CART_BUTTON).click()
        self.is_clickable(MainPageLocators.BALL_65_CM).click()
        self.is_clickable(MainPageLocators.YOGA_STRAP_10_FOOT).click()
        self.quantity_field_item(quantity)
        self.is_clickable(MainPageLocators.ADD_TO_CART_FROM_ITEM_BUTTON).click()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)

    def add_portia_capri_28_blue_color_to_cart(self):
        self.go_to_women_pants_catalog()
        self.select_blue_28_portia_capri_pants()
        self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE)

    def add_zero_items_to_cart(self, quantity: int = 0):
        self.is_clickable(MainPageLocators.CUSTOMIZE_AND_ADD_TO_CART_BUTTON).click()
        self.quantity_field_item(quantity)
        self.is_clickable(MainPageLocators.ADD_TO_CART_FROM_ITEM_BUTTON).click()
        self.error_quantity_msg()

    def add_more_than_maximum_items_to_cart(self, quantity: int = 10001):
        self.is_clickable(MainPageLocators.CUSTOMIZE_AND_ADD_TO_CART_BUTTON).click()
        self.quantity_field_item(quantity)
        self.is_clickable(MainPageLocators.ADD_TO_CART_FROM_ITEM_BUTTON).click()
        self.error_quantity_msg()

    def add_negative_items_to_cart(self, quantity: int = -1):
        self.is_clickable(MainPageLocators.CUSTOMIZE_AND_ADD_TO_CART_BUTTON).click()
        self.quantity_field_item(quantity)
        self.is_clickable(MainPageLocators.ADD_TO_CART_FROM_ITEM_BUTTON).click()
        self.error_quantity_msg()

    def add_more_than_in_stock_items_to_cart(self, quantity: int = 10000):
        self.is_clickable(MainPageLocators.CUSTOMIZE_AND_ADD_TO_CART_BUTTON).click()
        self.quantity_field_item(quantity)
        self.is_clickable(MainPageLocators.ADD_TO_CART_FROM_ITEM_BUTTON).click()
        self.error_qty_is_not_available()

    # ДОБАВИЛ ДАНЯ КОНЕЦ
