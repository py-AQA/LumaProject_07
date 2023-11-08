from selenium.webdriver.common.by import By
from pages.abstract import Page
from selenium.webdriver.support.ui import Select


class AnonShippingAddressAddPage(Page):
    WITH_REGIONS = ["AU","BR","CA","CH","CN","CO","EE","ES","HR","IN","LT","LV","MX","PL","RO","US"]
    URL = "https://magento.softwaretestingboard.com/checkout/#shipping"
    URL_DONE = "https://magento.softwaretestingboard.com/checkout/#payment"

    EMAIL = (By.CSS_SELECTOR, "input#customer-email")

    FIRST_NAME = (By.CSS_SELECTOR, 'input[name="firstname"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="lastname"]')
    COMPANY = (By.CSS_SELECTOR, 'input[name="company"]')
    STREET_1 = (By.CSS_SELECTOR, 'input[name="street[0]"]')
    STREET_2 = (By.CSS_SELECTOR, 'input[name="street[1]"]')
    STREET_3 = (By.CSS_SELECTOR, 'input[name="street[2]"]')
    CITY = (By.CSS_SELECTOR, 'input[name="city"]')
    # STATE and REGION share same place
    # select STATE is for states with regions
    STATE = (By.CSS_SELECTOR, 'select[name="region_id"]')
    # input REGION if for states with regions
    REGION = (By.CSS_SELECTOR, 'input[name="region"]')
    ZIP = (By.CSS_SELECTOR, 'input[name="postcode"]')
    COUNTRY = (By.CSS_SELECTOR, 'select[name="country_id"]')
    PHONE = (By.CSS_SELECTOR, 'input[name="telephone"]')

    BUTTON_NEXT = (By.CSS_SELECTOR, "button.continue")

    LD_PAYMENT_METHOD = (By.CSS_SELECTOR, "li.checkout-payment-method")

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        # переходим к указанной или URL странице
        # self.current_url = url

    @property
    def email(self):
        return self.is_visible(self.EMAIL)

    @email.setter
    def email(self, val: str):
        self.clear_and_send_keys(self.email, val)

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
    def company(self):
        return self.is_visible(self.COMPANY)

    @company.setter
    def company(self, val: str):
        self.clear_and_send_keys(self.company, val)

    @property
    def telephone(self):
        return self.is_visible(self.PHONE)

    @telephone.setter
    def telephone(self, val: str):
        self.clear_and_send_keys(self.telephone, val)

    @property
    def street_1(self):
        return self.is_visible(self.STREET_1)

    @street_1.setter
    def street_1(self, val: str):
        self.clear_and_send_keys(self.street_1, val)

    @property
    def street_2(self):
        return self.is_visible(self.STREET_2)

    @street_2.setter
    def street_2(self, val: str):
        self.clear_and_send_keys(self.street_2, val)

    @property
    def street_3(self):
        return self.is_visible(self.STREET_3)

    @street_3.setter
    def street_3(self, val: str):
        self.clear_and_send_keys(self.street_3, val)

    @property
    def city(self):
        return self.is_visible(self.CITY)

    @city.setter
    def city(self, val: str):
        self.clear_and_send_keys(self.city, val)

    @property
    def region(self):
        return self.is_visible(self.REGION)

    @region.setter
    def region(self, val):
        self.clear_and_send_keys(self.region, val)

    @property
    def postcode(self):
        return self.is_visible(self.ZIP)

    @postcode.setter
    def postcode(self, val: str):
        self.clear_and_send_keys(self.postcode, val)

    @property
    def state(self):
        return [x.text for x in Select(self.is_clickable(self.STATE)).options]

    @state.setter
    def state(self, text):
        Select(self.is_clickable(self.STATE)).select_by_visible_text(text)

    @property
    def country(self):
        return [x.get_attribute('value') for x in Select(self.is_clickable(self.COUNTRY)).options]

    @country.setter
    def country(self, val):
        Select(self.is_clickable(self.COUNTRY)).select_by_value(val)

    def button_next(self):
        self.is_invisible(self.LD_PAYMENT_METHOD)
        return self.is_clickable(self.BUTTON_NEXT)
