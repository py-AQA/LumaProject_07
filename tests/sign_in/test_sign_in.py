from pages.login_page import LoginPage


def test_header(driver):
    page = LoginPage(driver, url='https://magento.softwaretestingboard.com/customer/account/login')
    page.open()
    assert page.header().text == 'Customer Login'


def test_sign_in(driver):
    page = LoginPage(driver, url='https://magento.softwaretestingboard.com/customer/account/login')
    page.open()
    page.email().send_keys('sve3363@gmail.com')
    page.password().send_keys('Zaqxsw100')
    page.button_sign_in().click()
    assert page.header().text == 'My Account'



