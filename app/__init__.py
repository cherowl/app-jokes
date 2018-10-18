from flask import Flask
from .config import config
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config = config(filename='config_data.ini', section='flask')
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

