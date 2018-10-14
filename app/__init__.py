from flask import Flask
from temp.config import config


app = Flask(__name__)
# app.config = config(filename='config_data.ini', section='flask')

from app import views