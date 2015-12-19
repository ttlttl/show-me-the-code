from app import app, db
from flask import render_template, request, jsonify
from .models import Message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a+b)

@app.route('/submit')
def post():
    author = request.args.get('author', 0)
    message = request.args.get('message', 0)
    if author and message:
        msg = Message(author=author, message=message)
        db.session.add(msg)
        db.session.commit()
    result = Message.query.filter_by(author=author).first()

    return jsonify(result=str(result.author) + str(result.message) + str(result.timestamp))

@app.route('/test')
def test():
    return render_template('test.html')