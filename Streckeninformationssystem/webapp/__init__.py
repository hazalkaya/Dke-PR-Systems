from os import path

from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"
marsh = Marshmallow()



def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'JuliaH'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initiieren DB
    db.init_app(app)
    marsh.init_app(app)
    migrate = Migrate(app, db)

    from .bahnhof import views
    from .authentification import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Models importieren für Datenbankstruktur
    from .modelsDatabase import Benutzer, Bahnhof, Abschnitt
    from .api import api
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    app.register_blueprint(api, url_prefix="/")

    @login_manager.user_loader
    def load_user(id):
        return Benutzer.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

