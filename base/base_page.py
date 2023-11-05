from time import sleep
from selenium.common import TimeoutException
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

    def is_visible(self, locator: (str, str), timeout: int = 15) -> WebElement:
        try:
            return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Timeout: Element located by {locator} not visible after {timeout}s")

    def is_clickable(self, locator: tuple[str, str], timeout: int = 15) -> WebElement:
        try:
            return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Timeout: Element located by {locator} not clickable after {timeout}s")

    @property
    def current_url(self):
        return self.driver.current_url

    def clear_and_send_keys(self, el: WebElement, val: str) -> None:
        el.clear()
        el.send_keys(val)