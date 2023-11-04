from pages.account import AccountPage
from pages.create_account import CreateAccountPage
from pages.account_edit import AccountEditPage
from pages.logout import LogoutPage

from fake_data import TestDriver, first_name, last_name, email, password

from pages.sign_in import SignInPage


class TestNow(TestDriver):
    def test_change_first_name(self, first_name, last_name, email, password):
        CreateAccountPage(self.driver).create(first_name, last_name, email, password)
        page = AccountEditPage(self.driver)
        page.first_name = self.first_name
        page.save().click()
        assert page.msg == AccountEditPage.SUCCESS
        assert page.url == AccountPage.URL

    def test_change_last_name(self, first_name, last_name, email, password):
        CreateAccountPage(self.driver).create(first_name, last_name, email, password)
        page = AccountEditPage(self.driver)
        page.last_name = self.last_name
        page.save().click()
        assert page.msg == AccountEditPage.SUCCESS
        assert page.url == AccountPage.URL

    def test_change_email(self, first_name, last_name, email, password):
        CreateAccountPage(self.driver).create(first_name, last_name, email, password)
        page = AccountEditPage(self.driver)
        page.change_email().click()
        page.email = self.email
        page.password_current = password
        page.save().click()
        assert page.msg == AccountEditPage.SUCCESS
        assert page.url == SignInPage.URL

    def test_change_password(self, first_name, last_name, email, password):
        CreateAccountPage(self.driver).create(first_name, last_name, email, password)
        page = AccountEditPage(self.driver)
        page.change_password().click()
        page.password_current = password
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        assert page.msg == AccountEditPage.SUCCESS
        assert page.url == SignInPage.URL

    def test_change_email_and_password(self, first_name, last_name, email, password):
        CreateAccountPage(self.driver).create(first_name, last_name, email, password)
        page = AccountEditPage(self.driver)
        page.change_email().click()
        page.change_password().click()
        page.email = self.email
        page.password_current = password
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        assert page.url == SignInPage.URL
