import logging

import requests

from flask import session, request, abort, Blueprint

from src import models
from src.app import db
# from src.auth_handlers import auth_required

jokes = Blueprint("jokes", __name__)


@jokes.route('/generate_joke/<int:primary_key>', methods = ['GET'])
# @auth_required
def generate_joke():
    '''
    Generate a joke using api: https://geek-jokes.sameerkumar.website/api
    '''
    response = None
    try: 
        response = requests.get("https://geek-jokes.sameerkumar.website/api")
    except: Exception('Geek Api isn\'t responding...')

    else:
        if response:
            return response.json()+"\n" 


@jokes.route('/get_joke/<int:primary_key>', methods = ['GET'])
# @auth_required
def get_joke(primary_key):
    pass


@jokes.route('/show_jokes', methods = ['GET'])
# @auth_required
def show_jokes():
    pass

@jokes.route('/update_joke/<int:primary_key>', methods = ['POST'])
# @auth_required
def update_joke(primary_key):
    pass

@jokes.route('/delete_joke/<int:primary_key>', methods = ['DELETE'])
# @auth_required
def delete_joke(primary_key):
    pass
