from flask import Flask
from .config import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
import subprocess

print(SQLALCHEMY_DATABASE_URI)

subprocess.run("export FLASK_ENV=development", shell=True)
subprocess.run("export FLASK_APP=run", shell=True)

app = Flask(__name__)

# app.config = config(filename='config_data.ini', section='flask')
# app.config.from_object('config') #or from_pyfile()

db = SQLAlchemy(app)

from app import views, models

