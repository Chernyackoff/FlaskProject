from flask import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key= "P0werw0lf_vl@d"
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


db.create_all()
