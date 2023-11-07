from time import sleep

from data.fake_data import FakeData
from pages.create_account import CreateAccountPage
from pages.home import HomePage
from pages.sign_in import SignInPage
from pages.logout import LogoutPage
from pages.account import AccountPage
from pages.forgot import ForgotPage


class TestNow(FakeData):
    def test_create_account(self, driver, first_name, last_name, email, password):
        page = CreateAccountPage(driver).create(first_name, last_name, email, password)
        # page.first_name = first_name
        # page.last_name = last_name
        # page.email = email
        # page.password_one = password
        # page.password_two = password
        # page.create_account().click()
        assert page.current_url == AccountPage.URL
        assert page.msg == CreateAccountPage.SUCCESS

    def test_create_second_account_with_same_email(self, driver, create_account, email):
        LogoutPage(driver)
        page = CreateAccountPage(driver)
        # .create(self.first_name, self.last_name, email, self.password)
        page.first_name = self.first_name
        page.last_name = self.last_name
        page.email = email
        page.password_one = (password := self.password)
        page.password_two = password
        page.create_account().click()
        assert page.current_url == CreateAccountPage.URL
        # todo add msg_fail
        # assert page.msg == CreateAccountPage.FAIL

    def test_correct_credentials_login(self, driver, create_account, email, password):
        LogoutPage(driver)
        page = SignInPage(driver)
        page.email = email
        page.password_one = password
        page.sign_in().click()
        assert page.current_url == AccountPage.URL

    def test_bad_credentials_login(self, driver, email, password):
        page = SignInPage(driver)
        page.email = email
        page.password_one = password
        page.sign_in().click()
        assert page.current_url.startswith(SignInPage.URL)
        assert page.msg == SignInPage.FAIL

    def test_logout(self, driver, create_account):
        page = LogoutPage(driver)
        assert page.current_url == LogoutPage.URL_DONE
        sleep(6)
        assert page.current_url == HomePage.URL

    def test_reset_password(self, driver, email):
        page = ForgotPage(driver)
        page.email = email
        page.reset_password().click()
        assert page.current_url == ForgotPage.URL_DONE
        assert page.msg == ForgotPage.SUCCESS % email
