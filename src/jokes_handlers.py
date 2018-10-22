import logging

import requests

from flask import session, request, abort, Blueprint, current_app, Response

from src import models
from src.models import db

jokes = Blueprint("jokes", __name__)

@jokes.before_request
def before_request():
    try:
        if 'username' in session:
            pass
        else:
            raise Exception
    except Exception as e:
        logging.error(e)
        return Response(
                    response="Access denied.\n", 
                    status=401)


@jokes.route('/generate_joke', methods = ['GET', 'POST'])
def generate_joke():
    '''
    Generate a joke using api: https://geek-jokes.sameerkumar.website/api
    '''
    response = None
    try:
        response = requests.get("https://geek-jokes.sameerkumar.website/api")
        # return Response(response.json(), 200)
        if response is not None:
            user_id = models.User.query.filter(models.User.username == session['username']).first().id
            joke_text = response.json()+"\n" 
            joke = models.Joke(text=joke_text, user_id=user_id)
            db.session.add(joke)
            db.session.commit()
            logging.info(f"A joke was generated and saved for {session['username']}")
            return Response(
                response=f"A joke was generated and saved to db", 
                status='200')
        else:
            logging.error("API https://geek-jokes.sameerkumar.website/api is not respondig" )
            return Response(
                    response="Geek api is not responding",
                    status=400)

    except Exception as e:
        logging.error('Not unigue joke')
        return Response(
                response="Not uniqie joke", 
                status='400')

@jokes.route('/get_joke/<int:primary_key>', methods = ['GET'])
def get_joke(primary_key):
    pass


@jokes.route('/show_jokes', methods = ['GET'])
def show_jokes():
    pass

@jokes.route('/update_joke/<int:primary_key>', methods = ['POST'])
def update_joke(primary_key):
    pass

@jokes.route('/delete_joke/<int:primary_key>', methods = ['DELETE']) #203
def delete_joke(primary_key):
    pass
