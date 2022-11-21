from flask import Flask
from Strecken.config import Config
from Strecken.app import routes


app = Flask(__name__)
app.config.from_object(Config)


