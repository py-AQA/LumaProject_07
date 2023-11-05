import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

GRID_URL = "http://localhost:4444/wd/hub"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        choices=['chrome', 'firefox', 'edge', 'all'],
        action="store",
        default='chrome',
        help="browsers to run",
    )
    parser.addoption(
        "--place",
        choices=['remote', 'local', 'all', 'debug'],
        action="store",
        default='local',
        help="place to run browsers",
    )
    parser.addoption(
        "--state",
        choices=['headless', 'visible'],
        action="store",
        default='headless',
        help="state to run browsers",
    )


def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        option = metafunc.config.getoption("browser")
        option = ['chrome', 'firefox', 'edge'] if option == 'all' else [option]
        metafunc.parametrize("browser", dict(zip(option, option)), scope="function")
    if "place" in metafunc.fixturenames:
        option = metafunc.config.getoption("place")
        option = ['remote', 'local'] if option == 'all' else [option]
        metafunc.parametrize("place", dict(zip(option, option)), scope="function")
    if "state" in metafunc.fixturenames:
        option = [metafunc.config.getoption("state")]
        metafunc.parametrize("state", dict(zip(option, option)), scope="function")


@pytest.fixture
def options(browser, state):
    options = None
    if browser == "chrome":
        options = ChromeOptions()
        # options.add_argument('--window-size=800,800')

        options.add_argument("--disable-automatic-password-saving")
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-material-design-user-manager")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-session-crashed-bubble")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-translate")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--no-zygote")
    if browser == "firefox":
        options = FirefoxOptions()
        # options.add_argument('--width=800')
        # options.add_argument('--height=800')
    if browser == "edge":
        options = EdgeOptions()
    if state == 'headless':
        options.add_argument("--headless")
    return options


@pytest.fixture(scope="function", autouse=True)
def driver(request, browser, place, options):
    driver = None
    if place == 'debug':
        print('\n_deb_driver starting_')
        myoptions = ChromeOptions()
        # myoptions.add_argument('--window-size=750,750')
        myoptions.add_experimental_option("debuggerAddress", "localhost:9222")
        # myoptions.add_argument("--headless")
        # myoptions.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=myoptions)
        original_window = driver.current_window_handle
        driver.switch_to.new_window('tab')

        request.cls.driver = driver
        yield

        driver.close()
        print('\n_deb_driver page closed_')
        driver.switch_to.window(original_window)
        print('\n_deb_driver exiting - original page untouched_')
        return None

    if browser == "chrome":
        if place == 'local':
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    if browser == "firefox":
        if place == 'local':
            driver = webdriver.Firefox(options=options)
        else:
            driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    if browser == "edge":
        if place == 'local':
            driver = webdriver.Edge(options=options)
        else:
            driver = webdriver.Remote(command_executor=GRID_URL, options=options)

    yield driver
    driver.quit()


@pytest.fixture
def random_email():
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


# todo стоит ли передавать новые данные фикстурами
# @pytest.fixture
# def wait_1(driver):
#     wait_our = WebDriverWait(driver, timeout=15)
#     return wait_our


@pytest.fixture
def random_new_email():
    faker = Faker()
    return faker.email()


@pytest.fixture
def random_new_password():
    faker = Faker()
    return faker.password()
