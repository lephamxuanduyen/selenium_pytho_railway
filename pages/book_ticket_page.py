from selenium.webdriver.common.by import By

from base.base_page import BasePage
from locators.locator import BookTicket as BookTicketPageLocators
from utils.actions import Action
from test_data.test_data import *
from enums.enum import TabName

class BookTicketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def book_ticket(self, ticket):
        self.select_depart_station(ticket.get_depart_station())
        self.select_depart_date(ticket.get_depart_date())
        self.select_seat_type(ticket.get_seat_type())
        self.select_ticket_amount(ticket.get_ticket_amount())
        self.select_arrive_station(ticket.get_arrive_station())
        Action(self.driver).click(BookTicketPageLocators.submit_form_btn)

    def select_value(self, field, value):
        Action(self.driver).select(BookTicketPageLocators.txb % field, value)

    def select_depart_station(self, station):
        self.select_value("DepartStation", station)

    def select_arrive_station(self ,station):
        self.select_value("ArriveStation", station)

    def select_depart_date(self, date):
        self.select_value("Date", date)

    def select_seat_type(self, seatype):
        self.select_value("SeatType", seatype)

    def select_ticket_amount(self, amount):
        self.select_value("TicketAmount", amount)

    def book_ticket_from_json(self, tickets_data):
        for ticket_data in tickets_data:
            ticket = get_a_ticket(ticket_data)
            self.select_tab(TabName.BOOK_TICKET.value)
            self.book_ticket(ticket)
