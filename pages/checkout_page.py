from selenium.webdriver.common.by import By

from base.base_page import BasePage
from data.locators import CheckoutPageLocators, CartLocators


class CheckoutPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/checkout/"

    URL_ORDER_PLACED_SUCCESS = "https://magento.softwaretestingboard.com/checkout/onepage/success/"

    def __init__(self, driver, url=URL, open=True):
        super().__init__(driver, url, open)

    def email_field(self):
        return self.is_visible(CheckoutPageLocators.EMAIL_FIELD)

    def first_name_field(self):
        return self.is_visible(CheckoutPageLocators.FIRST_NAME_FIELD)

    def last_name_field(self):
        return self.is_visible(CheckoutPageLocators.LAST_NAME_FIELD)

    def street_address_1_field(self):
        return self.is_visible(CheckoutPageLocators.STREET_1_FIELD)

    def city_field(self):
        return self.is_visible(CheckoutPageLocators.CITY_FIELD)

    def postcode_field(self):
        return self.is_visible(CheckoutPageLocators.POSTCODE_FIELD)

    def country_dropdown_field(self):
        return self.is_visible(CheckoutPageLocators.COUNTRY_FIELD_DROPDOWN)

    def state_dropdown_field(self):
        return self.is_visible(CheckoutPageLocators.STATE_FIELD_DROPDOWN)

    def select_state(self, state):
        return self.is_clickable((By.XPATH, f"//*[@data-title='{state}']")).click()

    def select_russia_country(self):
        return self.is_clickable(CheckoutPageLocators.RUSSIA_COUNTRY_DROPDOWN)

    def phone_number_field(self):
        return self.is_visible(CheckoutPageLocators.PHONE_NUMBER_FIELD)

    def wait_overlay_closed(self):
        return self.is_invisible(CheckoutPageLocators.OVERLAY)

    def checkout_button(self):
        return self.is_clickable(CartLocators.CART_PROCEED_TO_CHECKOUT_BUTTON)

    def step_2_next_button(self):
        return self.is_clickable(CheckoutPageLocators.CHECKOUT_STEP_2_NEXT_BUTTON)

    def place_order_button(self):
        return self.is_clickable(CheckoutPageLocators.PLACE_ORDER_BUTTON)

    def order_number_guest(self):
        return self.is_visible(CheckoutPageLocators.ORDER_NUMBER_GUEST)

    def order_number_user(self):
        return self.is_visible(CheckoutPageLocators.ORDER_NUMBER_AS_USER)

    def email_order(self):
        return self.is_visible(CheckoutPageLocators.EMAIL_ORDER)

    def select_flat_rate_shipping(self):
        self.is_loading()
        self.is_clickable(CheckoutPageLocators.SHIPPING_FLAT_RATE).click()
        # self.is_loading()
        self.step_2_next_button().click()
        self.wait_overlay_closed()

    def place_order(self):
        self.place_order_button().click()
        self.wait_overlay_closed()

    def success_place_order_message(self):
        return self.is_visible(CheckoutPageLocators.SUCCESS_PLACE_ORDER_MESSAGE)

    def fill_all_require_field_as_gues_us_shipping(self, state, email, firstname, lastname, street_1, city, postcode,
                                                   phone_number):
        self.state_dropdown_field().click()
        self.select_state(state)
        self.email_field().send_keys(email)
        self.first_name_field().send_keys(firstname)
        self.last_name_field().send_keys(lastname)
        self.street_address_1_field().send_keys(street_1)
        self.city_field().send_keys(city)
        self.postcode_field().send_keys(postcode)
        self.phone_number_field().send_keys(phone_number)

    def fill_all_require_field_as_gues_ru_shipping(self, email, firstname, lastname, street_1, city, postcode,
                                                   phone_number):
        self.country_dropdown_field().click()
        self.select_russia_country().click()
        self.email_field().send_keys(email)
        self.first_name_field().send_keys(firstname)
        self.last_name_field().send_keys(lastname)
        self.street_address_1_field().send_keys(street_1)
        self.city_field().send_keys(city)
        self.postcode_field().send_keys(postcode)
        self.phone_number_field().send_keys(phone_number)

    def fill_all_require_field_as_user_ru_shipping(self, street_1, city, postcode, phone_number):
        self.country_dropdown_field().click()
        self.select_russia_country().click()
        self.street_address_1_field().send_keys(street_1)
        self.city_field().send_keys(city)
        self.postcode_field().send_keys(postcode)
        self.phone_number_field().send_keys(phone_number)

    def fill_all_require_field_as_user_us_shipping(self, state, street_1, city, postcode,
                                                   phone_number):
        self.state_dropdown_field().click()
        self.select_state(state)
        self.street_address_1_field().send_keys(street_1)
        self.city_field().send_keys(city)
        self.postcode_field().send_keys(postcode)
        self.phone_number_field().send_keys(phone_number)

    # ФУНКЦИЯ ВЕШАЕТ ЗАКАЗ КАК ГОСТЬ И ВОЗВРАЩАЕТ НОМЕР ЗАКАЗА
    def full_guest_place_order_ru_address(self, email, firstname, lastname, street_1, city, postcode,
                                          phone_number) -> str:
        self.fill_all_require_field_as_gues_ru_shipping(email, firstname, lastname, street_1, city, postcode,
                                                        phone_number)
        self.select_flat_rate_shipping()
        self.place_order()
        order_id = self.order_number_guest().text
        assert self.current_url == self.URL_ORDER_PLACED_SUCCESS
        return order_id

    def full_guest_place_order_us_address(self, state, email, firstname, lastname, street_1, city, postcode,
                                          phone_number) -> str:
        self.fill_all_require_field_as_gues_us_shipping(state, email, firstname, lastname, street_1, city, postcode,
                                                        phone_number)
        self.select_flat_rate_shipping()
        self.place_order()
        order_id = self.order_number_guest().text
        assert self.current_url == self.URL_ORDER_PLACED_SUCCESS
        return order_id

    def full_user_place_order_flat_rate(self, state, street_1, city, postcode,
                                        phone_number) -> str:
        self.fill_all_require_field_as_user_us_shipping(state, street_1, city, postcode,
                                                        phone_number)
        self.select_flat_rate_shipping()
        self.place_order()
        order_id = self.order_number_user().text
        assert self.current_url == self.URL_ORDER_PLACED_SUCCESS
        return order_id
