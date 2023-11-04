import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


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


def pytest_configure(config):
    print(">>>")


def pytest_unconfigure(config):
    print("<<<")


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


@pytest.fixture(scope="function")
def options(browser, state):
    options = None
    if browser == "chrome":
        options = ChromeOptions()
        # options.add_argument('--window-size=800,800')
    if browser == "firefox":
        options = FirefoxOptions()
        # options.add_argument('--width=800')
        # options.add_argument('--height=800')
    if browser == "edge":
        options = EdgeOptions()
    if state == 'headless':
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-setuid-sandbox")
    # options.add_argument("--no-zygote")
    return options


@pytest.fixture(scope="function", autouse=True)
def driver_fixture(request, browser, place, options):
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
    print('>>>>>>>>>>>>>>>>>>>>>>init driver')
    request.cls.driver = driver
    yield
    print('>>>>>>>>>>>>>>>>>>>>>>quit driver')
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def login_fixture(request):
    request.cls.my_login = "XXXXXXXX"
    request.cls.my_password = "XXXXXXXX"
