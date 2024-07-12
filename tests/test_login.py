import pytest
from pages.login_page import LoginPage
from pages.mail_page import MailPage
from models.user import User
from enums.enum import TabName
from test_data.test_data import *
from helper.soft_assert import *
from config.config import read_config
from pages.register_page import RegisterPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.login_page = LoginPage(self.driver)
        self.mail_page = MailPage(self.driver)
        self.register_page = RegisterPage(self.driver)

    def test_login_valid_user(self):
        '''
        User can log into Railway with valid username and password.
        :return:
        '''
        user=User(get_info_user("valid_mail"), get_info_user("valid_pwd"))
        self.login_page.select_tab(TabName.LOGIN.value)
        self.login_page.login(user)
        assert self.login_page.is_display_welcome_mes()!=None, "Welcome Message doesn't display."

    def test_login_blank_mail(self):
        '''
        User cannot login with blank "Username" textbox.
        :return:
        '''
        user=User("", get_info_user("valid_pwd"))
        self.login_page.select_tab(TabName.LOGIN.value)
        self.login_page.login(user)
        assert self.login_page.is_display_error_mes(get_message("login","error_login"))

    def test_login_invalid_pwd(self):
        '''
        User cannot log into Railway with invalid password.
        :return:
        '''
        user = User(get_info_user("valid_mail"), get_info_user("invalid_pwd"))
        self.login_page.select_tab(TabName.LOGIN.value)
        self.login_page.login(user)
        assert self.login_page.is_display_error_mes(get_message("login","error_login")), "Message doesn't display like expected"

    def test_login_wrong_pws_manytime(self):
        '''
        System shows message when user enters wrong password many times.
        :return:
        '''
        user = User(get_info_user("valid_mail"), get_info_user("invalid_pwd"))
        soft_assert = SoftAssert()
        self.login_page.login_manytime(user, 5, soft_assert, get_message("login","error_mail_pwd"))
        soft_assert.check(self.login_page.is_display_error_mes(get_message("login","error_login_manytime")), "Message which displays to info user that they will unable to login for 15m doesn't appears.")
        soft_assert.assert_all()

    def test_acc_inactive(self):
        '''
        User can't login with an account hasn't been activated.
        :return:
        '''
        self.mail_page.open_mailpage()
        self.mail_page.switch_tab_by_url(read_config("tempmail_url"))
        self.mail_page.driver.refresh()
        mail = self.mail_page.get_mail()
        user = User(mail, get_info_user("valid_pwd"), get_info_user("valid_pid"))

        self.register_page.switch_tab_by_url(read_config("railway_url"))
        self.register_page.select_tab(TabName.REGISTER.value)
        self.register_page.register(user)

        self.login_page.select_tab(TabName.LOGIN.value)
        self.login_page.login(user)
        self.login_page.is_display_error_mes(get_message("login","error_login_mail_noactive"))