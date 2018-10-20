import logging

# Flask
APP_PORT = 8000

# Database
DB_USER = "dummy_user"
DB_PASSWORD = "dummy"
DB_SERVER = "postgresql"
DB_NAME = "dummy_name"

# SQL-Alchemy
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Logging
LOG_LEVEL = logging.INFO
