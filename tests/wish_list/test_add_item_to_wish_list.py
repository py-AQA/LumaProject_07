from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.add_wish_list import ItemToWishList
from time import sleep
import pytest


def test_add_to_wish_list(driver, auth):
    page = ItemToWishList(driver)
    page.open()
    page.add_item_to_wish_list().click()
    # todo убрать явный слип и сделать ожидание которое не ломается
    assert page.current_url.startswith("https://magento.softwaretestingboard.com/wishlist/")
    assert page.success_message == ItemToWishList.MESSAGE


