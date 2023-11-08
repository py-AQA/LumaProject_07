from time import sleep
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from data.locators import BasePageLocators
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    URL = "about:blank"
    TIMEOUT = 10
    LOADER = (By.CSS_SELECTOR, "div.loader")

    def __init__(self, driver, url=URL):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.delete_cookie("mage-messages")
        self.driver.get(self.url)

    def header(self) -> WebElement:
        return self.is_visible(BasePageLocators.HEADER)

    def is_visible(self, locator: (str, str), timeout: int = TIMEOUT) -> WebElement:
        try:
            return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"{timeout}s wait to be visible of {locator}")

    def is_clickable(self, locator: tuple[str, str], timeout: int = TIMEOUT) -> WebElement:
        try:
            return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"{timeout}s wait to be clickable of {locator}")

    @property
    def current_url(self):
        return self.driver.current_url

    @current_url.setter
    def current_url(self, val) -> None:
        self.driver.delete_cookie("mage-messages")
        self.driver.get(val)

    def clear_and_send_keys(self, el: WebElement, val: str) -> None:
        el.clear()
        el.send_keys(val)

    # ДАНЯ ДОБАВИЛ
    def hold_mouse_on_element(self, locator):
        ActionChains(self.driver).move_to_element(self.is_visible(locator)).perform()

    # ДАНЯ ДОБАВИЛ КОНЕЦ

    def window_size(self) -> dict:
        return self.driver.get_window_size()

    def is_invisible(self, locator: (str, str), timeout: int = TIMEOUT) -> WebElement:
        try:
            return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"{timeout}s wait to be invisible of {locator}")

    def is_all_present(self, locator: tuple[str, str], timeout: int = TIMEOUT) -> list[WebElement]:
        try:
            return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"{timeout}s wait all to be present of {locator}")

    def is_present(self, locator: tuple[str, str], timeout: int = TIMEOUT) -> bool:
        try:
            wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_loading(self):
        while self.is_present(self.LOADER, 0.1):
            print(f'loader {self.LOADER} is present: waiting to dissapear .... ')
            self.is_invisible(self.LOADER)
        else:
            print(f'loader {self.LOADER} is NOT present: gtg .... ')
