import logging

# Flask
APP_PORT = 9000
SECRET_KEY = 'some_secret'

# Database
DB_USER = "test_user"
DB_PASSWORD = "test"
DB_SERVER = "localhost"
DB_NAME = "users_jokes" # another for texting

# SQL-Alchemy
# SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                            'sqlite:///' + os.path.join(APP_DIR + '/src/db/' + DB_NAME + '.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Logging
LOG_LEVEL = logging.DEBUG
BASIC_AUTH_FORCE = True # True makes the whole site require HTTP basic access authentication.


# Other
TESTING = True
