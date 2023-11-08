from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def __init__(self, driver, url=LoginPageLocators.URL, open=True):
        super().__init__(driver, url, open)

    def email(self) -> WebElement:
        return self.is_visible(LoginPageLocators.EMAIL)

    def password(self) -> WebElement:
        return self.is_visible(LoginPageLocators.PASSWORD)

    def button_sign_in(self) -> WebElement:
        return self.is_clickable(LoginPageLocators.BUTTON_SIGN_IN)

    def button_forgot_password(self) -> WebElement:
        return self.is_clickable(LoginPageLocators.BUTTON_FORGOT_PASSWORD)

    # ДАНЯ ДОБАВИЛ

    def create_an_account_button(self) -> WebElement:
        return self.is_clickable(LoginPageLocators.CREATE_AN_ACCOUNT_BUTTON)

    # # нет такого мессаджа ?
    # def success_signin_msg(self) -> WebElement:
    #     return self.is_visible(BasePageLocators.MSG_SUCCESS)

    def error_signin_msg(self):
        return self.is_visible(BasePageLocators.MSG_ERROR)

    def login_with_email_password(self, email, password):
        self.email().send_keys(email)
        self.password().send_keys(password)
        self.button_sign_in().click()

    # ДАНЯ ДОБАВИЛ КОНЕЦ

    def sign_in(self):
        self.email().send_keys('sve3363@gmail.com')
        self.password().send_keys('Zaqxsw100')
        self.button_sign_in().click()
        assert self.header().text == 'My Account', "Не удалось войти"
