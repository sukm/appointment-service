from enum import Enum


class BookingType(Enum):
    available = 1
    reserved = 2
    booked = 3
    expired = 4
