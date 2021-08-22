from .cucumber_scrapper import cucumber_scrapper
from flask import Flask


cucumbers = cucumber_scrapper()
app = Flask(__name__)


from app import routes