from pages.main_page import MainPage
from pages.login_page import LoginPage
from time import sleep
import pytest


@pytest.mark.xfail
def test_my_account(driver):
    page = LoginPage(driver)
    page.sign_in(page)
    page = MainPage(driver)
    page.open()
    page.dropdown().click()
    page.link_my_account().click()
    assert page.current_url == 'https://magento.softwaretestingboard.com/customer/account/'


@pytest.mark.xfail
def test_my_wish(driver):
    page = LoginPage(driver)
    page.sign_in(page)
    page = MainPage(driver)
    page.open()
    sleep(30)
    page.dropdown().click()
    page.link_my_wish().click()
    assert page.current_url == 'https://magento.softwaretestingboard.com/wishlist/'


@pytest.mark.xfail
def test_sign_out(driver):
    page = LoginPage(driver)
    # page.open()
    # page.email().send_keys('sve3363@gmail.com')
    # page.password().send_keys('Zaqxsw100')
    # page.button_sign_in().click()
    # assert page.header().text == 'My Account'
    page.sign_in(page)
    page = MainPage(driver)
    page.open()
    page.dropdown().click()
    page.link_sign_out().click()
    assert page.driver.current_url == 'https://magento.softwaretestingboard.com/customer/account/logoutSuccess/'
