from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config
from .oauth import OAuthSignIn

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    login.init_app(app)
    db.init_app(app)

    from .models import models

    from app.blueprints.auth import bp as auth_bp
    from app.blueprints.main import bp as main_bp

    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app