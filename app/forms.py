from flask_wtf import FlaskForm
from wtforms import SubmitField

class CucumberForm(FlaskForm):
    submit = SubmitField('Get Cucumber!')