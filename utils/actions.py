from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Action:
    def __init__(self, driver):
        self.driver = driver
    def click(self, xpath):
        self.scroll(xpath)
        self.driver.find_element(By.XPATH, xpath).click()

    def enter(self, xpath, value):
        self.driver.find_element(By.XPATH, xpath).send_keys(value)

    def is_display(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).is_displayed()

    def get_text(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).text

    def scroll(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def select(self, xpath, value):
        self.scroll(xpath)
        select = Select(self.driver.find_element(By.XPATH, xpath))
        select.selectByVisibleText(value)

    def is_select(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).is_selected()