from base.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from data.locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def __init__(self, driver, url=RegistrationPageLocators.URL, open_url=True):
        super().__init__(driver, url, open_url)

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

    def create_account(self, random_first_name, random_last_name, random_email, random_password):
        # todo sometimes fails with 'NoneType' object has no attribute 'send_keys' for
        #  page.first_name().send_keys(random_first_name)
        self.first_name().send_keys(random_first_name)
        self.last_name().send_keys(random_last_name)
        self.email().send_keys(random_email)
        self.password().send_keys(random_password)
        self.confirm_password().send_keys(random_password)
        self.button_create_account().click()
        assert self.success_message() == 'Thank you for registering with Main Website Store.', 'Не удалось создать.'
