# -*- coding: utf-8 -*-
from . import db
from . import login_manager
from flask_moment import datetime
from flask_login import  UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    tasks = db.relationship('Task', backref='author', lazy='dynamic')
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

"""
Flask-Login要求程序实现一个回调函数，使用指定的标识符加载用户，
加载用户的回调函数接收以Unicode字符串形式表示的用户标识符，
如果找到用户，这个函数必须返回用户对象，否则返回None
"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    title = db.Column(db.String(64), index=True)
    body = db.Column(db.Text)