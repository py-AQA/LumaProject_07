from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.abstract import Page


class Link(Page):
    LOCATOR = (By.CSS_SELECTOR, ".page-footer")
    TEXT = ""
    COLOR = ""
    VISITED_COLOR = ""
    HOVER_COLOR = ""
    HREF = ""
    BACKGROUND_COLOR = "#ff0101"

    def el(self):
        return self.is_clickable(self.LOCATOR)

    def ck_background_color(self):
        assert self.el().value_of_css_property("background-color") == self.BACKGROUND_COLOR

    def ck_text(self):
        assert self.el().text == self.TEXT

    def ck_href(self):
        assert self.el().get_attribute("href") == self.TEXT


class Footer(Page):
    # FOOTER = (By.CSS_SELECTOR, "div.footer.content")
    LOCATOR = (By.CSS_SELECTOR, ".page-footer")
    ALL_LINKS = (By.CSS_SELECTOR, ".page-footer a")
    LINKS = ["l11", "l2", "l3"]
    BACKGROUND_COLOR = "#ff0101"

    def links(self):
        return self.are_present(self.ALL_LINKS)

    def el(self):
        return self.is_clickable(self.LOCATOR)

    def ck_background_color(self):
        assert self.el().value_of_css_property("background-color") == self.BACKGROUND_COLOR


class BurgerMenu(Page):
    SIGN_IN_SIDE = (By.CSS_SELECTOR, "div.section-item-content li.authorization-link a")
    ACCOUNT_SIDE = (By.CSS_SELECTOR, "div.section-item-content li a")
    WELCOME_SIDE = (By.CSS_SELECTOR, "div.section-item-content span.logged-in")
    SIGN_OUT_SIDE = (By.CSS_SELECTOR, "div.section-item-content li.authorization-link a")
    WISHLIST_SIDE = (By.CSS_SELECTOR, "div.section-item-content li.wishlist")

    def sign_in_side(self):
        return self.is_clickable(self.SIGN_IN_SIDE)


class HomePage(Page):
    URL = "https://magento.softwaretestingboard.com/"

    SIGN_IN = (By.CSS_SELECTOR, "div.panel li.authorization-link a")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, ".panel li:nth-child(3) a")
    LOGO = (By.CSS_SELECTOR, "a.logo")

    ACCOUNT_PANEL = (By.CSS_SELECTOR, "div.panel li a")
    WELCOME_PANEL = (By.CSS_SELECTOR, "div.panel span.logged-in")
    SIGN_OUT_PANEL = (By.CSS_SELECTOR, "div.panel li.authorization-link a")
    WISHLIST_PANEL = (By.CSS_SELECTOR, "div.panel li.wishlist")

    # TEXT = 'sex'
    # copyright = Copyright()
    # burger = BurgerMenu()
    switch = 768

    def __init__(self, driver, url=URL):
        super().__init__(driver)
        self.current_url = url
        self.footer = Footer(driver)



    @property
    def sign_in(self):
        # print(self.window_size())
        return self.is_clickable(self.SIGN_IN)

    @property
    def create_account(self):
        return self.is_clickable(self.CREATE_ACCOUNT)

    @property
    def logo(self):
        return self.is_visible(self.LOGO)



