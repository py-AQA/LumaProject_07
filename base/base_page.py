from time import sleep
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from data.locators import BasePageLocators
# ДАНЯ ДОБАВИЛ
from selenium.webdriver.common.action_chains import ActionChains


# ДАНЯ ДОБАВИЛ КОНЕЦ


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def header(self) -> WebElement:
        return self.is_visible(BasePageLocators.HEADER)

    def is_visible(self, locator: (str, str), timeout: int = 10) -> WebElement:
        try:
            return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Timeout: Element located by {locator} not visible after {timeout}s")

    def is_clickable(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
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

    # ДАНЯ ДОБАВИЛ
    def hold_mouse_on_element(self, locator):
        element_to_hover_over = wait(self.driver, timeout=15).until(EC.visibility_of_element_located(locator))
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
    # ДАНЯ ДОБАВИЛ КОНЕЦ
