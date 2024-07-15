import pytest
from config.config import read_config
from enums.enum import TabName
from models.user import User
from pages.register_page import RegisterPage
from pages.mail_page import MailPage
from test_data.test_data import *
from helper.soft_assert import SoftAssert

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_register_active_acc(self):
        self.register_page = RegisterPage(self.driver)
        self.mail_page = MailPage(self.driver)
        '''
        User can't create account with an already in-use email
        :return:
        '''

        mail_confirm_instruction = "thanhletraining03@gmail.com "

        self.mail_page.open_mailpage()
        self.mail_page.switch_tab_by_url(read_config("tempmail_url"))
        mail = self.mail_page.get_mail()
        user = User(mail, get_info_user("valid_pwd"), get_info_user("valid_pid"))

        self.register_page.switch_tab_by_url(read_config("railway_url"))
        self.register_page.select_tab(TabName.REGISTER.value)
        self.register_page.register(user)
        self.register_page.close_tab()

        self.mail_page.switch_tab_by_url(read_config("tempmail_url"))
        self.mail_page.confirm_acc(mail_confirm_instruction)

        self.register_page.switch_tab_by_url(read_config("railway_url"))
        self.register_page.select_tab(TabName.REGISTER.value)
        self.register_page.register(user)

        expected_result = get_message("register", "mail_already_in_use")
        actual_result = self.register_page.get_mes_error_register()
        assert actual_result == expected_result

    def test_register_empty_pwd_pid(self):
        self.register_page = RegisterPage(self.driver)
        self.mail_page = MailPage(self.driver)
        '''
        User can't create account while password and PID fields are empty
        :return:
        '''
        self.register_page.select_tab(TabName.REGISTER.value)
        user = User(get_info_user("valid_mail"), "", "")
        self.register_page.register(user)
        softAssert = SoftAssert()
        softAssert.check(get_message("register","error_form"), "Message error register doesn't display.")
        softAssert.check(get_message("register", "error_password"), "Message invalid password doesn't display.")
        softAssert.check(get_message("register", "error_pid"), "Message invalid pid doesn't display.")
        softAssert.assert_all()