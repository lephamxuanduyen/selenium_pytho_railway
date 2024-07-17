from base.base_page import BasePage
from utils.actions import Action
from locators.locator import MyTicket as MyTicketLocators

class MyTicketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def filter_ticket(self, depart_station, depart_date):
        Action(self.driver).select(MyTicketLocators.filter_depart_station, depart_station)
        Action(self.driver).enter(MyTicketLocators.filter_date, depart_date)
        Action(self.driver).click(MyTicketLocators.filter_apply_btn)

    def is_correct_filter_ticket(self, expected_station, expected_date):
        depart_station_list = Action(self.driver).find_many_elements(MyTicketLocators.departs)
        date_list = Action(self.driver).find_many_elements(MyTicketLocators.date)
        for station in depart_station_list:
            for date in date_list:
                if station != expected_station and expected_date != date:
                    return False
        else:
            return True

    def clean_ticket(self):
        tickets = Action(self.driver).find_many_elements(MyTicketLocators.cancel_btn)
        for ticket in tickets:
            ticket.click()
