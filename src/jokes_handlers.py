import logging

import requests

from flask import session, request, abort, Blueprint, current_app, Response

from src import models
from src.models import db

jokes = Blueprint("jokes", __name__)

# @jokes.before_request
# def before_request():
#     try:
#         if 'username' in session:
#             pass
#         else:
#             raise Exception
#     except Exception as e:
#         logging.error(e)
#         return Response(
#                     response="Access denied.\n", 
#                     status=401)


@jokes.route('/generate_joke', methods = ['GET', 'POST'])
def generate_joke():
    '''
    Generate a joke using api: https://geek-jokes.sameerkumar.website/api
    '''
    response = None
    # user = session['username']
    user = 'test'
    try:
        response = requests.get("https://geek-jokes.sameerkumar.website/api")
        if response is not None:
            user_id = models.User.query.filter(models.User.username == user ).first().id
            joke_text = response.json()+"\n" 
            
            joke = models.Joke(text=joke_text, user_id=user_id)
            if joke is not None:
                db.session.add(joke)
                db.session.commit()
                logging.info(f"A joke was generated and saved for {user}")
                return Response(
                    response=f"A joke was generated and saved to db\n", 
                    status='200')
            else:
                logging.error('Not unigue joke')
                return Response(
                        response="Not uniqie joke", 
                        status='400')
        else:
            logging.error("API https://geek-jokes.sameerkumar.website/api is not respondig" )
            return Response(
                    response="Geek api is not responding",
                    status=400)
    except Exception:
        logging.error("Unexpected server error\n")
        return Response(
                response="Unexpected server error\n",
                status=400)
    

@jokes.route('/get_joke/<int:primary_key>', methods = ['GET'])
def get_joke(primary_key):
    user = session['username']
    # user = 'test'

    jokes = models.User.query.filter(models.User.username == user).first_or_404().jokes
    if jokes is not None:    
        for joke in jokes:
            if joke.id == primary_key:
                logging.info(f"The joke by id {primary_key} is {joke.text}")
                return Response(
                response=f"OK: {joke.text}\n",
                status=200
        ) 
    else:
        logging.error(f"Joke by id {primary_key} was not found")
        return Response(
                response="Joke was not found\n",
                status=400
        ) 

@jokes.route('/show_jokes', methods = ['GET'])
def show_jokes():
    # user = session['username']
    user = 'test'

    jokes = models.User.query.filter(models.User.username == user).first_or_404().jokes
    if jokes is not None:  
        searching = []
        for joke in jokes:
            searching.append(joke.text)  
        
        logging.info(f"Jokes of user {user} are {searching}")
        return Response(
                response=f"OK: {searching}\n",
                status=200) 
    else:
        logging.error(f"Jokes of user {user} was not found")
        return Response(
                response="Joke was not found\n",
                status=400) 

@jokes.route('/update_joke/<int:primary_key>', methods = ['POST'])
def update_joke(primary_key):
    user = session['username']
    # user = 'test'

    new_text = request.json.get("new_text")
    joke = models.Joke.query.filter(models.User.id == primary_key).first_or_404()
    if joke and new_text:    
        joke.text = new_text
        db.session.commit()
        logging.info(f"The joke by id {primary_key} was updated as: '{new_text}''")
        return Response(
                response=f"The joke by id {primary_key} was updated as: {new_text}\n",
                status=200) 
    else:
        logging.error(f"Joke by id {primary_key} was not found\n")
        return Response(
                response="Joke was not found\n",
                status=400) 
    
@jokes.route('/delete_joke/<int:primary_key>', methods = ['DELETE']) #203
def delete_joke(primary_key):
    user = session['username']
    # user = 'test'

    joke = models.Joke.query.filter(models.User.id == primary_key).first_or_404()
    if joke is not None:    
        db.session.delete(joke)
        db.session.commit()
        logging.info(f"The joke by id {primary_key} was deleted")
        return Response(
                response=f"The joke by id {primary_key} was deleted\n",
                status=200) 
    else:
        logging.error(f"Joke by id {primary_key} was not found\n")
        return Response(
                response="Joke was not found\n",
                status=400) 
    