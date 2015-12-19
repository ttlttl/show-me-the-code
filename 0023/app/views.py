from app import app, db
from flask import render_template, request, jsonify,current_app, redirect, url_for
from .models import Message

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Message.query.order_by(Message.timestamp.desc()).paginate(
        page, per_page=current_app.config['MESSAGES_PER_PAGE'], error_out=False
    )
    messages = pagination.items
    return render_template('index.html', messages=messages, pagination=pagination)

@app.route('/submit')
def post():
    author = request.args.get('author', 0)
    message = request.args.get('message', 0)
    if author and message:
        msg = Message(author=author, message=message)
        db.session.add(msg)
        db.session.commit()
        return jsonify(result='Success')
    return jsonify(result='False')


@app.route('/deleteall')
def destroydatabase():
    messages = Message.query.order_by(Message.timestamp)
    for message in messages:
        db.session.delete(message)
    db.session.commit()
    return redirect(url_for('.index'))