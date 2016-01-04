from . import task
from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user
from .forms import TaskForm, OrderByForm
from ..models import Task, User
from .. import db
import json

@task.route('/task/new-task', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data,
                    body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('task.my_tasks'))
    return render_template('task/new-task.html', form=form)

@task.route('/task/my-tasks', methods=['POST', 'GET'])
@login_required
def my_tasks():
    order = 0
    form = OrderByForm()
    if form.validate_on_submit():
        order = int(form.select.data)
    page = int(request.args.get('page', 1, type=int))
    if order == 0:
        pagination = Task.query.filter_by(author_id=current_user.id).order_by(Task.timestamp.desc()).paginate(
            page, per_page=5, error_out=False
        )
    else:
        pagination = Task.query.filter_by(author_id=current_user.id).order_by(Task.timestamp).paginate(
            page, per_page=5, error_out=False
        )
    tasks = pagination.items
    return render_template('task/my-tasks.html', tasks=tasks, pagination=pagination, form=form)

@task.route('/task/<int:id>')
@login_required
def detail_task(id):
    task = Task.query.get_or_404(id)
    return render_template('task/detail-task.html', task=task)

@task.route('/task/delete/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('task.my_tasks'))

@task.route('/task/tasks', methods=['POST', 'GET'])
def tasks():
    if request.args.get('order') == '1':
        tasks = Task.query.filter_by(author_id=current_user.id).order_by(Task.timestamp.desc())
    else:
        tasks = Task.query.filter_by(author_id=current_user.id).order_by(Task.timestamp)
    return json.dumps([{"id": task.id,
             "author": User.query.filter_by(id = task.author_id).first().username,
             "title": task.title,
             "timestamp": str(task.timestamp)}
            for task in tasks])
