from pages.main_page import MainPage
from pages.login_page import LoginPage
from time import sleep
import pytest

def test_my_account(driver, auth):
    page = MainPage(driver)
    page.open()
    page.dropdown().click()
    page.link_my_account().click()
    assert page.current_url == 'https://magento.softwaretestingboard.com/customer/account/'


def test_my_wish(driver, auth):
    page = MainPage(driver)
    page.open()
    # sleep(30)
    page.dropdown().click()
    page.link_my_wish().click()
    assert page.current_url == 'https://magento.softwaretestingboard.com/wishlist/'


def test_sign_out(driver, auth):
    page = MainPage(driver)
    page.open()
    page.dropdown().click()
    page.link_sign_out().click()
    assert page.current_url == 'https://magento.softwaretestingboard.com/customer/account/logoutSuccess/'
