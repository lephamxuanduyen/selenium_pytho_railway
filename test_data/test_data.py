import os
from utils.read_json import readJson
from models.ticket import Ticket

def get_message(page, key):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'message.json'
    file_path = os.path.join(current_dir, file_name)
    datas = readJson(file_path)
    return datas.get(page).get(key)

def get_info_user(key):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'user.json'
    file_path = os.path.join(current_dir, file_name)
    return readJson(file_path)[key]

def get_tickets():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'tickets.json'
    file_path = os.path.join(current_dir, file_name)
    return readJson(file_path).get("ticketSameStation")

def get_a_ticket(ticket_data):
    date = ticket_data.get("DepartDate")
    depart_station = ticket_data.get("DepartStaion")
    arrive_station = ticket_data.get("ArriveStation")
    seat_type = ticket_data.get("SeatType")
    ticket_amount = ticket_data.get("TicketAmount")

    ticket = Ticket(date, depart_station, arrive_station, seat_type, ticket_amount)
    return ticket
