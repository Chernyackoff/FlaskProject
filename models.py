from flask import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key= generate_password_hash("P0werw0lf_vl@d")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/Anchor.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(10000), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    account_type = db.Column(db.String(5), unique=False, nullable=False)
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10000), unique=False, nullable=False)
    text = db.Column(db.String(100000000000), unique=False, nullable=False)
    description = db.Column(db.String(10000), unique=False, nullable=False)

    def __repr__(self):
        return '<News {}, {}, {}, {}>'.format(self.id, self.title, self.text, self.description)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100000000000), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Comment {}, {}, {}>'.format(self.id, self.text, self.user_id)


db.create_all()
