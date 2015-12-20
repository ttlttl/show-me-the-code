import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BasicConfig:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SECRET_KEY = '@hell9ow13rld0'
    @staticmethod
    def init_app(app):
        pass