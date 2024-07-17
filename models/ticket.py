class Ticket:
    def __init__(self, depart_date, depart_station, arrive_station, seat_type, ticket_amount):
        self.depart_date = depart_date
        self.depart_station = depart_station
        self.arrive_station = arrive_station
        self.seat_type = seat_type
        self.ticket_amount = ticket_amount

    def get_depart_date(self):
        return self.depart_date

    def get_depart_station(self):
        return self.depart_station

    def get_seat_type(self):
        return self.seat_type

    def get_arrive_station(self):
        return self.arrive_station

    def get_ticket_amount(self):
        return self.ticket_amount