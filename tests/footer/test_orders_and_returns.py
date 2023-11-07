from data.fake_data import FakeData
from data.locators import OrdersAndReturnsPageLocators
from pages.checkout_page import CheckoutPage
from pages.create_account import CreateAccountPage
from pages.main_page import MainPage
from pages.orders_and_returns_page import OrdersAndReturnsPage


# ВОЗМОЖНО НУЖНО УСОВЕРШЕНСТВОВАТЬ
class TestCheckGuestOrder(FakeData):
    # ФУНКЦИЯ ВЕШАЕТ РАНДОМНЫЙ ОРДЕР И ПРОВЕРЯЕТ ЕГО В БАЗЕ ПО ЕМЕЙЛУ
    def test_check_order_by_email(self, driver):
        email = self.email
        last_name = self.last_name
        state = self.state
        page = MainPage(driver)
        page.open()
        page.add_item_from_gear_watches_catalog_to_cart(6)
        checkout_page = CheckoutPage(driver)
        order_id = checkout_page.full_guest_place_order_us_address(state,email, self.first_name,
                                                           last_name,self.street_address, self.city,
                                                           self.us_postcode_state(state),
                                                           self.phone_number)
        orders_and_returns_page = OrdersAndReturnsPage(driver)
        orders_and_returns_page.find_order_by_email(order_id,last_name,email)
        assert orders_and_returns_page.text_order_number_on_check_page().text == f"Order # {order_id}"

    # ФУНКЦИЯ ВЕШАЕТ РАНДОМНЫЙ ОРДЕР И ПРОВЕРЯЕТ ЕГО В БАЗЕ ПО ИНДЕКСУ ПОЧТОВОМУ
    def test_check_order_by_zip(self, driver):
        last_name = self.last_name
        state = self.state
        postcode = self.us_postcode_state(state)
        page = MainPage(driver)
        page.open()
        page.add_item_from_gear_bags_catalog_to_cart(6)
        checkout_page = CheckoutPage(driver)
        order_id = checkout_page.full_guest_place_order_us_address(state, self.email, self.first_name,
                                                           last_name, self.street_address, self.city,
                                                           postcode,
                                                           self.phone_number)
        orders_and_returns_page = OrdersAndReturnsPage(driver)
        orders_and_returns_page.fill_all_field_with_postcode(order_id,last_name,postcode)
        orders_and_returns_page.continue_button().click()
        assert orders_and_returns_page.text_order_number_on_check_page().text == f"Order # {order_id}"

class TestCheckUserOrder(FakeData):
    # ФУНКЦИЯ ВЕШАЕТ РАНДОМНЫЙ ОРДЕР И ПРОВЕРЯЕТ ЕГО В БАЗЕ ПО ЕМЕЙЛУ
    def test_check_order_by_email(self, driver):
        email = self.email
        last_name = self.last_name
        state = self.state
        page = CreateAccountPage(driver)
        page.create(self.first_name,last_name,email,self.password)
        MainPage(driver).add_item_from_gear_watches_catalog_to_cart(4)
        checkout_page = CheckoutPage(driver)
        order_id = checkout_page.full_user_place_order_flat_rate(state,self.street_address, self.city,
                                                           self.us_postcode_state(state),
                                                           self.phone_number)
        print(order_id)
        MainPage(driver).dropdown().click()
        MainPage(driver).link_sign_out().click()
        orders_and_returns_page = OrdersAndReturnsPage(driver)
        orders_and_returns_page.find_order_by_email(order_id,last_name,email)
        assert orders_and_returns_page.text_order_number_on_check_page().text == f"Order # {order_id}"

    # ФУНКЦИЯ ВЕШАЕТ РАНДОМНЫЙ ОРДЕР И ПРОВЕРЯЕТ ЕГО В БАЗЕ ПО ИНДЕКСУ ПОЧТОВОМУ
    def test_check_order_by_zip(self, driver):
        last_name = self.last_name
        state = self.state
        postcode = self.us_postcode_state(state)
        page = MainPage(driver)
        page.open()
        page.add_item_from_gear_bags_catalog_to_cart(6)
        checkout_page = CheckoutPage(driver)
        order_id = checkout_page.full_guest_place_order_us_address(state, self.email, self.first_name,
                                                           last_name, self.street_address, self.city,
                                                           postcode,
                                                           self.phone_number)
        orders_and_returns_page = OrdersAndReturnsPage(driver)
        orders_and_returns_page.fill_all_field_with_postcode(order_id,last_name,postcode)
        orders_and_returns_page.continue_button().click()
        assert orders_and_returns_page.text_order_number_on_check_page().text == f"Order # {order_id}"


class TestFieldsNotFilled(FakeData):
    def test_order_id_field_not_filled(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.order_id_not_filled(self.last_name, self.email)
        page.continue_button().click()
        assert page.error_msg_order_id_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле order_id не заполнено , а ошибка не показана"

    def test_lastname_field_not_filled(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.billing_last_name_not_filled(self.order_id, self.email)
        page.continue_button().click()
        assert page.error_msg_billing_lastname_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле billing lastname не заполнено , а ошибка не показана"

    def test_email_field_not_filled(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.email_not_filled(self.order_id, self.last_name)
        page.continue_button().click()
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле email не заполнено , а ошибка не показана"

    def test_zip_field_not_filled(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.postcode_not_filled(self.order_id, self.last_name)
        page.continue_button().click()
        assert page.error_msg_billing_postcode_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле zipcode не заполнено , а ошибка не показана"

    def test_email_filled_incorrect_email_type(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.fill_incorrect_email_to_email_field(self.order_id, self.last_name)
        page.continue_button().click()
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_EMAIL_TYPE, "Не появилась ошибка про неправильный email"


class TestSwitchFindOrderBy:

    def test_switch_to_zip(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.select_find_order_by_postcode_dropdown()
        assert page.name_billing_postcode_field().text == OrdersAndReturnsPageLocators.TEXT_NAME_POSTCODE_FIELD, 'не произошло переключение поиска заказа с Email на ZIP'

    def test_switch_to_email(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.select_find_order_by_postcode_dropdown()
        assert page.name_billing_postcode_field().text == OrdersAndReturnsPageLocators.TEXT_NAME_POSTCODE_FIELD, 'не произошло переключение поиска заказа с Email на ZIP'
        page.select_find_order_by_email_dropdown()
        assert page.name_email_field().text == OrdersAndReturnsPageLocators.TEXT_NAME_EMAIL_FIELD, 'не произошло переключение поиска заказа с ZIP на Email'
