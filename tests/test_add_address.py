from time import sleep
from random import choice
from data.fake_data import FakeData
from pages.account import AccountPage
from pages.account_add_address import AddressAddPage
from pages.create_account import CreateAccountPage
from pages.account_edit import AccountEditPage
from pages.logout import LogoutPage
from pages.sign_in import SignInPage


class TestNow(FakeData):
    def test_add_address_with_select_state(self, driver, first_name, last_name, email, password):
        LogoutPage(driver)
        CreateAccountPage(driver).create(first_name, last_name, email, password)
        page = AddressAddPage(driver)
        page.company = self.company
        page.telephone = self.phone_number

        page.country = choice(AddressAddPage.WITH_REGIONS)
        page.state = (state := choice(page.state[1:]))
        page.city = (city := self.city)
        page.postcode = (postcode := self.postcode)
        page.street_1 = self.secondary_address
        page.street_2 = self.street_address
        page.street_3 = f"{city} {state} {postcode}"

        # page.set_billing.click()
        page.save().click()
        assert page.msg == AddressAddPage.SUCCESS
        assert page.url == AddressAddPage.URL_DONE

    def test_add_address_with_input_state(self, driver, first_name, last_name, email, password):
        LogoutPage(driver)
        CreateAccountPage(driver).create(first_name, last_name, email, password)
        page = AddressAddPage(driver)
        page.company = self.company
        page.telephone = self.phone_number

        page.country = choice(list(filter(lambda x: x not in AddressAddPage.WITH_REGIONS, page.country)))

        city = self.city
        state = self.state
        postcode = self.postcode
        page.street_1 = self.secondary_address
        page.street_2 = self.street_address
        page.street_3 = f"{city} {state} {postcode}"
        page.city = city
        page.postcode = postcode
        page.region = state

        # page.set_shpping.click()

        page.save().click()
        assert page.msg == AddressAddPage.SUCCESS
        assert page.url == AddressAddPage.URL_DONE
