from base.seleniumbase import BasePage
from selenium.webdriver.remote.webelement import WebElement
from locators.locators import RegistrationPageLocators




class RegistrationPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def first_name(self) -> WebElement:
        return self.is_visible(RegistrationPageLocators.FIRST_NAME)

    def last_name(self) -> WebElement:
        return self.is_visible(RegistrationPageLocators.LAST_NAME)

    def email(self) -> WebElement:
        return self.is_visible(RegistrationPageLocators.EMAIL)

    def password(self) -> WebElement:
        return self.is_visible(RegistrationPageLocators.PASSWORD)

    def confirm_password(self) -> WebElement:
        return self.is_visible(RegistrationPageLocators.CONFIRM_PASSWORD)

    def button_create_account(self) -> WebElement:
        return self.is_clickable(RegistrationPageLocators.BUTTON_CREATE_ACCOUNT)

    def success_message(self) -> str:
        return self.is_visible(RegistrationPageLocators.SUCCESS_MESSAGE).text

    def create_account(self, page, random_first_name, random_last_name, random_email, random_password):
        page.open()
        page.first_name().send_keys(random_first_name)
        page.last_name().send_keys(random_last_name)
        page.email().send_keys(random_email)
        page.password().send_keys(random_password)
        page.confirm_password().send_keys(random_password)
        page.button_create_account().click()
        assert page.success_message() == 'Thank you for registering with Main Website Store.', 'Не удалось создать.'
