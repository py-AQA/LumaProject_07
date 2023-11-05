from random import choice
from time import sleep

import pytest

from data.fake_data import FakeData
from pages.abstract import Page
from pages.account import AccountPage
from pages.anon_shipping import AnonShippigAddressAddPage
from pages.create_account import CreateAccountPage
from pages.account_edit import AccountEditPage
from pages.home import HomePage
from pages.logout import LogoutPage
from pages.sign_in import SignInPage
from pages.add_to_cart_mok import ItemDetailsPage


class TestNow(FakeData):

    @pytest.mark.xfail
    def test_anon_add_shipping_address_with_select_state(self, driver):
        LogoutPage(driver)

        page = ItemDetailsPage(driver)
        page.add_to_cart().click()
        assert page.msg == ItemDetailsPage.SUCCESS

        page = AnonShippigAddressAddPage(driver)
        page.email = self.email
        page.first_name = self.first_name

        page.last_name = self.last_name

        page.company = self.company

        page.country = choice(AnonShippigAddressAddPage.WITH_REGIONS)
        page.state = (state := choice(page.state[1:]))
        page.city = (city := self.city)
        page.postcode = (postcode := self.postcode)
        page.street_1 = self.secondary_address
        page.street_2 = self.street_address
        page.street_3 = f"{city} {state} {postcode}"
        page.telephone = self.phone_number

        sleep(5)
        page.button_next().click()
        # assert page.msg == AnonShippigAddressAddPage.SUCCESS
        # assert page.url == AnonShippigAddressAddPage.URL_DONE
        sleep(20)

    def test_anon_add_shipping_address_with_input_state(self, driver):
        pass
