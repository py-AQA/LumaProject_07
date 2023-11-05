from conftest import *
from pages.login_page import LoginPage
from pages.my_account import MyAccountPage
from pages.registration_page import RegistrationPage


def test_edit_first_and_last_name(driver):
    page = LoginPage(driver)
    page.sign_in(page)
    page = MyAccountPage(driver)
    page.edit_account().click()
    assert page.current_url == 'https://magento.softwaretestingboard.com/customer/account/edit/'
    page.first_name().clear()
    page.first_name().send_keys('Lana')
    page.last_name().clear()
    page.last_name().send_keys('Hrav')
    page.button_save_account().click()
    assert page.current_url == 'https://magento.softwaretestingboard.com/customer/account/'
    assert page.success_message == 'You saved the account information.'
    assert 'Lana' in page.contact_information, "Имя не сохранилось"


def test_change_email(driver, random_first_name, random_last_name, random_email, random_password, random_new_email):
    page = RegistrationPage(driver)
    page.create_account(page, random_first_name, random_last_name, random_email, random_password)
    # page = LoginPage(driver)
    # page.sign_in(page)
    page = MyAccountPage(driver)
    page.edit_account().click()
    page.check_box_email().click()
    page.email().clear()
    page.email().send_keys(random_new_email)
    page.current_password().send_keys(random_password)
    page.button_save_account().click()
    assert page.success_message == 'You saved the account information.'
    # assert 'sve3363@gmail.com' in page.contact_information, "Email не сохранилось"


def test_change_password(driver, random_first_name, random_last_name, random_email, random_password, random_new_password):
    page = RegistrationPage(driver)
    page.create_account(page, random_first_name, random_last_name, random_email, random_password)
    # page = LoginPage(driver)
    # page.sign_in(page)
    page = MyAccountPage(driver)
    page.edit_account().click()
    page.check_box_password().click()
    page.current_password().send_keys(random_password)
    page.new_password().send_keys(random_new_password)
    page.confirm_new_password().send_keys(random_new_password)
    page.button_save_account().click()
    assert page.success_message == 'You saved the account information.'