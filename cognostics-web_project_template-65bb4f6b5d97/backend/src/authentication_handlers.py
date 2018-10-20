import logging

from flask import session, request, abort, Blueprint

import src.models as models

auth = Blueprint("auth", __name__)


@auth.before_request
def before_request():
    if "username" not in session and request.endpoint != "auth.login":
        logging.info("Access denied")
        abort(401)


@auth.route('/echo/<string:message>')
def echo(message):
    return message


@auth.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    user = models.User.query.filter(models.User.username == username).first()
    if user is not None and user.check_password(request.form["password"]):
        session["username"] = username
        logging.info("Login by user = {}".format(username))
        return "OK", 200, {"Access-Control-Allow-Credentials": "true"}
    else:
        logging.info("Login denied for user = {}".format(username))
        abort(401)


@auth.route("/logout", methods=["POST"])
def logout():
    logging.info("Logout by user = {}".format(session.get("username")))
    session.pop("username", None)
    return "Logged out"
