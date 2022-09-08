from sre_constants import SUCCESS
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        departureStation = request.form.get('departureStation')
        destinationStation = request.form.get('destinationStation')
        departureTime = request.form.get('departureTime')
        

        if (len(departureStation) < 1 or len(destinationStation) < 1):
            flash('Invalid station!', category='error')
        else:
            flash('Added trip!', category='success')
            return redirect(url_for('views.result'))

    return render_template("home.html", user = current_user)

@views.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
    return render_template("result.html", user = current_user)
