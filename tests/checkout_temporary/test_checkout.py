from data.fake_data import FakeData
from pages.guest_shipping_address_page import GuestShippingAddressPage
from pages.main_page import MainPage


class TestCheckOutGuest(FakeData):
    def test_checkout_bolo_sport_watch_ru_shipping(self, driver):
        page = MainPage(driver)
        page.open()
        page.add_bolo_sport_watch_to_cart()
        checkout_page = GuestShippingAddressPage(driver)
        checkout_page.open()
        checkout_page.checkout_button().click()
        email = self.email
        checkout_page.fill_all_require_field_ru_shipping(email, self.first_name, self.last_name, self.street_address,
                                                         self.city, self.postcode, self.phone_number)
        checkout_page.select_flat_rate_shipping().click()
        checkout_page.step_2_next_button().click()
        checkout_page.wait_overlay_closed()
        checkout_page.place_order_button().click()
        assert checkout_page.email_order().text == email, 'неправильно отобразился email после заказа'
        assert checkout_page.current_url == GuestShippingAddressPage.URL_ORDER_PLACED_SUCCESS, 'не удалось сделать гостевой заказ'

    def test_checkout_bolo_sport_watch_us_shipping(self, driver):
        page = MainPage(driver)
        page.open()
        page.add_bolo_sport_watch_to_cart()
        checkout_page = GuestShippingAddressPage(driver)
        checkout_page.open()
        checkout_page.checkout_button().click()
        email = self.email
        state = self.state
        checkout_page.fill_all_require_field_us_shipping(state, email, self.first_name, self.last_name,
                                                         self.street_address, self.city, self.us_postcode_state(state),
                                                         self.phone_number)
        checkout_page.select_flat_rate_shipping().click()
        checkout_page.step_2_next_button().click()
        checkout_page.wait_overlay_closed()
        checkout_page.place_order_button().click()
        assert checkout_page.email_order().text == email, 'неправильно отобразился email после заказа'
        assert checkout_page.current_url == GuestShippingAddressPage.URL_ORDER_PLACED_SUCCESS, 'не удалось сделать гостевой заказ'