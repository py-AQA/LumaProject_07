from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER = (By.CSS_SELECTOR, 'h1 span')


class MainPageLocators:
    DROPDOWN = (By.CSS_SELECTOR, '.customer-name button.action.switch')
    LINK_MY_ACCOUNT = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/customer/account/'])[1]")
    LINK_MY_WISH = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/wishlist/'])[1]")
    LINK_SIGN_OUT = (By.XPATH, "(//*[@href='https://magento.softwaretestingboard.com/customer/account/logout/'])[1]")


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, 'input#email')
    PASSWORD = (By.CSS_SELECTOR, 'input#pass')
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, 'button.login')
    BUTTON_FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a.remind')

