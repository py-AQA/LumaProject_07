from pages.password_reset import ResetPage
from data.locators import ResetPageLocators


def test_password_reset(driver):
    page = ResetPage(driver, url='https://magento.softwaretestingboard.com/customer/account/login')
    page.open()
    page.button_forgot_password().click()
    page.email().send_keys('sve3363@gmail.com')
    page.button_reset_password().click()
    assert page.success_message() == ('If there is an account associated with sve3363@gmail.com you'
                                      ' will receive an email with a link to reset your password.')


def test_password_reset_not_valid_email(driver):
    page = ResetPage(driver, url=ResetPageLocators.FORGOT_PASS_URL)
    page.open()
    page.email().send_keys('@gmail.com')
    page.button_reset_password().click()
    assert page.error_message() == 'Please enter a valid email address (Ex: johndoe@domain.com).'
