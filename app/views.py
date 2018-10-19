# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, session, escape, request
# from flask_basicauth import required ?? dosn't work
import requests
from app import app
from app import db
from app.models import User, Joke, Cookie
from app import auth
from flask_login import login_required # different modules for create and check login NB!
# from flask_basicauth import logout 
 

# TODO make sessions + add routes

@app.route('/') 
@app.route('/api') 
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
        return redirect(url_for(sign_in))

# localhost:8000/api/login?name=ME&passwordHash=365aw4d84qaw84ae4w

@app.route('/api/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        try:
            name = request.get('name')
            u = User(name=name, password_hash=request.get('password_hash'))
            session['user'] = name
            if u.unique():
                db.session.add(u)
                db.session.commit()
                # redirect(url_for(auth))
        except:
            print("Will be redirection")
    else:
        return url_for('login')
    
@app.route('/api/sign_in')
@login_required
def sign_in(name, password_hash):
    # if     
    return redirect(url_for('login'))

#  logout with flask_basicauth  
@app.route('/api/logout')
@login_required
def logout():
    # logout()
    flash('You have been logged out.')
    return redirect(url_for('start'))
  
@app.route('/api/auth/<name>/get_joke', methods = ['GET'])
@login_required
def get_joke(name):
    pass


@app.route('/api/auth/<name>/show_jokes', methods = ['GET'])
@login_required
def show_jokes(name):
    pass

@app.route('/api/auth/<name>/generate_joke', methods = ['PUT'])
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