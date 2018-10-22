from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
# import bcrypt

db = SQLAlchemy()

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)   
    meta = db.relationship('Meta', backref='user', lazy='dynamic')
    jokes = db.relationship('Joke', backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.name = username
        self.password_hash = generate_password_hash(password)
        # self.password_hash = bcrypt.hashpw(password.encode("utf-8"),
        #                                    bcrypt.gensalt()).decode("utf-8")
    # def check_password(self, password):
    #     return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

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

class Joke(db.Model):
    __tablename__='jokes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(140), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Joke {}, {}, {}>'.format(self.id, self.text, self.user_id)

 
class Meta(db.Model):
    __tablename__='user_request_history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sid = db.Column(db.Integer, nullable=False)
    ip = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<meta {}, {}, {}, {}, {}>'.format(
            self.id, self.ip, self.sid, self.timestamp, self.user_id
        )
