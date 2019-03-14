from flask_wtf import FlaskForm
from wtforms import *


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.required()])
    email = StringField('Email', [validators.email(), validators.required()])
    password = PasswordField('Password', [validators.required()])
    account_type = SelectField('Account type', choices=[('usr', 'User'),
                                                        ('dev', 'Developer')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.required()])
    password = PasswordField('Password', [validators.required()])
    submit = SubmitField('Login')


class NewsForm(FlaskForm):
    title = StringField('Title', [validators.required()])
    text = TextAreaField('Text', [validators.required()])
    description = TextAreaField('Description', [validators.required()])
    submit = SubmitField('Add')


class ComentForm(FlaskForm):
    text = TextAreaField('Text', [validators.required()])
    submit = SubmitField('Add')
