from data.locators import OrdersAndReturnsPageLocators
from pages.guest_shipping_address_page import GuestShippingAddressPage
from pages.main_page import MainPage
from pages.orders_and_returns_page import OrdersAndReturnsPage


# ВОЗМОЖНО НУЖНО УСОВЕРШЕНСТВОВАТЬ
class TestCheckOrder:
    # ФУНКЦИЯ ВЕШАЕТ РАНДОМНЫЙ ОРДЕР И ПРОВЕРЯЕТ ЕГО В БАЗЕ ПО ЕМЕЙЛУ
    def test_check_order_by_email(self, driver, random_email, random_first_name, random_last_name, random_ru_zip_code,
                                  random_street, random_city, random_ru_phone_number):
        page = MainPage(driver)
        page.open()
        page.add_bolo_sport_watch_to_cart()
        checkout_page = GuestShippingAddressPage(driver)
        order_id = checkout_page.full_guest_place_order(email=random_email, firstname=random_first_name,
                                                        lastname=random_last_name,
                                                        street_1=random_street, city=random_city,
                                                        zip_code=random_ru_zip_code,
                                                        phone_number=random_ru_phone_number)
        orders_and_returns_page = OrdersAndReturnsPage(driver)
        orders_and_returns_page.open()
        orders_and_returns_page.order_id_field().send_keys(order_id)
        orders_and_returns_page.billing_lastname_field().send_keys(random_last_name)
        orders_and_returns_page.email_field().send_keys(random_email)
        orders_and_returns_page.continue_button().click()
        assert orders_and_returns_page.text_order_number_on_check_page().text == f"Order # {order_id}"


    # ФУНКЦИЯ ВЕШАЕТ РАНДОМНЫЙ ОРДЕР И ПРОВЕРЯЕТ ЕГО В БАЗЕ ПО ИНДЕКСУ ПОЧТОВОМУ
    def test_check_order_by_zip(self, driver, random_email, random_first_name, random_last_name, random_ru_zip_code,
                                random_street, random_city, random_ru_phone_number):
        page = MainPage(driver)
        page.open()
        page.add_bolo_sport_watch_to_cart()
        checkout_page = GuestShippingAddressPage(driver)
        order_id = checkout_page.full_guest_place_order(email=random_email, firstname=random_first_name,
                                                        lastname=random_last_name,
                                                        street_1=random_street, city=random_city,
                                                        zip_code=random_ru_zip_code,
                                                        phone_number=random_ru_phone_number)
        orders_and_returns_page = OrdersAndReturnsPage(driver)
        orders_and_returns_page.open()
        orders_and_returns_page.select_find_order_by_zip_code_dropdown()
        orders_and_returns_page.order_id_field().send_keys(order_id)
        orders_and_returns_page.billing_lastname_field().send_keys(random_last_name)
        orders_and_returns_page.billing_zip_code_field().send_keys(random_ru_zip_code)
        orders_and_returns_page.continue_button().click()
        assert orders_and_returns_page.text_order_number_on_check_page().text == f"Order # {order_id}"


class TestFieldsNotFilled:
    def test_order_id_field_not_filled(self, driver, random_last_name, random_email):
        page = OrdersAndReturnsPage(driver)
        page.order_id_not_filled(random_last_name, random_email)
        page.continue_button().click()
        assert page.error_msg_order_id_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле order_id не заполнено , а ошибка не показана"

    def test_lastname_field_not_filled(self, driver, random_email, random_order_id):
        page = OrdersAndReturnsPage(driver)
        page.billing_last_name_not_filled(random_order_id, random_email)
        page.continue_button().click()
        assert page.error_msg_billing_lastname_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле billing lastname не заполнено , а ошибка не показана"

    def test_email_field_not_filled(self, driver, random_last_name, random_order_id):
        page = OrdersAndReturnsPage(driver)
        page.email_not_filled(random_order_id, random_last_name)
        page.continue_button().click()
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле email не заполнено , а ошибка не показана"

    def test_zip_field_not_filled(self, driver, random_last_name, random_order_id):
        page = OrdersAndReturnsPage(driver)
        page.zip_code_not_filled(random_order_id, random_last_name)
        page.continue_button().click()
        assert page.error_msg_billing_zip_code_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле zipcode не заполнено , а ошибка не показана"

    def test_email_filled_incorrect_email_type(self, driver, random_last_name, random_order_id):
        page = OrdersAndReturnsPage(driver)
        page.fill_incorrect_email_to_email_field(random_order_id, random_last_name)
        page.continue_button().click()
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_EMAIL_TYPE, "Не появилась ошибка про неправильный email"


class TestSwitchFindOrderBy:

    def test_switch_to_zip(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.select_find_order_by_zip_code_dropdown()
        assert page.name_billing_zip_code_field().text == OrdersAndReturnsPageLocators.TEXT_NAME_ZIP_CODE_FIELD, 'не произошло переключение поиска заказа с Email на ZIP'

    def test_switch_to_email(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.select_find_order_by_zip_code_dropdown()
        assert page.name_billing_zip_code_field().text == OrdersAndReturnsPageLocators.TEXT_NAME_ZIP_CODE_FIELD, 'не произошло переключение поиска заказа с Email на ZIP'
        page.select_find_order_by_email_dropdown()
        assert page.name_email_field().text == OrdersAndReturnsPageLocators.TEXT_NAME_EMAIL_FIELD, 'не произошло переключение поиска заказа с ZIP на Email'
