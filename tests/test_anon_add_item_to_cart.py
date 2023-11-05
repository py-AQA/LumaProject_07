from time import sleep

from data.fake_data import FakeData
from pages.abstract import Page
from pages.account import AccountPage
from pages.add_to_cart_mok import ItemDetailsPage
from pages.create_account import CreateAccountPage
from pages.account_edit import AccountEditPage
from pages.home import HomePage
from pages.logout import LogoutPage
from pages.sign_in import SignInPage


class TestNow(FakeData):
    def test_add_available_item_to_cart(self, driver):
        page = ItemDetailsPage(driver)
        page.add_to_cart().click()
        assert page.msg == ItemDetailsPage.SUCCESS

    def test_add_unavailable_item_to_cart(self, driver):
        pass


    def test_add_available_item_to_cart_from_item_details(self, driver):
        pass

    def test_add_unavailable_item_to_cart_from_item_details(self, driver):
        pass


    def test_add_available_item_to_cart_from_item(self, driver):
        pass

    def test_add_unavailable_item_to_cart_from_item(self, driver):
        pass

