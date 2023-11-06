from selenium.webdriver.common.by import By
from pages.abstract import Page
from pages.account import AccountPage


class CreateAccountPage(Page):
    URL = "https://magento.softwaretestingboard.com/customer/account/create/"

    FIRST_NAME = (By.CSS_SELECTOR, "input#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "input#lastname")
    EMAIL = (By.CSS_SELECTOR, "input#email_address")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#password-confirmation")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "button.action.submit.primary")

    SUCCESS = "Thank you for registering with Main Website Store."

    def __init__(self, driver, url=URL):
        super().__init__(driver)
        # переходим к указанной или URL странице
        # print('>>>>>>>>>>>>>', url)
        self.current_url = url

    @property
    def first_name(self):
        return self.is_visible(self.FIRST_NAME)

    @first_name.setter
    def first_name(self, val: str):
        self.clear_and_send_keys(self.first_name, val)

    @property
    def last_name(self):
        return self.is_visible(self.LAST_NAME)

    @last_name.setter
    def last_name(self, val: str):
        self.clear_and_send_keys(self.last_name, val)

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
    def password_one(self,  val: str):
        self.clear_and_send_keys(self.password_one, val)

    @property
    def password_two(self):
        return self.is_visible(self.PASSWORD_CONFIRM)

    @password_two.setter
    def password_two(self,  val: str):
        self.clear_and_send_keys(self.password_two, val)

    def create_account(self):
        return self.is_visible(self.CREATE_ACCOUNT)

    def create(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_one = password
        self.password_two = password
        self.create_account().click()
        assert self.myurl == AccountPage.URL
        # return AccountPage(self.driver)
