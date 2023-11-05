from Lesson4.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

EMAIL = (By.CSS_SELECTOR, 'input#email_address')
BUTTON_RESET_PASSWORD = (By.CSS_SELECTOR, 'button.submit')
SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id=message-success] div")


class ResetPage(LoginPage):
    def email(self) -> WebElement:
        return self.is_visible(EMAIL)

    def button_reset_password(self) -> WebElement:
        return self.is_clickable(BUTTON_RESET_PASSWORD)

    def success_message(self) -> str:
        return self.is_visible(SUCCESS_MESSAGE).text

