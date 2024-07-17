from enum import Enum

class TabName(Enum):
    HOME = "Home"
    FAQ = "FAQ"
    CONTACT = "Contact"
    TIMETABLE = "Timetable"
    TICKET_PRICE = "Ticket price"
    BOOK_TICKET = "Book ticket"
    REGISTER = "Register"
    LOGIN = "Login"
    LOGOUT = "Log out"
    MY_TICKET = "My ticket"
    CHANGE_PASSWORD = "Change password"

class Station:
    SAIGON = "Sài Gòn"
    NHATRANG = "Nha Trang"
    PHANTHIET = "Phan Thiết"
    QUANGNGAI = "Quảng Ngãi"
    DANANG = "Đà Nẵng"
    HUE = "Huế"

class SeatType:
    HS = "Hard seat"
    SS = "Soft seat"
    SSC = "Soft seat with air conditioner"
    HB = "Hard bed"
    SB = "Soft bed"
    SBC = "Soft bed with air conditioner"