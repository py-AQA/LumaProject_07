from time import sleep

import pytest

from data.fake_data import FakeData
from pages.home import HomePage
from pages.logout import LogoutPage
from pages.sign_in import SignInPage
from pages.create_account import CreateAccountPage


class TestNow(FakeData):

    def test_sign_in_link(self, driver):
        # todo узнать какую страницу сайта выбрать для проверки
        page = HomePage(driver)
        page.sign_in.click()
        assert page.current_url.startswith(SignInPage.URL)

    def test_create_account_link(self, driver):
        # todo узнать какую страницу сайта выбрать для проверки
        # todo fails with assert page.url == CreateAccountPage.URL for .../account/create/ .../account/login/referer...
        page = HomePage(driver)
        sleep(5)
        page.create_account.click()
        sleep(5)
        assert page.current_url == CreateAccountPage.URL

    def test_logo_link(self, driver):
        # todo узнать какую страницу сайта выбрать для клика по логотипу для проверки
        # go to any page of the site
        page = HomePage(driver, "https://magento.softwaretestingboard.com/customer/account/create/")
        page.logo.click()
        assert page.current_url == HomePage.URL

