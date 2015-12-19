from app import db
from flask_moment import datetime

class Message(db.Model):
    __tablename__ = 'messages'
    author = db.Column(db.String(64), index=True)
    message = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow, primary_key=True)