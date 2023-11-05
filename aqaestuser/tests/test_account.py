from time import sleep

from pages.create_account import CreateAccountPage
from pages.home import HomePage
from pages.sign_in import SignInPage
from pages.logout import LogoutPage
from pages.account import AccountPage
from pages.forgot import ForgotPage

from fake_data import TestDriver, first_name, last_name, email, password


class TestNow(TestDriver):
    def test_create_account(self, first_name, last_name, email, password):
        page = CreateAccountPage(self.driver)
        page.first_name = first_name
        page.last_name = last_name
        page.email = email
        page.password_one = password
        page.password_two = password
        page.create_account().click()
        assert page.msg == CreateAccountPage.SUCCESS
        assert page.url == AccountPage.URL

    def test_correct_credentials_login(self, first_name, last_name, email, password):
        CreateAccountPage(self.driver).create(first_name, last_name, email, password)
        LogoutPage(self.driver)
        page = SignInPage(self.driver)
        page.email = email
        page.password_one = password
        page.sign_in().click()
        assert page.url == AccountPage.URL

    def test_bad_credentials_login(self, email, password):
        page = SignInPage(self.driver)
        page.email = email
        page.password_one = password
        page.sign_in().click()
        assert page.msg == SignInPage.FAIL
        assert page.url.startswith(SignInPage.URL)

    def test_logout(self, first_name, last_name, email, password):
        CreateAccountPage(self.driver).create(first_name, last_name, email, password)
        page = LogoutPage(self.driver, LogoutPage.URL)
        assert page.url == LogoutPage.URL_DONE
        sleep(6)
        assert page.url == HomePage.URL

    def test_reset_password(self, email):
        page = ForgotPage(self.driver)
        page.email = email
        page.reset_password().click()
        assert page.msg == ForgotPage.SUCCESS % email
        assert page.url == ForgotPage.URL_DONE
