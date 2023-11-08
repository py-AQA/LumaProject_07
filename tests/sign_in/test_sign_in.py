import pytest

from pages.login_page import LoginPage


def test_header(driver):
    page = LoginPage(driver, url='https://magento.softwaretestingboard.com/customer/account/login')
    page.open()
    assert page.header().text == 'Customer Login'

@pytest.mark.skip
def test_sign_in(driver):
    page = LoginPage(driver, url='https://magento.softwaretestingboard.com/customer/account/login')
    page.sign_in()
    assert page.header().text == 'My Account'



