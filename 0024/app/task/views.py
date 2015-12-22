from . import task
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from .forms import TaskForm
from ..models import Task
from .. import db

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

@task.route('/task/my-tasks', methods=['GET', 'POST'])
@login_required
def my_tasks():
    page = request.args.get('page', 1, type=int)
    pagination = Task.query.filter_by(author_id=current_user.id).order_by(Task.timestamp.desc()).paginate(
        page, per_page=5, error_out=False
    )
    tasks = pagination.items
    return render_template('task/my-tasks.html', tasks=tasks, pagination=pagination)

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
