from base.base_page import BasePage
from utils.actions import Action
from locators.locator import Register as RegisterPageLocators
from locators.locator import Base as BasePageLocators

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def register(self, user):
        Action(self.driver).enter(RegisterPageLocators.email_txb, user.get_mail())
        Action(self.driver).enter(RegisterPageLocators.passwword_txb, user.get_password())
        Action(self.driver).enter(RegisterPageLocators.confirm_pwd_txb, user.get_password())
        Action(self.driver).enter(RegisterPageLocators.pid_txb, user.get_pid())
        Action(self.driver).click(RegisterPageLocators.register_btn)

    def get_mes_error_register(self):
        return Action(self.driver).get_text(BasePageLocators.mes_problem_acc)

    def get_mes_error_pwd(self):
        return Action(self.driver).get_text(RegisterPageLocators.message_invalid_pwd)

    def get_mes_error_pid(self):
        return Action(self.driver).get_text(RegisterPageLocators.message_invalid_pid)