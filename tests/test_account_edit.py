from data.fake_data import FakeData
from pages.account import AccountPage
from pages.create_account import CreateAccountPage
from pages.account_edit import AccountEditPage
from pages.logout import LogoutPage
from pages.sign_in import SignInPage


class TestNow(FakeData):
    def test_change_first_name(self, driver, first_name, last_name, email, password):
        LogoutPage(driver)
        CreateAccountPage(driver).create(first_name, last_name, email, password)
        page = AccountEditPage(driver)
        page.first_name = self.first_name
        page.save().click()
        assert page.msg == AccountEditPage.SUCCESS
        assert page.current_url == AccountPage.URL

    def test_change_last_name(self, driver, first_name, last_name, email, password):
        LogoutPage(driver)
        CreateAccountPage(driver).create(first_name, last_name, email, password)
        page = AccountEditPage(driver)
        page.last_name = self.last_name
        page.save().click()
        # todo ffox AssertionError: assert 'Thank you fo...ebsite Store.' == 'You saved th...
        assert page.msg == AccountEditPage.SUCCESS
        assert page.current_url == AccountPage.URL

    def test_change_email(self, driver, first_name, last_name, email, password):
        LogoutPage(driver)
        CreateAccountPage(driver).create(first_name, last_name, email, password)
        page = AccountEditPage(driver)
        page.change_email().click()
        page.email = self.email
        page.password_current = password
        page.save().click()
        assert page.msg == AccountEditPage.SUCCESS
        assert page.current_url == SignInPage.URL

    def test_change_password(self, driver, first_name, last_name, email, password):
        LogoutPage(driver)
        CreateAccountPage(driver).create(first_name, last_name, email, password)
        page = AccountEditPage(driver)
        page.change_password().click()
        page.password_current = password
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        assert page.msg == AccountEditPage.SUCCESS
        assert page.current_url == SignInPage.URL

    def test_change_email_and_password(self, driver, first_name, last_name, email, password):
        LogoutPage(driver)
        CreateAccountPage(driver).create(first_name, last_name, email, password)
        page = AccountEditPage(driver)
        page.change_email().click()
        page.change_password().click()
        page.email = self.email
        page.password_current = password
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        assert page.current_url == SignInPage.URL
