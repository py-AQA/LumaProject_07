from selenium.webdriver.common.by import By
from pages.abstract import Page


class ForgotPage(Page):
    URL = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"
    URL_DONE = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw%2C%2C/"

    EMAIL = (By.CSS_SELECTOR, "input#email_address")
    RESET_PASSWORD = (By.CSS_SELECTOR, "button.action.submit.primary")

    SUCCESS = "If there is an account associated with %s you will receive an email with a link to reset your password."

    def __init__(self, driver, url=URL):
        super().__init__(driver)
        self.url = url

    @property
    def email(self):
        return self.is_visible(self.EMAIL)

    @email.setter
    def email(self, val: str):
        self.clear_and_send_keys(self.email, val)

    def reset_password(self):
        return self.is_visible(self.RESET_PASSWORD)

