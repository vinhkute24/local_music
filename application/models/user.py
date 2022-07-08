from email.policy import default
from .base import db

from werkzeug.security import generate_password_hash



class User(db.Model):

    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    role =db.Column(db.Integer, default = 0)
   

    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


 
