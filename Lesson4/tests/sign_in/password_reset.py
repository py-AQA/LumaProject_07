from Lesson4.pages.login_page import LoginPage
from Lesson4.pages.password_reset import ResetPage
from Lesson4.conftest import driver, options


def test_password_reset(driver):
    page = ResetPage(driver, url='https://magento.softwaretestingboard.com/customer/account/login')
    page.open()
    page.button_forgot_password().click()
    page.email().send_keys('sve3363@gmail.com')
    page.button_reset_password().click()
    assert page.success_message() == ('If there is an account associated with sve3363@gmail.com you'
                                      ' will receive an email with a link to reset your password.')



