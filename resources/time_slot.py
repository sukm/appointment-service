import logging
from datetime import datetime, timedelta
from flask import request
from flask_restful import Resource
from enums.BookingType import BookingType
from models.time_slot import TimeSlotModel
from schemas.time_slot import TimeSlotSchema

LOGGER = logging.getLogger(__name__)
time_slot_schema = TimeSlotSchema()


class TimeSlot(Resource):
    @classmethod
    def post(cls):
        """
        We assume multiple same time slots with same timestamp and duration exist.
        """
        time_slot_json = request.get_json()
        time_slot_json['status'] = BookingType.available
        time_slot = TimeSlotModel(**time_slot_json)
        try:
            time_slot.save_to_db()
        except:
            return {'message': 'time slot error inserting'}, 500
        return {'message': 'Successfully created a time slot'}, 201

    @classmethod
    def put(cls):
        """
        For simplicity, the logic uses local timezone.
        
        if addition of start_timestamp and duration is less than the current time we set time slots to expired.
        """
        time_slot_json = request.get_json()
        time_slot_data = time_slot_schema.load(time_slot_json)
        start_timestamp = time_slot_data.get('start_timestamp')
        start_datetime = datetime.strptime(start_timestamp,
                                           '%Y-%m-%d %H:%M:%S')
        duration = time_slot_data.get('duration')
        end_timestamp = start_datetime + timedelta(minutes=duration)

        if end_timestamp < datetime.now():
            time_slots = TimeSlotModel.find_previous_slots(
                start_timestamp, duration)
            for time_slot in time_slots:
                time_slot.status = BookingType.expired
                time_slot.save_to_db()
        else:
            return {'message': 'Invalid time range'}
        return {'message': 'Successfully set time slots to expired'}, 200


class TimeSlotAvailability(Resource):
    @classmethod
    def get(cls):
        time_slot_json = request.get_json()
        time_slot_data = time_slot_schema.load(time_slot_json)
        time_slot = TimeSlotModel.find_available_slot(**time_slot_data)
        if time_slot:
            return {'message': 'Found available time slot'}, 200
        return {'message': 'Time slot not found'}, 404
