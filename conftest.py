from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def options():
    options = Options()
    # options.add_argument('--window-size=2880,1800')
    return options


@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

#
# @pytest.fixture
# def wait_1(driver):
#     wait_our = WebDriverWait(driver, timeout=15)
#     return wait_our


@pytest.fixture
def random_email():
    faker = Faker()
    return faker.email()


@pytest.fixture
def random_new_email():
    faker = Faker()
    return faker.email()


@pytest.fixture
def random_first_name():
    faker = Faker()
    return faker.first_name()


@pytest.fixture
def random_last_name():
    faker = Faker()
    return faker.last_name()


@pytest.fixture
def random_password():
    faker = Faker()
    return faker.password()

@pytest.fixture
def random_new_password():
    faker = Faker()
    return faker.password()
