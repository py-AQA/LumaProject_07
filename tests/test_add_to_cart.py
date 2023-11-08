from pages.main_page import MainPage


class TestSuccessMessageAddToCart:

    def test_driven_backpack_text(self, driver):
        page = MainPage(driver)
        page.add_driven_backpack_from_backpacks_catalog_to_cart()
        assert page.success_add_to_cart_message().text == page.text_success_message('Driven Backpack')

    def test_clamber_watch_text(self, driver):
        page = MainPage(driver)
        page.add_clamber_watch_from_watches_catalog_to_cart()
        assert page.success_add_to_cart_message().text == page.text_success_message('Clamber Watch')

    def test_montana_wind_jacket_text(self, driver):
        page = MainPage(driver)
        page.add_montana_wind_jacket_from_men_jacket_to_cart()
        assert page.success_add_to_cart_message().text == page.text_success_message('Montana Wind Jacket')

    def test_add_yoga_kit_text(self, driver):
        page = MainPage(driver, 'https://magento.softwaretestingboard.com/sprite-yoga-companion-kit.html')
        page.add_yoga_kit_from_gear_fitness_to_cart()
        assert page.success_add_to_cart_message().text == page.text_success_message('Sprite Yoga Companion Kit')

    def test_add_portia_capri_28_blue_color_to_cart(self, driver):
        page = MainPage(driver)
        page.add_portia_capri_28_blue_color_to_cart()
        assert page.success_add_to_cart_message().text == page.text_success_message('Portia Capri')


class TestNegativeQuantity:

    def test_negative_quantity(self, driver):
        page = MainPage(driver, 'https://magento.softwaretestingboard.com/sprite-yoga-companion-kit.html')
        page.add_negative_items_to_cart()
        assert page.error_quantity_msg().text == 'Please enter a quantity greater than 0.'

    def test_zero_quantity(self, driver):
        page = MainPage(driver, 'https://magento.softwaretestingboard.com/sprite-yoga-companion-kit.html')
        page.add_zero_items_to_cart()
        assert page.error_quantity_msg().text == 'Please enter a quantity greater than 0.'

    def test_add_more_than_maximum_items(self, driver):
        # todo sometimes fails - to check for loaders later
        page = MainPage(driver, 'https://magento.softwaretestingboard.com/sprite-yoga-companion-kit.html')
        page.add_more_than_maximum_items_to_cart()
        assert page.error_quantity_msg().text == 'The maximum you may purchase is 10000.'

    def test_add_more_than_in_stock_items(self, driver):
        page = MainPage(driver, 'https://magento.softwaretestingboard.com/sprite-yoga-companion-kit.html')
        page.add_more_than_in_stock_items_to_cart()
        assert page.error_qty_is_not_available().text == 'The requested qty is not available'


class TestAddToCartIconCounter:

    def test_add_one_item(self, driver):
        page = MainPage(driver)
        page.add_portia_capri_28_blue_color_to_cart()
        assert page.cart_counter().text == '1'

    def test_add_five_items(self, driver):
        page = MainPage(driver, 'https://magento.softwaretestingboard.com/sprite-yoga-companion-kit.html')
        page.add_yoga_kit_from_gear_fitness_to_cart(5)
        assert page.cart_counter().text == '5'




