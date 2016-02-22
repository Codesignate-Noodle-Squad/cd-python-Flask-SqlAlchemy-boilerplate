from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

# Creates table User with username, firstname, lastname, email and message columns
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    email = db.Column(db.String(30))
    message = db.Column(db.String(100))

    def __init__(self, username, firstname, lastname, email, message):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.message = message