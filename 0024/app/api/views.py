from . import api
from flask import render_template, redirect, request, url_for, jsonify
from flask_login import login_required, current_user
from ..models import Task, User
from .. import db

@api.route('/tasks/')
def get_tasks():
    order = request.args.get('order')
    if order == '0':
        tasks = Task.query.filter_by(author_id=current_user.id).order_by(Task.timestamp.desc())
    else:
        tasks = Task.query.filter_by(author_id=current_user.id).order_by(Task.timestamp)
    return jsonify({'tasks': [task.to_json() for task in tasks]})

@api.route('/tasks/<int:id>')
def get_task():
    task = Task.query.get_or_404(id)
    return jsonify(task.to_json())

@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())