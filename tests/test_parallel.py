import pytest
from pages.login_page import LoginPage
from enums.enum import TabName
from models.user import User
from test_data.test_data import *

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogout:

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.login_page = LoginPage(self.driver)

    @pytest.mark.parametrize('setup_and_teardown', ['chrome'], indirect=True)
    def test_logout_chrome(self):
        self.login_page.select_tab(TabName.LOGIN.value)
        user = User(get_info_user("valid_mail"), get_info_user("valid_pwd"))
        self.login_page.login(user)

        self.login_page.select_tab(TabName.FAQ.value)

        self.login_page.select_tab(TabName.LOGOUT.value)
        assert self.login_page.is_loged_out()==False

    @pytest.mark.parametrize('setup_and_teardown', ['firefox'], indirect=True)
    def test_logout_firefox(self):
        self.login_page.select_tab(TabName.LOGIN.value)
        user = User(get_info_user("valid_mail"), get_info_user("valid_pwd"))
        self.login_page.login(user)

        self.login_page.select_tab(TabName.FAQ.value)

        self.login_page.select_tab(TabName.LOGOUT.value)
        assert self.login_page.is_loged_out() == False