import logging

from flask import session, request, abort, Blueprint, Response, escape

# from functools import wraps

from src import models
from src.app import db

auth = Blueprint("auth", __name__)

@auth.route('/', methods=["GET"])  
def start():
    try:
        offer =" - generate a joke /generate_joke \n \
                 - get a joke /get_joke \n \
                 - see list of jokes /show_jokes \n \
                 - delete the joke /delete_joke \n \
                 - update the joke \n"
        if session['logging_in'] == True:
            name = escape(session['username'])
            return f"Hi {name}. Welcome back!\n" + offer
        elif session['logging_in'] == False: 
            return "Hey! Welcome to the planet of Jokes."
    except Exception as e:
        logging.info(e)
        abort(500)


@auth.route("/login", methods=["POST"])
def login():
    try:
        username = request.form["username"]
        user = models.User.query.filter(models.User.username == username).first()
        password = request.form["password"]
        if user is not None and user.check_password(password):
            session["username"] = username
            session['logging_in'] = True
            user = models.User(name=username, password=password)
            db.session.add(user)
            db.session.commit()
            logging.info("Login by user = {}".format(username))
            return Response(
                        "You're logged in successfuly", 
                        status='200',
                        headers={"Access-Control-Allow-Credentials": "true"})
        else: raise Exception
    except Exception as e:
        logging.info(e, "Login denied for user = {}".format(username))
        abort(401)    


@auth.route("/logout", methods=["POST"])
# @auth_required
def logout():
    try:
        logging.info("Logout by user = {}".format(session.get("username")))
        session.pop("username", None)
        session['logging_in'] = False
        return Response(
                    "You're logged out", 
                    status='200')
    except Exception as e:
        logging.error(e)
        abort(401)


@auth.before_request
def before_request():
    try:
        if escape(session['username']) not in session and request.endpoint != "auth.login":
            pass
        else: raise Exception
    except Exception as e:
        logging.error(e, "Access denied")
        abort(401)

# def auth_required(f):
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         if session['logging_in'] == False:
#             return login()
#         return f(*args, **kwargs)
#     return wrapper