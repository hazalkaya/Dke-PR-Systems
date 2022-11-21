from flask import Flask
from Streckeninformationssystem.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from Streckeninformationssystem.app import routes