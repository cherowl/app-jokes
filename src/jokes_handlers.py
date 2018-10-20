import logging
from flask import session, request, abort, Blueprint
from src import app, models

jokes = Blueprint("jokes", __name__)
