import logging
from flask import session, request, abort, Blueprint
from src import app, models

auth = Blueprint("auth", __name__)session


@auth.route("/login", methods=["POST"])
def login():
    try:
        username = request.form["username"]
        user = models.User.query.filter(models.User.username == username).first()
        password = request.form["password"]
        if user is not None and user.check_password(password):
            session["username"] = username
            user = models.User(name=username, password_hash=password)
            db.session.add(u)
            db.session.commit()
            logging.info("Login by user = {}".format(username))
            return "OK", 200, {"Access-Control-Allow-Credentials": "true"}
        else:
            logging.info("Login denied for user = {}".format(username))
            abort(401)
    except:
        (Exception, e)
        loggin.error(e)


@auth.route("/logout", methods=["POST"])
def logout():
    logging.info("Logout by user = {}".format(session.get("username")))
    session.pop("username", None)
    return "Logged out"


@auth.before_request
def before_request():
    if "username" not in session and request.endpoint != "auth.login":
        logging.info("Access denied")
        abort(401)




@app.route('/login', methods = ['GET', 'POST'])
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
    
@app.route('/sign_in')
@login_required
def sign_in(name, password_hash):
    # if     
    return login()

#  logout with flask_basicauth  
@app.route('/logout')
@login_required
def logout():
    session['logged_in'] = False
    flash('You have been logged out.')
    return start()
  