from sre_constants import SUCCESS
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Station, User
from . import db, stationNames, SearchRoute
import json
import pyodbc

views = Blueprint('views', __name__)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#data = stationNames.read()
#stations = data.split("\n")

trainsToTake = []

@views.route('/', methods=['GET', 'POST'])
def home():
    stations = [r.stationName for r in Station.query.order_by(Station.stationName).all()]
    trainsToTake = []
    if request.method == 'POST':
        departureStation = str(request.form.get('departureStation'))
        destinationStation = str(request.form.get('destinationStation'))
        day = str(request.form.get('day'))
        departureTime = request.form.get('departureTime')
        print(departureTime)

        if ((departureStation not in stations) or (destinationStation not in stations)):
            flash('Invalid station!', category='error')
        elif (day not in days):
            flash('Invalid day!', category='error')
        elif (departureTime == ""):
            flash('Time not selected!', category='error')
        else:
            trainsToTake = ['M','B','C']
            return redirect(url_for('views.result'))

    return render_template("home.html", user = current_user, stations = stations, days = days)

@views.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
    return render_template("result.html", user = current_user, trains = trainsToTake)
