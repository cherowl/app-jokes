import logging

# Flask
APP_PORT = 8000
SECRET_KEY = 'some_secret'


# Database
DB_USER = "dummy_user"
DB_PASSWORD = "dummy"
DB_SERVER = "postgresql"
DB_NAME = "users_jokes"

# SQL-Alchemy
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Logging
LOG_LEVEL = logging.INFO
