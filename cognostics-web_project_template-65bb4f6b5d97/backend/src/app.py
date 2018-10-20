import logging

from flask import Flask
from flask_cors import CORS

from src.authentication_handlers import auth
from src.database import db
from src.request_handler import RequestHandler
from src.scheduler_manager import SchedulerManager
from src.socketio_handlers import create_sio


def create_app():
    # create flask app
    app = Flask(__name__)
    app.config.from_envvar("CONFIG")
    # allow any origin for testing and development environments
    if app.config["TESTING"] or app.config["DEVELOPMENT"]:
        CORS(app) 

    # configure logger
    logging.basicConfig(format="%(asctime)s %(levelname)s [%(module)s %(lineno)d] %(message)s",
                        level=app.config['LOG_LEVEL'])

    # init sqlalchemy db connection
    db.init_app(app)

    # create and init socket server with request handler
    request_handler = RequestHandler()
    sio = create_sio(request_handler)
    sio.init_app(app)

    # init scheduler in case if it's not a testing environment
    if not app.config["TESTING"]:
        SchedulerManager(app, sio)

    app.register_blueprint(auth, url_prefix='/auth')

    return sio, app


def create_minimal_app():
    app = Flask(__name__)
    app.config.from_envvar("CONFIG")
    logging.basicConfig(format="%(asctime)s %(levelname)s [%(module)s %(lineno)d] %(message)s",
                        level=app.config['LOG_LEVEL'])
    db.init_app(app)
    return app
