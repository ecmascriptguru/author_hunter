# coding: utf-8
"""
Main Module for project.
"""

import logging, os

from flask import Flask

from config import app_config
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

login_manager = LoginManager()
from .models import db, session
from .env import DEFAULT_FLASK_CONFIG

config_name = os.getenv('FLASK_CONFIG')
if not config_name:
    config_name = DEFAULT_FLASK_CONFIG
    
app = Flask(__name__, instance_relative_config = True)
app.config.from_object(app_config[config_name])

Bootstrap(app)
db.init_app(app)

login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"

migrate = Migrate(app, db)

logging.basicConfig()

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.errorhandler(404)
def page_not_found(e):
    logging.exception("Page not found.")
    return """
    Page not found: <pre>{}</pre>
    See logs for full track.
    """.format(e), 404

@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()
    pass
