from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from locators.locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def header(self) -> WebElement:
        return self.is_visible(BasePageLocators.HEADER)

    def is_visible(self, locator) -> WebElement:
        return wait(self.driver, timeout=15).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator) -> WebElement:
        return wait(self.driver, timeout=15).until(EC.element_to_be_clickable(locator))

    @property
    def current_url(self):
        return self.driver.current_url
