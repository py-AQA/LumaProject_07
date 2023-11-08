from pages.login_page import LoginPage
from pages.my_account import MyAccountPage
from pages.registration_page import RegistrationPage
from pages.my_account_wish_list import MyAccountWishListPage


def test_check_item_present(driver, auth):
    page = MyAccountWishListPage(driver)
    # page.open()
    assert page.check_item_present(), 'item не найден'


