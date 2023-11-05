from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver, url=LoginPageLocators.URL):
        super().__init__(driver, url)

    def email(self) -> WebElement:
        return self.is_visible(LoginPageLocators.EMAIL)

    def password(self) -> WebElement:
        return self.is_visible(LoginPageLocators.PASSWORD)

    def button_sign_in(self) -> WebElement:
        return self.is_clickable(LoginPageLocators.BUTTON_SIGN_IN)

    def button_forgot_password(self) -> WebElement:
        return self.is_clickable(LoginPageLocators.BUTTON_FORGOT_PASSWORD)

    def sign_in(self, page):
        page.open()
        page.email().send_keys('sve3363@gmail.com')
        page.password().send_keys('Zaqxsw100')
        page.button_sign_in().click()
        assert page.header().text == 'My Account', "Не удалось войти"
