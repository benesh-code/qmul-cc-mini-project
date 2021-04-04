from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
from sqlalchemy.sql import select
import requests
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .models import User



test=session.query(User)

for tests in test:
    print(tests.countrycode)