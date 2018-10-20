import logging

# Flask
SECRET_KEY = 'secret!'
APP_PORT = 9000

# Database
DB_USER = "test_user"
DB_PASSWORD = "test"
DB_SERVER = "localhost"
DB_NAME = "test_db"

# SQL-Alchemy
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Logging
LOG_LEVEL = logging.DEBUG

# Other
TESTING = True
