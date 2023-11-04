from time import sleep

from pages.home import HomePage
from pages.logout import LogoutPage
from pages.sign_in import SignInPage
from pages.create_account import CreateAccountPage

from fake_data import TestDriver


class TestNow(TestDriver):
    def test_sign_in_link(self):
        # todo узнать какую страницу сайта выбрать для проверки
        page = HomePage(self.driver)
        page.sign_in.click()
        assert page.url.startswith(SignInPage.URL)

    def test_create_account_link(self):
        # todo узнать какую страницу сайта выбрать для проверки
        page = HomePage(self.driver)
        page.create_account.click()
        assert page.url == CreateAccountPage.URL

    def test_logo_link(self):
        # todo узнать какую страницу сайта выбрать для клика по логотипу для проверки
        # go to any page of the site
        page = HomePage(self.driver, "https://magento.softwaretestingboard.com/customer/account/create/")
        page.logo.click()
        assert page.url == HomePage.URL

