from flask import Flask
from temp.config import config
from app import views

app = Flask(__name__)
app.config = config(filename='../temp/config_data.ini', section='flask')