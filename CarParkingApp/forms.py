from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    Phone_number = StringField('Mobile Number',
                           validators=[DataRequired(), Length(min=10, max=10)])
    car_number = StringField('Car Registration Number',
                           validators=[DataRequired(), Length(min=11, max=11)])                                           

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AvailabilityForm(FlaskForm):
    City = SelectField('City',
                         choices=[('KOL', 'Kolkata'), ('MUM', 'Mumbai'), ('Che', 'Chennai')])
                         

    Area = SelectField('Area',
                         choices=['North','South','East','West'] )
    ShoppingMall = SelectField('Shopping Mall',
                         choices=['South City Mall','Axis Mall','Acropolis Mall'])
    submit = SubmitField('Check Availibility')   