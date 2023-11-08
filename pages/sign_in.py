from selenium.webdriver.common.by import By
from pages.abstract import Page
from urllib import parse
from base64 import b64decode


class SignInPage(Page):
    URL = "https://magento.softwaretestingboard.com/customer/account/login/"
    EMAIL = (By.CSS_SELECTOR, "input#email")
    PASSWORD = (By.CSS_SELECTOR, "input#pass")
    SIGN_IN = (By.CSS_SELECTOR, "button.action.login.primary")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a.action.remind")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "a.action.create.primary")

    MSG = (By.CSS_SELECTOR, '[data-ui-id="message-error"]')
    FAIL = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        # self.current_url = url

        # self.referer = parse.unquote(url.split('referer/')[1])
        # print(b64decode(self.referer))

    @property
    def email(self):
        return self.is_visible(self.EMAIL)

    @email.setter
    def email(self, val: str):
        self.clear_and_send_keys(self.email, val)

    @property
    def password_one(self):
        return self.is_visible(self.PASSWORD)

    @password_one.setter
    def password_one(self,  val: str) -> None:
        self.clear_and_send_keys(self.password_one, val)

    def sign_in(self):
        return self.is_visible(self.SIGN_IN)

    def forgot_password(self):
        return self.is_visible(self.FORGOT_PASSWORD)

    def create_account(self):
        return self.is_visible(self.CREATE_ACCOUNT)
