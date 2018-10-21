import os
import logging

from flask import Flask, session, current_app
from flask_cors import CORS
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy



# db = SQLAlchemy()

def create_app():
    # create flask app
    app = Flask(__name__)
    with app.app_context():
                
        # export CONFIG=/home/elena/workspace/selectel/app-jokes/config/testing.py
        # export CONFIG=/home/elena/workspace/selectel/app-jokes/config/production.py
        # export CONFIG=/home/elena/workspace/selectel/app-jokes/config/development.py
        app.config.from_envvar("CONFIG")

        # allow any origin for testing and development environments
        if app.config["TESTING"] or app.config["DEVELOPMENT"]:
            CORS(app) 

        # configure logger
        logging.basicConfig(format="%(asctime)s %(levelname)s [%(module)s %(lineno)d] %(message)s",
                            level=app.config['LOG_LEVEL'])

        # auth = BasicAuth(app)

        # init sqlalchemy db connection
        from src.models import db
        db.init_app(app)
        db.create_all()


        from src.auth_handlers import auth
        from src.jokes_handlers import jokes


        app.register_blueprint(auth, url_prefix='/auth')
        app.register_blueprint(jokes, url_prefix='/jokes')


        session['logging_in'] == False

        # app.app_context().push()

    return app


def create_simple_app():
    # app = Flask(__name__)
    # logging.basicConfig(format="%(asctime)s %(levelname)s [%(module)s %(lineno)d] %(message)s",
    #                     level=app.config['LOG_LEVEL'])
    # app.config.from_envvar("CONFIG")    
    # with app.app_context():
    #     db.init_app(app)
    #     db.create_all()
    # session['logging_in'] == False
    # return app
    pass
