from flask import Blueprint

todolist = Blueprint('todolist', __name__)

from . import views