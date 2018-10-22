import logging

import requests

from flask import session, request, abort, Blueprint, current_app

from src import models
from src.models import db
# from src.auth_handlers import auth_required

jokes = Blueprint("jokes", __name__)


@jokes.route('/generate_joke/<int:primary_key>', methods = ['GET', 'POST'])
# @auth_required
def generate_joke():
    '''
    Generate a joke using api: https://geek-jokes.sameerkumar.website/api
    '''
    response = None
    try: 
        if session['logged_in'] == True:    
            user_id = models.User.query.filter(models.User.name == session['username']).id
            response = requests.get("https://geek-jokes.sameerkumar.website/api")
            if response:
                    joke_text = response.json()+"\n" 
                    try:
                        with app.app_context():
                            joke = models.Joke(text=joke_text, user_id=user_id)
                            db.session.add(joke)
                            db.session.commit()
                    except (Exception, e):
                        logging.error('Not unigue joke', e)
                        return Response(
                                "Not uniqie joke", 
                                status='400')
                    else:
                        logging.info(f"A joke was generated and saved for {session['username']}")
                        return Response(
                            f"A joke was generated and saved to db", 
                            status='200')
            else: raise Exception
        else: 
            return login()
    except:
        logging.error('Geek Api isn\'t responding...')
        abort(400) #"Bad request"

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

@jokes.route('/delete_joke/<int:primary_key>', methods = ['DELETE']) #203
# @auth_required
def delete_joke(primary_key):
    pass
