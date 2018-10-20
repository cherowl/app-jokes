# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, session, escape, request
import requests
from src.models import User, Joke, Meta
from src import models
from app import app, db

from app import db
from app import auth
from flask_login import login_required # different modules for create and check login NB!
# from flask_basicauth import logout 
 

# TODO make sessions + add routes

@app.route('/')  
def start():
    if 'user' in session:
        return "Welcome back, {}!\n \
                 - generate a joke /generate_joke \n \
                 - get a joke /get_joke \n \
                 - see list of jokes /show_jokes \n \
                 - delete the joke /delete_joke \n \
                 - update the joke \n".format(escape(session['user']))
    else:
        flash("To manage your database sing in, please")
        return sing_in()

# localhost:8000/login?name=ME&passwordHash=365aw4d84qaw84ae4w

@app.route('/auth/<name>/get_joke', methods = ['GET'])
@login_required
def get_joke(name):
    pass


@app.route('/auth/<name>/show_jokes', methods = ['GET'])
@login_required
def show_jokes(name):
    pass

@app.route('/auth/<name>/generate_joke', methods = ['GET'])
@login_required 
def generate_joke(name):
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