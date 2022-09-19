from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stationName = db.Column(db.String(150))
    area = db.Column(db.String(150))

class AreaNorth(db.Model):
    trainNumber = db.Column(db.String(150), primary_key=True)
    workingTime = db.Column(db.String(150), primary_key=True)
    departureStation = db.Column(db.String(150))
    arrivalStation = db.Column(db.String(150))
    timeOfDeparture = db.Column(db.String(150), primary_key=True)
    route = db.Column(db.String(150))

class AreaCentral(db.Model):
    trainNumber = db.Column(db.String(150), primary_key=True)
    workingTime = db.Column(db.String(150), primary_key=True)
    departureStation = db.Column(db.String(150))
    arrivalStation = db.Column(db.String(150))
    timeOfDeparture = db.Column(db.String(150), primary_key=True)
    route = db.Column(db.String(150))

class AreaSouth(db.Model):
    trainNumber = db.Column(db.String(150), primary_key=True)
    workingTime = db.Column(db.String(150), primary_key=True)
    departureStation = db.Column(db.String(150))
    arrivalStation = db.Column(db.String(150))
    timeOfDeparture = db.Column(db.String(150), primary_key=True)
    route = db.Column(db.String(150))

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departureStation = db.Column(db.String(150))
    destinationStation = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    trips = db.relationship('Trip')
