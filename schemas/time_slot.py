from ma import ma
from models.time_slot import TimeSlotModel


class TimeSlotSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TimeSlotModel
        fields = ('status', 'start_timestamp', 'duration')
