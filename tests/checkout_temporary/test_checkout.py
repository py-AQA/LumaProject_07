from time import sleep

from pages.guest_shipping_address_page import GuestShippingAddressPage
from pages.main_page import MainPage


class TestCheckOutGuest:
    def test_checkout_bolo_sport_watch(self, driver, random_email, random_first_name, random_last_name,
                                       random_ru_zip_code, random_street, random_city, random_ru_phone_number):
        page = MainPage(driver)
        page.open()
        page.add_bolo_sport_watch_to_cart()
        checkout_page = GuestShippingAddressPage(driver)
        checkout_page.open()
        checkout_page.checkout_button().click()
        checkout_page.fill_all_require_field(email=random_email, firstname=random_first_name, lastname=random_last_name,
                                             street_1=random_street, city=random_city, zip_code=random_ru_zip_code,
                                             phone_number=random_ru_phone_number)
        # todo element click intercepted: Element <td class="col col-carrier" data-bind="attr: {'id': 'label_carrier_'
        checkout_page.select_flat_rate_shipping().click()
        checkout_page.step_2_next_button().click()
        sleep(6)
        checkout_page.place_order_button().click()
        assert checkout_page.email_order().text == random_email, 'неправильно отобразился email после заказа'
        assert checkout_page.current_url == "https://magento.softwaretestingboard.com/checkout/onepage/success/", 'не удалось сделать гостевой заказ'
