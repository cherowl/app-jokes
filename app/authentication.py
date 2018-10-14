# from passlib.apps import custom_app_context as pwd_context
# import postgresql
# import json

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(32), index = True)
#     password_hash = db.Column(db.String(128))


# class User(db.Model):
#     __tablename__ 
#     id 
#     username
#     password_hash

#     def hash_password(self, password):
#         self.password_hash = pwd_context.encrypt(password)

#     def verify_password(self, password):
#         return pwd_context.verify(password, self.password_hash)


from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
  if g.user is not None and g.user.is_authenticated():
      return redirect(url_for('choose_point'))
  form = LoginForm()
  if form.validate_on_submit():
      session['remember_me'] = form.remember_me.data
      return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
  return render_template('login.html', 
      title = 'Sign In',
      form = form,
      providers = app.config['OPENID_PROVIDERS'])