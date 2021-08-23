from .cucumber_scrapper import cucumber_scrapper
from flask import Flask
from config import Config


cucumbers = cucumber_scrapper()
app = Flask(__name__)
app.config.from_object(Config)


from app import routes