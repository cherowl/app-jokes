import bcrypt

from src.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"),
                                           bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def get_full_name(self):
        return " ".join((self.first_name, self.last_name))
