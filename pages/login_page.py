from base.base_page import BasePage
from utils.actions import Action
from locators.locator import *
from enums.enum import TabName

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self, user):
        Action(self.driver).enter(Login.emailTxb, user.get_mail())
        Action(self.driver).enter(Login.pwdtxb, user.get_password())
        Action(self.driver).click(Login.loginBtn)

    def is_display_welcome_mes(self):
        return Action(self.driver).is_display(Base.welcome_mes)

    def is_display_error_mes(self, expected_resutl):
        actual_result = Action(self.driver).get_text(Base.mes_problem_acc)
        return actual_result == expected_resutl

    def login_manytime(self, user, times, sort_assert, expected_resutl):
        for i in range(times):
            self.select_tab(TabName.LOGIN.value)
            self.login(user)
            sort_assert.check(self.is_display_error_mes(expected_resutl), f"Time {i + 1}: Message doesn't display like expect.")