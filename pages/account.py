from selenium.webdriver.common.by import By
from pages.abstract import Page


class AccountPage(Page):
    URL = "https://magento.softwaretestingboard.com/customer/account/"

    FIRST_NAME = (By.CSS_SELECTOR, "input#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "input#lastname")
    EMAIL = (By.CSS_SELECTOR, "input#email_address")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#password-confirmation")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "button.action.submit.primary")

    def __init__(self, driver, url=URL):
        super().__init__(driver)
        # переходим к указанной или URL странице
        self.myurl = url

    @property
    def first_name(self):
        return self.is_visible(self.FIRST_NAME)
