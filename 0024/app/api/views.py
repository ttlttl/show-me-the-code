from . import api
from flask import render_template, redirect, request, url_for, jsonify
from flask_login import login_required, current_user
from ..models import Task, User
from .. import db

@api.route('/tasks/', methods=['GET'])
@login_required
def get_tasks():
    order = request.args.get('order')
    page = request.args.get('page', 1, type=int)
    if order == '0':
        ordered = Task.timestamp.desc()
    else:
        ordered = Task.timestamp
    keywords = request.args.get('keywords')
    if keywords:
        pagination = Task.query.filter_by(author_id=current_user.id).filter(Task.title.contains(keywords)).order_by(ordered).\
            paginate(page, per_page=8, error_out=False)
    else:
        pagination = Task.query.filter_by(author_id=current_user.id).order_by(ordered).\
            paginate(page, per_page=8, error_out=False)
    tasks = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_tasks', page=page-1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_tasks', page=page+1, _external=True)
    return jsonify({
        'tasks': [task.to_json() for task in tasks],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

@api.route('/tasks/<int:id>', methods=['GET'])
@login_required
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_json())

@api.route('/users/<int:id>', methods=['GET'])
@login_required
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())

@api.route('/tasks/<int:id>', methods=['DELETE'])
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': 'Done'})

@api.route('/tasks/', methods=['POST'])
@login_required
def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({'result': 'Error'})
    task = Task(title=request.json['title'],
                body=request.json['body'] if 'body' in request.json.keys() else None,
                author=current_user._get_current_object())
    db.session.add(task)
    db.session.commit()
    return jsonify({'result': 'Done'})

