from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        departureStation = request.form.get('departureStation')
        destinationStation = request.form.get('destinationStation')
        departureTime = request.form.get('departureTime')
        print(departureStation)

        if (len(departureStation) < 1 or len(destinationStation) < 1):
            flash('Invalid station!', category='error')
        else:
            new_note = Note(data=departureStation + "-" + destinationStation + " at " +departureTime, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Added trip!', category='success')

    return render_template("home.html", user=current_user)


