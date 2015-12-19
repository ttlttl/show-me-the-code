import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['MESSAGES_PER_PAGE'] = 5
db = SQLAlchemy(app)
moment = Moment(app)

from . import views, models