# -*- coding: utf-8 -*-
import logging

from flask import session, request, abort, Blueprint, Response, current_app, flash

from src import models
from src.models import db

auth = Blueprint("auth", __name__)

            


@auth.route('/', methods=["POST", "GET"])  
def start():
    try:
        offer ="""  - generate a joke /generate_joke \n
                    - get a joke /get_joke \n
                    - see list of jokes /show_jokes \n
                    - delete the joke /delete_joke \n
                    - update the joke \n"""
        if 'username' in session:
            name = session['username']
            logging.info("Greeting in start")
            return Response(
                    response=f'Hi {name}. Welcome back!\n{offer}',
                    status=200,
                    headers={"Access-Control-Allow-Credentials": "true"}) 
        elif 'username' not in session:
            logging.error("Forbidden acces in /")
            return Response(
                    response="Forbidden. Go to /auth/login or /auth/register to have an access.\n",
                    status=401)
    except Exception as e:
        logging.error(e)
        return Response(
                response="Unnexpected behaviour\n", 
                status=500)

@auth.route('/register', methods=["GET", "POST"])  
def register():
    try:
        username = request.json.get("username")
        password = request.json.get("password")
        if username and password:
            user = models.User(username=username, password=password)
            try:    
                db.session.add(user)
                db.session.commit()
                logging.info("Login by user = {}".format(username))
                return Response(
                           response="You're registred successfuly\n", 
                           status=200,
                           headers={"Access-Control-Allow-Credentials": "true"})    
            except Exception as e:
                logging.error(e)
                return Response(
                        response="Already exists!\n",
                        status=409) 
        else:
            raise Exception
    except Exception as e:
            logging.error(e)
            return Response(
                    response=f"{e}\n",
                    status=400) # Not Acceptable
        

@auth.route("/login", methods=["POST"])
def login():
    try:
        username = request.json.get("username")
        password = request.json.get("password")
        # user = models.User.query.filter(models.User.name == username).first()
        # password = request.form["password"]
        user = User.query.filter_by(username = username).first()
        # return Response(user, 200)
        if user is not None and user.check_password(password):
            # session.clear()
            session["username"] = username
            logging.info("Login by user = {}".format(username))
            return Response(
                        response=f"You're logged as {username}!\n", 
                        status=200,
                        headers={"Access-Control-Allow-Credentials": "true"})
        else:
            raise Exception
    except Exception as e:
        logging.error(e)
        return Response(
                response=f"Wrong credentials, {username}!\n",
                status=401)   


@auth.route("/logout", methods=["GET", "POST"])
def logout():
    try:
        logging.info("Logout by user = {}".format(session.get("username")))
        session.pop("username", None)
        logging.info("Successfuly logged out")
        session.clean()
        return Response(
                    response="You're logged out.\n", 
                    status=200)
    except Exception as e:
        logging.error(e)
        return Response(
                    response="Unnexpected behaviour.\n", 
                    status=500)

@auth.before_request
def before_request():
    try:
        if 'username' not in session and request.endpoint == "auth.register" \
                or request.endpoint != "auth":
            pass
        else:
            raise Exception
    except Exception as e:
        logging.error(e)
        return Response(
                    response="Access denied.\n", 
                    status=401)
