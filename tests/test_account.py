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
        LogoutPage(driver)
        page = CreateAccountPage(driver)
        page.first_name = first_name
        page.last_name = last_name
        page.email = email
        page.password_one = password
        page.password_two = password
        page.create_account().click()
        assert page.msg == CreateAccountPage.SUCCESS
        assert page.myurl == AccountPage.URL

    def test_correct_credentials_login(self, driver, first_name, last_name, email, password):
        LogoutPage(driver)
        CreateAccountPage(driver).create(first_name, last_name, email, password)
        LogoutPage(driver)
        page = SignInPage(driver)
        page.email = email
        page.password_one = password
        page.sign_in().click()
        assert page.myurl == AccountPage.URL

    def test_bad_credentials_login(self, driver, email, password):
        LogoutPage(driver)
        page = SignInPage(driver)
        page.email = email
        page.password_one = password
        page.sign_in().click()
        assert page.msg == SignInPage.FAIL
        assert page.myurl.startswith(SignInPage.URL)

    def test_logout(self, driver, first_name, last_name, email, password):
        LogoutPage(driver)
        CreateAccountPage(driver).create(first_name, last_name, email, password)
        page = LogoutPage(driver, LogoutPage.URL)
        assert page.myurl == LogoutPage.URL_DONE
        sleep(6)
        assert page.myurl == HomePage.URL

    def test_reset_password(self, driver, email):
        LogoutPage(driver)
        page = ForgotPage(driver)
        page.email = email
        page.reset_password().click()
        assert page.msg == ForgotPage.SUCCESS % email
        assert page.myurl == ForgotPage.URL_DONE
