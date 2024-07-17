import pytest

from config.config import read_config
from enums.enum import TabName
from models.user import User
from pages.login_page import LoginPage
from pages.mail_page import MailPage
from pages.register_page import RegisterPage
from pages.book_ticket_page import BookTicketPage
from pages.my_ticket_page import MyTicketPage
from test_data.test_data import *
from enums.enum import Station

@pytest.mark.usefixtures("setup_and_teardown")
class TestFilterTicket:

    def register(self):
        self.register_page = RegisterPage(self.driver)
        self.mail_page = MailPage(self.driver)
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

        self.mail_page.switch_tab_by_url(read_config("tempmail_url"))
        self.mail_page.clean_mail(mail_confirm_instruction)
        self.mail_page.switch_tab_by_url(read_config(("railway_url")))
        return user

    def test_filter(self):
        # init
        self.login_page = LoginPage(self.driver)
        self.book_ticket_page = BookTicketPage(self.driver)
        self.my_ticket_page = MyTicketPage(self.driver)
        tickets_data = get_tickets()
        filter_depart_station = Station.DANANG
        filter_depart_date = "8/1/2024"

        # register
        user = self.register()

        # login
        self.login_page.select_tab(TabName.LOGIN.value)
        self.login_page.login(user)

        # book ticket
        self.book_ticket_page.book_ticket_from_json(tickets_data)

        # filter
        self.my_ticket_page.select_tab(TabName.MY_TICKET.value)
        self.my_ticket_page.filter_ticket(filter_depart_station, filter_depart_date)
        is_correct_filter = self.my_ticket_page.is_correct_filter_ticket(filter_depart_station, filter_depart_date)
        self.my_ticket_page.clean_ticket()
        assert is_correct_filter == True