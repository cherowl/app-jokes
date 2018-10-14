# -*- coding: utf-8 -*-

from app import app
import requests
from authentication import User

@app.route('/')
def start():
    return "To start go to /login, sing in and create your database of jokes!"

@app.route('/user/<name>')
def welcome_back(name):
    return "Welcome back, {}!".format(name)


@app.route('/login')
def login():
    '''
    Register a new user
    '''

@app.route('/logout')
def logout():
   pass
    


@app.route('/user/<name>/generate-joke')
def generate_joke(name):
    '''
    Generate a joke using api: https://geek-jokes.sameerkumar.website/api
    '''
    response = None
    try: 
        print("Generating a joke for {}...".format(name))
        response = requests.get("https://geek-jokes.sameerkumar.website/api")
    except: Exception('Geek Api isn\'t responding...')

    else:
        if response:
            return response.json()