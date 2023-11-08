import time
from pages.registration_page import RegistrationPage


def test_header(driver):
    page = RegistrationPage(driver, 'https://magento.softwaretestingboard.com/customer/account/create/')
    # page.open()
    assert page.header().text == 'Create New Customer Account'


def test_first_name(driver, random_first_name):
    page = RegistrationPage(driver, 'https://magento.softwaretestingboard.com/customer/account/create/')
    # page.open()
    page.first_name().send_keys(random_first_name)
    time.sleep(2)
    # driver()


def test_last_name(driver, random_last_name):
    page = RegistrationPage(driver, 'https://magento.softwaretestingboard.com/customer/account/create/')
    # page.open()
    page.last_name().send_keys(random_last_name)
    time.sleep(2)


def test_email(driver, random_email):
    page = RegistrationPage(driver, 'https://magento.softwaretestingboard.com/customer/account/create/')
    # page.open()
    page.email().send_keys(random_email)
    time.sleep(2)


def test_password(driver, random_password):
    page = RegistrationPage(driver, 'https://magento.softwaretestingboard.com/customer/account/create/')
    # page.open()
    page.password().send_keys(random_password)
    time.sleep(2)


def test_registration(driver, random_first_name, random_last_name, random_email, random_password):
    page = RegistrationPage(driver, 'https://magento.softwaretestingboard.com/customer/account/create/')
    # page.open()
    page.first_name().send_keys(random_first_name)
    page.last_name().send_keys(random_last_name)
    page.email().send_keys(random_email)
    page.password().send_keys(random_password)
    page.confirm_password().send_keys(random_password)
    page.button_create_account().click()
    # time.sleep(10)
    assert page.success_message() == 'Thank you for registering with Main Website Store.'
    # assert page.is_visible(By.CSS_SELECTOR,
    # "[data-ui-id='message-success'] div").text == 'Thank you for registering with Main Website Store.'
