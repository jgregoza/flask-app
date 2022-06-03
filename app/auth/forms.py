from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validatiors import DataRequired, Length, Email, EqualTo, ValidatioError


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(3,15, message='between 3 to 15 character')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='password must match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')
    submit = SubmitField('Login')