# -*- coding: utf-8 -*-

"""
第 0024 题： 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。
用法:
1. python 0024.py deploy()
2. python 0024.py runserver [-h ipaddr, -p port]
"""

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Task

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Task=Task)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def deploy():
    from flask_migrate import upgrade
    db.create_all()
    upgrade()


if __name__ == '__main__':
    manager.run()