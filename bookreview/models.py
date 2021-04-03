from bookreview import db, login_manager, create_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    readinglist = db.relationship('Readinglist', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}',{self.id}.'{self.email}')"

class Readinglist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(100), nullable=False)
    review = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.Integer, nullable=False)
    libid = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ReadingList('{self.bookname}')"