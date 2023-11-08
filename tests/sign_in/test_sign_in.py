import pytest

from data.fake_data import FakeData
from data.locators import MyAccountPageLocators, LoginPageLocators
from pages.create_account import CreateAccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


# @pytest.mark.skip
# def test_sign_in(driver):
#     page = LoginPage(driver, url='https://magento.softwaretestingboard.com/customer/account/login')
#     page.sign_in()
#     assert page.header().text == 'My Account'


# ДОБАВИЛ ДАНЯ
class TestSignIn(FakeData):

    def test_good_email_password(self, driver):
        email = self.email
        password = self.password
        CreateAccountPage(driver).create(self.first_name, self.last_name, email, password)
        MainPage(driver, open_url=False).dropdown().click()
        MainPage(driver, open_url=False).link_sign_out().click()
        page = LoginPage(driver)
        page.login_with_email_password(email, password)
        assert page.header().text == 'My Account', "Не удалось войти в существующий аккаунт "
        assert page.current_url == MyAccountPageLocators.URL, "Не удалось залогиниться в существующий аккаунт "

    def test_bad_password(self, driver):
        email = self.email
        password = self.password
        CreateAccountPage(driver).create(self.first_name, self.last_name, email, password)
        MainPage(driver, open_url=False).dropdown().click()
        MainPage(driver, open_url=False).link_sign_out().click()
        page = LoginPage(driver)
        page.login_with_email_password(email, self.password)
        assert page.current_url == LoginPageLocators.URL, "удалось залогиниться с неправильным паролем"
        assert page.error_signin_msg().text == LoginPageLocators.TEXT_ERROR_MSG_LOGIN, "неправильное сообщение об ошибке при попытке логина с неправильным паролем"

    def test_bad_email_password(self, driver):
        page = LoginPage(driver)
        page.login_with_email_password(self.email, self.password)
        assert page.current_url == LoginPageLocators.URL, "удалось залогиниться с неправильным паролем"
        assert page.error_signin_msg().text == LoginPageLocators.TEXT_ERROR_MSG_LOGIN, "неправильное сообщение об ошибке при попытке логина с неправильным паролем"

    # ДОБАВИЛ ДАНЯ КОНЕЦ

    def test_header(self, driver):
        page = LoginPage(driver)
        assert page.header().text == 'Customer Login'
