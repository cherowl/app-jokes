import os
import logging

from flask import Flask, session
from flask_cors import CORS
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy

from src.models import db
from src.auth_handlers import auth
from src.jokes_handlers import jokes


def create_app():
    # create flask app
    app = Flask(__name__)

    app.config.from_envvar("CONFIG")
            
    # allow any origin for testing and development environments
    if app.config["TESTING"] or app.config["DEVELOPMENT"]:
        CORS(app) 

    # configure logger
    logging.basicConfig(format="%(asctime)s %(levelname)s [%(module)s %(lineno)d] %(message)s", level=app.config['LOG_LEVEL'])

    # init sqlalchemy db connection
    db.init_app(app)
    # db.create_all()

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(jokes, url_prefix='/jokes')

    return app


def create_simple_app():
    app = Flask(__name__)
    logging.basicConfig(format="%(asctime)s %(levelname)s [%(module)s %(lineno)d] %(message)s",
                        level=app.config['LOG_LEVEL'])
    app.config.from_envvar("CONFIG")    

    db.init_app(app)

    return app