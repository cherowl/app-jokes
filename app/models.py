from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    meta = db.relationship('History', lazy = 'dynamic')
    jokes = db.relationship('Joke', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % (self.id)

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(140), unique=True)
    user_id = db.Column(db.Integer, backref='user', db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Joke %r>' % (self.text)

class History(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ip = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    user_id = db.relationship(db.Integer, backref='user', db.ForeignKey('user.id'))

    def __repr__(self):
        return '<History %r>' % (self.ip)