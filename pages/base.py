import pytest
from selenium.common import TimeoutException

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from base.base_page import BasePage


class Base(BasePage):
    pass
    # driver: WebDriver = None

    # def __init__(self, driver):
    #     self.driver = driver
    #
    # @property
    # def myurl(self) -> str:
    #     return self.current_url()
    #
    # @myurl.setter
    # def myurl(self, val) -> None:
    #     self.driver.get(val)
    #
    # def window_size(self) -> dict:
    #     return self.driver.get_window_size()
    #
    # def is_visible(self, locator: (str, str), timeout: int = 15) -> WebElement:
    #     try:
    #         return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    #     except TimeoutException as e:
    #         print(f"Timeout: Element located by {locator} not visible after {timeout}s")
    #
    # def is_not_visible(self, locator: (str, str), timeout: int = 15) -> WebElement:
    #     try:
    #         return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    #     except TimeoutException as e:
    #         print(f"Timeout: Element located by {locator} still visible after {timeout}s")
    #
    # def is_clickable(self, locator: tuple[str, str], timeout: int = 15) -> WebElement:
    #     try:
    #         return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    #     except TimeoutException as e:
    #         print(f"Timeout: Element located by {locator} not clickable after {timeout}s")
    #
    # def are_present(self, locator: tuple[str, str], timeout: int = 15) -> list[WebElement]:
    #     try:
    #         return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    #     except TimeoutException as e:
    #         print(f"Timeout: Elements located by {locator} not present after {timeout}s")
    #
    # def current_url(self):
    #     return self.driver.current_url
    #
    # def clear_and_send_keys(self, el: WebElement, val: str) -> None:
    #     el.clear()
    #     el.send_keys(val)



