import pytest
from utils.webdriver_factory import WebDriverFactory

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome or firefox"
    )
    parser.addoption(
        "--target", action="store", default="local", help="my option: local or remote"
    )

@pytest.fixture(scope="class")
def setup_and_teardown(request):
    wdf = WebDriverFactory()
    browser = get_browser(request).lower()
    target = get_target(request).lower()
    driver = wdf.get_driver(browser, target)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()

def get_browser(request):
    if request.config.getoption("--browser"):
        return request.config.getoption("--browser")
    else:
        return "chrome"

def get_target(request):
    if request.config.getoption("--target"):
        return request.config.getoption("--target")
    else:
        return "local"