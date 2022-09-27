from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Station(db.Model):
    __tablename__ = 'Station'

    id = db.Column(db.Integer, primary_key=True)
    stationName = db.Column(db.String(150))
    area = db.Column(db.String(150))


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departureStation = db.Column(db.String(150))
    destinationStation = db.Column(db.String(150))
    day = db.Column(db.String(150))
    time = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    trips = db.relationship('Trip')

