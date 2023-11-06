from selenium.webdriver.common.by import By
from pages.abstract import Page


class ItemDetailsPage(Page):
    URL = "https://magento.softwaretestingboard.com/luma-analog-watch.html"

    ADD_TO_CART = (By.CSS_SELECTOR, "button.tocart")

    SUCCESS = "You added Luma Analog Watch to your shopping cart."

    def __init__(self, driver, url=URL):
        super().__init__(driver)
        self.current_url = url

    def add_to_cart(self):
        return self.is_clickable(self.ADD_TO_CART)
