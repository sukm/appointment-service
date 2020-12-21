import logging
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from ma import ma
from db import db
from resources.time_slot import TimeSlot, TimeSlotAvailability
from enums.BookingType import BookingType

FORMAT = '%(asctime)s|%(name)s|%(levelname)s|%(lineno)d|%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
LOGGER = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object("config")
api = Api(app)
migrate = Migrate(app, db)

api.add_resource(TimeSlot, '/timeSlots')
api.add_resource(TimeSlotAvailability, '/timeSlots/availability')

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True, port=5000)
