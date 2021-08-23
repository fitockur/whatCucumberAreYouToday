from app import app, cucumbers
from app.forms import CucumberForm
from flask import render_template


@app.route('/cucumbers-1337/')
def get_cucumbers():
    # Return the cucumbers
    return render_template('cucumbers.html', cucumbers=cucumbers)

# A welcome message to test our server
@app.route('/')
@app.route('/index/')
def index():
    form = CucumberForm()
    return render_template('index.html', name='Nikita', form=form)
