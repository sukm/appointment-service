from db import db
from datetime import datetime
from enums.BookingType import BookingType
from typing import List


class TimeSlotModel(db.Model):
    """
    For simplicity, assume we allow only one patient per time slot
    """
    __tablename__ = 'time_slots'
    id = db.Column(db.Integer, primary_key=True)
    start_timestamp = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(BookingType), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_available_slot(cls, start_timestamp, duration) -> 'TimeSlotModel':
        return cls.query.filter_by(start_timestamp=start_timestamp,
                                   duration=duration,
                                   status=BookingType.available).first()

    @classmethod
    def find_previous_slots(cls, start_timestamp,
                            duration) -> List["TimeSlotModel"]:
        return cls.query.filter(start_timestamp == start_timestamp,
                                duration == duration,
                                cls.status != BookingType.expired).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
