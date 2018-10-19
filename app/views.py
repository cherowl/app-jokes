# -*- coding: utf-8 -*-
import requests
from app import app
from app import db
from app import models as m
from flask import flash, redirect, url_for
from flask_basicauth import required, logout


@app.route('/') 
def start():
    flash("To create your database of jokes you need an acount, so go to /api/login or sing in")
    return redirect(url_for())

# localhost:8000/api/login?name=ME&passwordHash=365aw4d84qaw84ae4w

@app.route('/api/login?<name&<password>>', methods = ['GET', 'POST'])
def login():
    u = m.User()
  
@auth.route('/logout')
@auth.required
def logout():
    logout()
    flash('You have been logged out.')
    return redirect(url_for('start'))

@app.route('/api/auth/<name>')
def welcome_back(name):
    return "Welcome back, {}!\n \
            - generate a joke /generate_joke \n \
            - get a joke /get_joke \n \
            - see list of jokes /show_jokes \n \
            - delete the joke /delete_joke \n \
            - update the joke \n".format(name)
    
    
@app.route('/api/auth/<name>/get_joke', methods = ['GET'])
@auth.required
def show_jokes(name):
    pass


@app.route('/api/auth/<name>/show_jokes', methods = ['GET'])
@auth.required
def show_jokes(name):
    pass

@app.route('/api/auth/<name>/generate_joke', methods = ['PUT'])
@auth.required 
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