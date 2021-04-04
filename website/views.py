from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note , User
from . import db
from sqlalchemy.sql import select
import requests
import json
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
             flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
                

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/update-note', methods=['PUT'])
def update_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    data = note['data']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            note.data = data
            #db.session.update(note)
            db.session.commit()
            flash('Note Updated !', category='success')

    return jsonify({})

@views.route('/external',methods=['GET','POST'])
def external():
    if request.method=='GET' or 'POST':
        #user_id=current_user.id
        #CCuser=User.query.filter_by(countrycode=User.countrycode).first()
        calendar_url = f"https://holidays.abstractapi.com/v1?api_key=0521709cc2bd4c86a973c93f879341c3&country={current_user.countrycode}&year=2020"
        #calendar_format=calendar_url.format(CC=CCuser)

        req=requests.get(calendar_url)
        data1 = json.loads(req.content)
        for row in data1:
            for key in data1[1].keys():
                if row[key] == '':
                    row[key]='NULL'
    return render_template("external.html",data=data1,user=current_user) 
