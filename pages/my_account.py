from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import MyAccountPageLocators


class MyAccountPage(BasePage):
    def __init__(self, driver, url=MyAccountPageLocators.URL):
        super().__init__(driver, url)

    def edit_account(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.EDIT_ACCOUNT)

    def first_name(self) -> WebElement:
        return self.is_visible(MyAccountPageLocators.FIRST_NAME)

    def last_name(self) -> WebElement:
        return self.is_visible(MyAccountPageLocators.LAST_NAME)

    def button_save_account(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.BUTTON_SAVE_ACCOUNT)

    @property
    def success_message(self) -> str:
        return self.is_visible(MyAccountPageLocators.SUCCESS_MESSAGE).text

    @property
    def contact_information(self) -> str:
        return self.is_visible(MyAccountPageLocators.CONTACT_INFORMATION).text

    def check_box_email(self) -> WebElement:
        return self.is_clickable(MyAccountPageLocators.CHECK_BOX_EMAIL)

    def email(self) -> WebElement:
        return self.is_visible(MyAccountPageLocators.EMAIL)

    def current_password(self) -> WebElement:
        return self.is_visible(MyAccountPageLocators.CURRENT_PASSWORD)

    def check_box_password(self):
        return self.is_clickable(MyAccountPageLocators.CHECK_BOX_PASSWORD)

    def new_password(self) -> WebElement:
        return self.is_visible(MyAccountPageLocators.NEW_PASSWORD)

    def confirm_new_password(self) -> WebElement:
        return self.is_visible(MyAccountPageLocators.CONFIRM_NEW_PASSWORD)
