from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.add_wish_list import ItemToWishList
from time import sleep
import pytest


def test_add_to_wish_list(driver, auth):
    page = ItemToWishList(driver)
    page.open()
    page.add_item_to_wish_list().click()
    assert page.success_message == ItemToWishList.MESSAGE

