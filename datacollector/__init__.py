import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .frontend import frontend

def create_app(configfile=None):
    app = Flask(__name__)
    app.register_blueprint(frontend)
    app.config.from_envvar('DATACOLLECTOR_SETTINGS_PATH')
    csrf = CSRFProtect(app)
    return app