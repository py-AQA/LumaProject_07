from data.locators import MyAccountPageLocators
from pages.my_account import MyAccountPage


class TestMyAccountSwitchingButtons:
    #тестируем переходы по вкладкам в моем аккаунте
    def test_my_account_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.my_orders_button().click()
        page.my_account_button().click()
        assert page.current_url == MyAccountPageLocators.URL_MY_ACCOUNT, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ МОЙ АККАУНТ"

    def test_my_orders_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.my_orders_button().click()
        assert page.current_url == MyAccountPageLocators.URL_MY_ORDERS, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ ЗАКАЗОВ"

    def test_my_downloadable_products_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.my_downloadable_products_button().click()
        assert page.current_url == MyAccountPageLocators.URL_MY_DOWNLOADABLE_PRODUCTS, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ DOWNLOADABLE PRODUCTS"

    def test_my_wish_list_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.my_wish_list_button().click()
        assert page.current_url == MyAccountPageLocators.URL_MY_WISH_LIST, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ WISH LIST"

    def test_address_book_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.address_book_button().click()
        assert page.current_url == MyAccountPageLocators.URL_NEW_ADDRESS_BOOK, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ ADRESS BOOK"

    def test_account_information_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.account_information_button().click()
        assert page.current_url == MyAccountPageLocators.URL_ACCOUNT_INFORMATION, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ ACCOUNT INFORMATION"

    def test_stored_payment_methods_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.stored_payment_methods_button().click()
        assert page.current_url == MyAccountPageLocators.URL_STORED_PAYMENT_METHODS, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ PAYMENT METHODS"

    def test_my_product_review_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.my_product_reviews_button().click()
        assert page.current_url == MyAccountPageLocators.URL_MY_PRODUCT_REVIEW, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ MY PRODUCT REVIEW"


class TestCorrectnessOfTheSwitchButtonsName:
    #тестируем правильное отображение текста кнопок в аккаунте
    def test_my_account_button_name(self, driver, auth):
        page = MyAccountPage(driver)
        assert page.my_account_button().text == "My Account", 'Название кнопки My Account неправильное'

    def test_my_orders_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.my_orders_button().click()
        assert page.my_orders_button().text == "My Orders", 'Название кнопки My Orders неправильное'

    def test_my_downloadable_products_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.my_downloadable_products_button().click()
        assert page.my_downloadable_products_button().text =="My Downloadable Products", 'Название кнопки My Downloadable Products неправильное'

    def test_my_wish_list_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.my_wish_list_button().click()
        assert page.my_wish_list_button().text == "My Wish List", 'Название кнопки My Wish List неправильное'

    def test_address_book_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.address_book_button().click()
        assert page.address_book_button().text == "Address Book", 'Название кнопки Address Book неправильное'

    def test_account_information_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.account_information_button().click()
        assert page.account_information_button().text == "Account Information", 'Название кнопки Account Information неправильное'

    def test_stored_payment_methods_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.stored_payment_methods_button().click()
        assert page.stored_payment_methods_button().text == "Stored Payment Methods", 'Название кнопки Stored Payment Methods неправильное'

    def test_my_product_review_button(self, driver, auth):
        page = MyAccountPage(driver)
        page.my_product_reviews_button().click()
        assert page.my_product_reviews_button().text == "My Product Reviews", 'Название кнопки My Product Reviews неправильное'
