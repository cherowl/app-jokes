# -*- coding: utf-8 -*-
import requests
from app import app
from app import db
from flask import flash
# from app import oid
# from authentication import User


@app.route('/')
def start():
    # flash("Test flash")
    return "To start go to /login, sing in and create your database of jokes!\n"


@app.route('/login', methods = ['GET', 'POST'])
# @oid.loginhandler
def login():
    '''
    Register a new user
    '''
    pass

@app.route('/logout')
def logout():
   pass

@app.route('/user/<name>')
def welcome_back(name):
    return "Welcome back, {}!\n \
            - generate a joke /generate_joke \n \
            - see list of jokes /show_jokes \n \
            - delete the joke /delete_joke \n \
            - update the joke \n".format(name)
    
@app.route('/user/<name>/show_jokes', methods = ['GET'])
def show_jokes(name):
    return db.show_user_jokes(id_user="id")

@app.route('/user/<name>/generate_joke')
# @login_required 
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