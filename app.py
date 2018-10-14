# -*- coding: utf-8 -*-

from flask import Flask
from config import config
# import views


app = Flask(__name__)


if __name__ == '__main__':
    app.config = config(filename='config_data.ini', section='flask')
    app.run() 
    