from random import randint

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
    #ДОБАВИЛ ДАНЯ
    LINK_CART = (By.XPATH, "//*[@class='minicart-wrapper']")
    CHECKOUT_BUTTON_LINK_CART = (By.XPATH,"//*[@id='top-cart-btn-checkout']")
    LINK_GEAR_CATALOG = (By.XPATH,"//*[@ID='ui-id-6']")
    LINK_WATCHES_CATALOG =(By.XPATH,"//*[@ID='ui-id-27']")
    ADD_TO_CART_BOLO_SPORT_WATCH_BUTTON = (By.XPATH, "(//div[@class='product details product-item-details']//button[@title='Add to Cart'])[3]")
    HOLD_LINK_BOLO_SPORT_WATCH = (By.XPATH,"(//div[@class='product details product-item-details'])[3]")
    URL_CART = "https://magento.softwaretestingboard.com/checkout/cart/"
    #ДАНЯ КОНЕЦ


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

    #ДОБАВИЛ ДАНЯ
    MY_ACCOUNT_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[1]")
    MY_ORDERS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[2]")
    MY_DOWNLOADABLE_PRODUCTS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[3]")
    MY_WISH_LIST_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[4]")
    ADDRESS_BOOK_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[6]")
    ACCOUNT_INFORMATION_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[7]")
    STORED_PAYMENT_METHODS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[8]")
    MY_PRODUCT_REVIEWS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[10]")
    #ВРЕМЕННО URLS
    URL_MY_ACCOUNT = "https://magento.softwaretestingboard.com/customer/account/"
    URL_MY_ORDERS = "https://magento.softwaretestingboard.com/sales/order/history/"
    URL_MY_DOWNLOADABLE_PRODUCTS = "https://magento.softwaretestingboard.com/downloadable/customer/products/"
    URL_MY_WISH_LIST = "https://magento.softwaretestingboard.com/wishlist/"
    URL_ADDRESS_BOOK = "https://magento.softwaretestingboard.com/customer/address/"
    URL_NEW_ADDRESS_BOOK = "https://magento.softwaretestingboard.com/customer/address/new/"
    URL_ACCOUNT_INFORMATION = "https://magento.softwaretestingboard.com/customer/account/edit/"
    URL_STORED_PAYMENT_METHODS = "https://magento.softwaretestingboard.com/vault/cards/listaction/"
    URL_MY_PRODUCT_REVIEW = "https://magento.softwaretestingboard.com/review/customer/"
    #ДОБАВИЛ ДАНЯ КОНЕЦ


class CreateAccountFormLocators:
    # FIRST_NAME_LABEL = (By.CSS_SELECTOR, ".field-name-firstname")
    FIRST_NAME_LABEL = (By.CSS_SELECTOR, "label[for='firstname']")
    LAST_NAME_LABEL = (By.CSS_SELECTOR, "label[for='lastname']")
    EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='email_address']")
    PASSWORD_LABEL = (By.CSS_SELECTOR, "label[for='password']")
    CONFIRM_PASSWORD_LABEL = (By.CSS_SELECTOR, "label[for='password-confirmation']")


class ResetPageLocators:
    URL = 'https://magento.softwaretestingboard.com/customer/account/login'
    FORGOT_PASS_URL = 'https://magento.softwaretestingboard.com/customer/account/forgotpassword/'
    LONG_EMAIL = 'longgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg@ya.ru'
    EMAIL = (By.CSS_SELECTOR, 'input#email_address')
    BUTTON_RESET_PASSWORD = (By.CSS_SELECTOR, 'button.submit')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id=message-success] div")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#email_address-error")
    ERROR_ALERT = (By.CSS_SELECTOR, '[data-ui-id="message-error"]')


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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id='message-success']")
    ITEM_13740 = (By.CSS_SELECTOR, ".products-grid a[title='Breathe-Easy Tank']")


#ДОБАВИЛ ДАНЯ
class OrdersAndReturnsPageLocators:
    ORDER_ID_FIELD = (By.XPATH, "//*[@id='oar-order-id']")
    ORDER_ID_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar-order-id-error']")

    BILLING_LASTNAME_FIELD = (By.XPATH, "//*[@id='oar-billing-lastname']")
    BILLING_LASTNAME_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar-billing-lastname-error']")

    FIND_ORDER_BY_DROPDOWN = (By.XPATH,"//*[@id='quick-search-type-id']")
    FIND_ORDER_BY_EMAIL_DROPDOWN = (By.XPATH,"//option[@value='email']")
    FIND_ORDER_BY_ZIP_CODE_DROPDOWN = (By.XPATH, "//option[@value='zip']")

    EMAIL_FIELD = (By.XPATH,"//*[@id='oar_email']")
    EMAIL_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar_email-error']")
    NAME_EMAIL_FIELD = (By.XPATH,"//label[@for='oar_email']")

    ZIP_FIELD = (By.XPATH,"//*[@id='oar_zip']")
    ZIP_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar_zip-error']")
    NAME_ZIP_CODE_FIELD = (By.XPATH, "//label[@for='oar_zip']")

    CONTINUE_BUTTON = (By.XPATH, "//*[@title='Continue']")

    TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD = "This is a required field."
    TEXT_ERROR_MESSAGE_EMAIL_TYPE = "Please enter a valid email address (Ex: johndoe@domain.com)."
    TEXT_NAME_ZIP_CODE_FIELD = "Billing ZIP Code"
    TEXT_NAME_EMAIL_FIELD = "Email"

    ORDER_NUMBER_ON_CHECK_PAGE = (By.XPATH,"//span[@class='base']")


class GuestShippingAddressPageLocators:

    EMAIL_FIELD = (By.XPATH, "//div[@class='field required']//*[@id='customer-email']")
    FIRST_NAME_FIELD = (By.XPATH , "//*[@name='firstname']")
    LAST_NAME_FIELD = (By.XPATH, "//*[@name='lastname']")
    STREET_1_FIELD = (By.XPATH, "//*[@name='street[0]']")
    CITY_FIELD = (By.XPATH, "//*[@name='city']")
    COUNTRY_FIELD_DROPDOWN = (By.XPATH, "//*[@name='country_id']")
    RUSSIA_COUNTRY_DROPDOWN = (By.XPATH, "//*[@data-title='Russia']")
    ZIP_CODE_FIELD = (By.XPATH, "//*[@name='postcode']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//*[@name='telephone']")

    SHIPPING_BEST_WAY = (By.XPATH, "//*[@id='label_carrier_bestway_tablerate']")
    SHIPPING_FLAT_RATE = (By.XPATH, "//*[@id='label_carrier_flatrate_flatrate']")

    ORDER_NUMBER = (By.XPATH, "//div[@class='checkout-success']/p/span")
    EMAIL_ORDER = (By.XPATH, "//*[@data-bind='text: getEmailAddress()']")

    CHECKOUT_STEP_2_NEXT_BUTTON = (By.XPATH, "//*[@class='button action continue primary']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@title='Place Order']")

    OVERLAY = (By.XPATH, "//*[@data-role='loader']")



class CartLocators:

    CART_PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//div[@class='cart-summary']//*[@title='Proceed to Checkout']")


#ДОБАВИЛ ДАНЯ КОНЕЦ

