"""
第 0023 题： 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。
用法 python 0023.py
"""
from app import app, db

db.create_all()
app.run(debug=True)