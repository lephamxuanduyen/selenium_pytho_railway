import pytest
import allure
from utils.webdriver_factory import WebDriverFactory

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default=None, help="my option: chrome or firefox"
    )
    parser.addoption(
        "--target", action="store", default="local", help="my option: local or remote"
    )

@pytest.fixture(scope="class")
def setup_and_teardown(request):
    wdf = WebDriverFactory()
    browser = get_browser(request)
    target = get_target(request)
    driver = wdf.get_driver(browser, target)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()

def get_browser(request):
    if hasattr(request, 'param'):
        browser = request.param
    if request.config.getoption("--browser"):
        browser = request.config.getoption("--browser")
    if not hasattr(request, 'param') and not request.config.getoption("--browser"):
        browser = "chrome"
    return browser

def get_target(request):
    if request.config.getoption("--target"):
        return request.config.getoption("--target")
    else:
        return "local"

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Quá trình thực hiện các bài kiểm tra
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        # Nếu bài kiểm tra thất bại, chụp ảnh màn hình
        driver = item.cls.driver
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)