from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from base.base_page import BasePage

class WebDriverFactory:
    def get_driver(self, browser, target):
        if target == "local":
            if browser == "chrome":
                driver = webdriver.Chrome(service=ChromeService())
            elif browser == "firefox":
                driver = webdriver.Firefox(service=FirefoxService())
            else:
                driver = webdriver.Chrome(service=ChromeService())
            BasePage(driver).open_railway()
            return driver
        elif target == "remote":
            if browser == "chrome":
                options = ChromeOptions()
            elif browser == "firefox":
                options = FirefoxOptions()
            else:
                options = ChromeOptions()
            driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=options)
            BasePage(driver).open_railway()
            return driver
