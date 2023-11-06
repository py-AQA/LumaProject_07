from pages.login_page import LoginPage
from selenium.webdriver.remote.webelement import WebElement
from data.locators import ResetPageLocators


class ResetPage(LoginPage):
    def email(self) -> WebElement:
        return self.is_visible(ResetPageLocators.EMAIL)

    def button_reset_password(self) -> WebElement:
        return self.is_clickable(ResetPageLocators.BUTTON_RESET_PASSWORD)

    def success_message(self) -> str:
        return self.is_visible(ResetPageLocators.SUCCESS_MESSAGE).text

    def error_message(self) -> str:
        return self.is_visible(ResetPageLocators.ERROR_MESSAGE).text
