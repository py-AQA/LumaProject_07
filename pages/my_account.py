from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import BasePage

EDIT_ACCOUNT = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/customer/account/edit/'])[1]")
FIRST_NAME = (By.CSS_SELECTOR, 'input#firstname')
LAST_NAME = (By.CSS_SELECTOR, 'input#lastname')
BUTTON_SAVE_ACCOUNT = (By.CSS_SELECTOR, 'button.save')
SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id='message-success'] div")
CONTACT_INFORMATION = (By.CSS_SELECTOR, '.box-information .box-content')
CHECK_BOX_EMAIL = (By.CSS_SELECTOR, '#change-email')
CHECK_BOX_PASSWORD = (By.CSS_SELECTOR, '#change-password')
EMAIL = (By.CSS_SELECTOR, 'input#email')
CURRENT_PASSWORD = (By.CSS_SELECTOR, '#current-password')
NEW_PASSWORD = (By.CSS_SELECTOR, '#password')
CONFIRM_NEW_PASSWORD = (By.CSS_SELECTOR, '#password-confirmation')


class MyAccountPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/customer/account/'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def edit_account(self) -> WebElement:
        return self.is_clickable(EDIT_ACCOUNT)

    def first_name(self) -> WebElement:
        return self.is_visible(FIRST_NAME)

    def last_name(self) -> WebElement:
        return self.is_visible(LAST_NAME)

    def button_save_account(self) -> WebElement:
        return self.is_clickable(BUTTON_SAVE_ACCOUNT)

    @property
    def success_message(self) -> str:
        return self.is_visible(SUCCESS_MESSAGE).text

    @property
    def contact_information(self) -> str:
        return self.is_visible(CONTACT_INFORMATION).text

    def check_box_email(self) -> WebElement:
        return self.is_clickable(CHECK_BOX_EMAIL)

    def email(self) -> WebElement:
        return self.is_visible(EMAIL)

    def current_password(self) -> WebElement:
        return self.is_visible(CURRENT_PASSWORD)

    def check_box_password(self):
        return self.is_clickable(CHECK_BOX_PASSWORD)

    def new_password(self) -> WebElement:
        return self.is_visible(NEW_PASSWORD)

    def confirm_new_password(self) -> WebElement:
        return self.is_visible(CONFIRM_NEW_PASSWORD)
