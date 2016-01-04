from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bootstrap import WebCDN
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from .config import BasicConfig

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(BasicConfig)

    bootstrap.init_app(app)
    app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
        '//cdn.bootcss.com/jquery/1.11.3/'
    )
    app.extensions['bootstrap']['cdns']['bootstrap'] = WebCDN(
        '//cdn.bootcss.com/bootstrap/3.3.5/'
    )
    db.init_app(app)
    login_manager.init_app(app)

    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .task import task as task_blueprint
    app.register_blueprint(task_blueprint)
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app