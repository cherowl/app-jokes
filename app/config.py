import os
from configparser import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))

production_db = 'users_jokes.db'
test_db = 'test.db'


class Config:
# os.urandom(24)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                            'sqlite:///' + os.path.join(basedir, test_db)
    BASIC_AUTH_FORCE = True # True makes the whole site require HTTP basic access authentication.
    @staticmethod
    def init_app(app):
        pass

class TestingConfig(Config):
    BASIC_AUTH_FORCE = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                            'sqlite:///' + os.path.join(basedir, test_db)

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, production_db)
    BASIC_AUTH_USERNAME = 'cherowl'
    BASIC_AUTH_PASSWORD = 'matrix'
    BASIC_AUTH_FORCE = True

config = {
    'default': Config,
    'development': Config,
    'testing': TestingConfig,
    'production': ProductionConfig
}

