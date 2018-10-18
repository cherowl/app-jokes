# -*- coding: utf-8 -*-

from app import app
import requests
import database as db
# from authentication import User

@app.route('/')
def start():
    return "To start go to /login, sing in and create your database of jokes!\n"

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        user_id = db.add_user(password=form.password.data)
        user = User(user_id=user_id)
        login_user(user, form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('auth/sign_up.html', form=form)


@app.route('/login')
def login():
    '''
    Register a new user
    '''
    pass

@app.route('/logout')
def logout():
   pass

@app.route('/user/<name>')
def welcome_back(name):
    return "Welcome back, {}!\n".format(name)
    

@app.route('/user/<name>/generate_joke')
# @login_required 
def generate_joke():
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