from sre_constants import SUCCESS
from time import time
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import current_user
from .models import Station, User, Trip
from . import db, logged_in
import json
import pyodbc
import os
from website.SearchRoute import SearchRoute
SR = SearchRoute()
from website.Functions import Functions
f = Functions()


views = Blueprint('views', __name__)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


trainsToTake = []

# code for home page
@views.route('/', methods=['GET', 'POST'])
def home():
    # query stations from database to display them on the html page
    stations = [r.stationName for r in Station.query.order_by(Station.stationName).all()]
    trainsToTake.clear() # clear any previous trips that may be stored
    if request.method == 'POST':
        departureStation = str(request.form.get('departureStation'))
        destinationStation = str(request.form.get('destinationStation'))
        day = str(request.form.get('day'))
        departureTime = request.form.get('departureTime')
        
        # ensure stations exist and are not the same, day exists and time is entered
        if ((departureStation not in stations) or (destinationStation not in stations)):
            flash('Please enter a valid station!', category='error')
        elif (day not in days):
            flash('Please choose a valid day!', category='error')
        elif (departureTime == ""):
            flash('Time not selected!', category='error')
        elif (departureStation == destinationStation):
            flash('You are already at ' + departureStation, category = 'error')
        
        # if all input is valid, call the algortihm to calculate the shortest route
        else:
            trains = SR.search(departureStation, destinationStation, day)
            output = f.outputPaths(trains, departureTime)
            for line in output:
                trainsToTake.append(line)

            # only add the trip to the database if the user is authenticated
            if current_user.is_authenticated:
                new_trip = Trip(destinationStation=destinationStation, departureStation=departureStation,
                day=day,time=departureTime, user_id=current_user.id)
                db.session.add(new_trip)
                db.session.commit()
            return redirect(url_for('views.result'))

    return render_template("home.html", user = current_user, stations = stations, days = days, authenticated = logged_in)

# code for result page
@views.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
    return render_template("result.html", user = current_user, trains = trainsToTake)
