from random import choice

from data.fake_data import FakeData
from pages.abstract import Page
from pages.account import AccountPage
from pages.anon_shipping import AnonShippigAddressAddPage
from pages.create_account import CreateAccountPage
from pages.account_edit import AccountEditPage
from pages.home import HomePage
from pages.logout import LogoutPage
from pages.sign_in import SignInPage


class TestNow(FakeData):
    def test_anon_add_shipping_address_with_select_state(self, driver):
        LogoutPage(driver)
        # CreateAccountPage(driver).create(first_name, last_name, email, password)
        page = AnonShippigAddressAddPage(driver)
        page.company = self.company
        page.telephone = self.phone_number

        page.country = choice(AnonShippigAddressAddPage.WITH_REGIONS)
        page.state = (state := choice(page.state[1:]))
        page.city = (city := self.city)
        page.postcode = (postcode := self.postcode)
        page.street_1 = self.secondary_address
        page.street_2 = self.street_address
        page.street_3 = f"{city} {state} {postcode}"

        # page.set_billing.click()
        page.save().click()
        assert page.msg == AnonShippigAddressAddPage.SUCCESS
        assert page.url == AnonShippigAddressAddPage.URL_DONE

    def test_anon_add_shipping_address_with_input_state(self, driver):
        pass
