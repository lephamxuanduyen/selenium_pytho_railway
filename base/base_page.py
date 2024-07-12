from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import read_config
from enums.enum import TabName
from locators.locator import *
from utils.actions import Action
from locators.locator import Base as BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def open_railway(self):
        retry_count = 5
        retry = 0
        while (retry < retry_count):
            try:
                self.driver.get(read_config("railway_url"))
                if 'Safe Railway' in self.driver.title:
                    break
            except WebDriverException:
                raise RuntimeError("Failed to load.")
            retry += 1

    def switch_tab_by_url(self, url):
        tabs = self.driver.window_handles
        for tab in tabs:
            self.driver.switch_to.window(tab)
            if url in self.driver.current_url:
                return
        raise Exception(f"No tab with URL {url} found")

    def get_current_window(self):
        return self.driver.current_window_handle

    def select_tab(self, tab_name):
        xpath = Base.tab_menu % tab_name
        Action(self.driver).click(xpath)

    def open_mailpage(self):
        self.driver.execute_script(f"window.open('{read_config('tempmail_url')}', '_blank');")

    def is_loged_out(self):
        try:
            return Action(self.driver).is_display(BasePageLocators.tab_menu % TabName.LOGOUT.value)
        except NoSuchElementException:
            return False

    def close_tab(self):
        self.driver.close()

    def refresh(self):
        self.driver.refresh()

    def wait_element_to_visibility(self, xpath, time):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.XPATH, xpath)))
