from data.fake_data import FakeData
from pages.abstract import Page
from pages.account import AccountPage
from pages.create_account import CreateAccountPage
from pages.account_edit import AccountEditPage
from pages.home import HomePage
from pages.logout import LogoutPage
from pages.sign_in import SignInPage


class TestNow(FakeData):
    def test_run(self, driver):
        page = HomePage(driver)
        page.demo.ck_text()
        demo = page.demo
        demo.ck_css()
