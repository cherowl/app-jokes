import logging

# Flask
SECRET_KEY = "dummy_data"
APP_PORT = 8000

# Database
DB_USER = "dummy_data"
DB_PASSWORD = "dummy_data"
DB_SERVER = "postgresql"
DB_NAME = "dummy_data"

# SQL-Alchemy
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Logging
LOG_LEVEL = logging.INFO
