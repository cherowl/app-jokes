import os
import logging

# Extra
APP_DIR = os.getcwd()
BASEDIR = os.path.abspath(os.path.dirname(__file__)) 
BASIC_AUTH_FORCE = True
BASIC_AUTH_USERNAME = 'cherowl'
BASIC_AUTH_PASSWORD = 'matrix'

# Flask
APP_PORT = 8000
DEVELOPMENT = True
SECRET_KEY = 'some_secret'

# Database
DB_USER = "cherowl"
DB_PASSWORD = "matrix" 
DB_SERVER = "localhost"
DB_NAME = "dev"

# SQL-Alchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                            'sqlite:///' + os.path.join(APP_DIR + '/src/db/' + DB_NAME + '.db')
# SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Logging
LOG_LEVEL = logging.DEBUG
