from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# UserMixin - maybe not needed

class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)   
    meta = db.relationship('Meta', backref='user', lazy = 'dynamic')
    jokes = db.relationship('Joke', backref='user', lazy = 'dynamic')

    def __repr__(self):
        return '<User {}, {}, {}>'.format(self.id, self.name, self.password_hash)

    @property
    def password(self):
        raise AttributeError('Password is not a readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Joke(UserMixin, db.Model):
    __tablename__='jokes'
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(140), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #backref='user',

    def __repr__(self):
        return '<Joke {}, {}, {}>'.format(self.id, self.text, self.user_id)

 
class meta(UserMixin, db.Model):
    __tablename__='user_request_history'
    id = db.Column(db.Integer, primary_key = True)
    sid = db.Column(db.Integer, nullable=False)
    ip = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #backref='user',

    def __repr__(self):
        return '<meta {}, {}, {}, {}, {}>'.format(
            self.id, self.ip, self.sid, self.timestamp, self.user_id
        )
