from config.config import read_config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from base.base_page import BasePage

class WebDriverFactory:
    def get_driver(self, browser):
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService())
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService())
        else:
            driver = webdriver.Chrome(service=ChromeService())
        BasePage(driver).open_railway()
        return driver
