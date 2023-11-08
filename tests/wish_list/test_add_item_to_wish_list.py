import pytest

from pages.add_wish_list import ItemToWishList


@pytest.mark.skip
def test_add_to_wish_list(driver, create_account):
    page = ItemToWishList(driver)
    page.open()
    page.add_item_to_wish_list().click()
    assert page.current_url.startswith("https://magento.softwaretestingboard.com/wishlist/")
    assert page.success_message == ItemToWishList.MESSAGE


