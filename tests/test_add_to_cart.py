from pages.main_page import MainPage


class TestAddToCart:

    def test_add_driven_backpack(self, driver):
        page = MainPage(driver)
        page.add_driven_backpack_from_backpacks_catalog_to_cart()

    def test_add_clamber_watch(self, driver):
        page = MainPage(driver)
        page.add_clamber_watch_from_watches_catalog_to_cart()

    def test_add_montana_wind_jacket_from_men_jacket_to_cart(self, driver):
        page = MainPage(driver)
        page.add_montana_wind_jacket_from_men_jacket_to_cart()

    def test_add_yoga_kit(self, driver):
        page = MainPage(driver, 'https://magento.softwaretestingboard.com/sprite-yoga-companion-kit.html')
        page.add_yoga_kit_from_gear_fitness_to_cart()
