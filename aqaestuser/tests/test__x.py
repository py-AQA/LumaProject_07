from pages.abstract import Page
from pages.home import HomePage
from pages.create_account import CreateAccountPage
from pages.sign_in import SignInPage
from pages.account import AccountPage
from pages.account_edit import AccountEditPage
from pages.logout import LogoutPage

from fake_data import TestDriver, first_name, last_name, email, password


class TestNow(TestDriver):

    def test_run(self):
        page = HomePage(self.driver)
        page.demo.ck_text()
        demo = page.demo
        demo.ck_css()
