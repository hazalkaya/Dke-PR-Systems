from flask import Flask
from Strecken.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from Strecken.app import routes
