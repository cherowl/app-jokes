import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from app import app
# from config import basedir


basedir = os.getcwd()

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))