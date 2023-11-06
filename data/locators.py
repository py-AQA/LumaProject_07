from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER = (By.CSS_SELECTOR, 'h1 span')
    MSG_ERROR = (By.CSS_SELECTOR, '[data-ui-id="message-error"]')
    MSG_SUCCESS = (By.CSS_SELECTOR, '[data-ui-id="message-success"]')


class MainPageLocators:
    URL = 'https://magento.softwaretestingboard.com/'
    DROPDOWN = (By.CSS_SELECTOR, '.customer-name button.action.switch')
    LINK_MY_ACCOUNT = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/customer/account/'])[1]")
    LINK_MY_WISH = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/wishlist/'])[1]")
    LINK_SIGN_OUT = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/customer/account/logout/'])[1]")


class LoginPageLocators:
    URL = 'https://magento.softwaretestingboard.com/customer/account/login'
    EMAIL = (By.CSS_SELECTOR, 'input#email')
    PASSWORD = (By.CSS_SELECTOR, 'input#pass')
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, 'button.login')
    BUTTON_FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a.remind')


class MyAccountPageLocators:
    URL = 'https://magento.softwaretestingboard.com/customer/account/'
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


class ResetPageLocators:
    EMAIL = (By.CSS_SELECTOR, 'input#email_address')
    BUTTON_RESET_PASSWORD = (By.CSS_SELECTOR, 'button.submit')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id=message-success] div")


class RegistrationPageLocators:
    URL = 'https://magento.softwaretestingboard.com/customer/account/create/'
    FIRST_NAME = (By.CSS_SELECTOR, 'input#firstname')
    LAST_NAME = (By.CSS_SELECTOR, 'input#lastname')
    EMAIL = (By.CSS_SELECTOR, 'input#email_address')
    PASSWORD = (By.CSS_SELECTOR, 'input#password')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input#password-confirmation')
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, 'button.action.submit.primary')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id='message-success'] div")


class ItemPageLocators:
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, 'div.product-social-links .towishlist')


class WishListPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id='message-success'] div")
    ITEM_13740 = (By.CSS_SELECTOR, ".products-grid a[title='Breathe-Easy Tank']")

