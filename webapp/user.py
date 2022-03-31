from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

    def get_id(self):
        return (self.user_id)

    def __repr__(self):
        return '<user {}>'.format(self.email)

class UserInfo(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    name = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    age = db.Column(db.String(50))
    city = db.Column(db.String(50))
    hobby = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    socity = db.Column(db.String(50))

    def get_id(self):
        return (self.user_id)

    def __repr__(self):
        return '<user {}>'.format(self.username)