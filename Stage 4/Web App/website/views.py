from sre_constants import SUCCESS
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
#from .models import Note
from . import db, file
import json
import pyodbc

views = Blueprint('views', __name__)


data = file.read()
stations = data.split("\n")

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        departureStation = request.form.get('departureStation')
        departureStation = str(departureStation)
        destinationStation = request.form.get('destinationStation')
        destinationStation = str(destinationStation)
        departureTime = request.form.get('departureTime')

        if ((str(departureStation) not in stations) or (str(destinationStation) not in stations)):
            flash('Invalid station!', category='error')
        else:
            return redirect(url_for('views.result'))

    return render_template("home.html", user = current_user, stations = stations)

@views.route('/result', methods=['GET', 'POST'])
def result():
    trains = ["Newlands", "UCT", "Muizenburg"]
    if request.method == 'POST':
        return redirect(url_for('views.home'))
    return render_template("result.html", user = current_user, trains = trains)
