from time import sleep

from data.fake_data import FakeData
from pages.create_account import CreateAccountPage
from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage


class TestCheckOutAsGuest(FakeData):
    def test_buy_watch_ru_shipping(self, driver):
        page = MainPage(driver)
        page.add_item_from_gear_watches_catalog_to_cart(2)
        checkout_page = CheckoutPage(driver)
        email = self.email
        checkout_page.fill_all_require_field_as_gues_ru_shipping(email, self.first_name, self.last_name, self.street_address,
                                                         self.city, self.postcode, self.phone_number)
        checkout_page.select_flat_rate_shipping()
        checkout_page.place_order()
        assert checkout_page.email_order().text == email, 'неправильно отобразился email после заказа'
        assert checkout_page.current_url == CheckoutPage.URL_ORDER_PLACED_SUCCESS, 'не удалось сделать гостевой заказ'

    def test_buy_bags_us_shipping(self, driver):
        page = MainPage(driver)
        page.open()
        page.add_item_from_gear_watches_catalog_to_cart(2)
        checkout_page = CheckoutPage(driver)
        checkout_page.open()
        email = self.email
        state = self.state
        checkout_page.fill_all_require_field_as_gues_us_shipping(state, email, self.first_name, self.last_name,
                                                         self.street_address, self.city, self.us_postcode_state(state),
                                                         self.phone_number)
        checkout_page.select_flat_rate_shipping()
        checkout_page.place_order()
        assert checkout_page.email_order().text == email, 'неправильно отобразился email после заказа'
        assert checkout_page.current_url == CheckoutPage.URL_ORDER_PLACED_SUCCESS, 'не удалось сделать гостевой заказ'

class TestCheckOutAsUser(FakeData):

    def test_buy_watches_us_shipping(self, driver):
        page = CreateAccountPage(driver)
        email = self.email
        page.create(self.first_name,self.last_name,email,self.password)
        MainPage(driver).add_item_from_gear_watches_catalog_to_cart(2)
        page = CheckoutPage(driver)
        page.open()
        page.fill_all_require_field_as_user_ru_shipping(self.street_address,
                                                         self.city, self.postcode, self.phone_number)
        page.select_flat_rate_shipping()
        page.place_order()
        assert page.success_place_order_message().text == "Thank you for your purchase!"
        assert page.current_url == CheckoutPage.URL_ORDER_PLACED_SUCCESS, 'не удалось сделать заказ как пользователь'
