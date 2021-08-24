from .cucumber_scrapper import cucumber_scrapper
from flask import Flask
from config import Config


cucumbers = None

app = Flask(__name__)
with app.app_context():
    cucumbers = cucumber_scrapper()

app.config.from_object(Config)


from app import routes