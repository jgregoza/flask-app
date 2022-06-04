import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()

def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    db.init_app(app)   #inicializar db
    login_manager.init_app(app)
    bcrypt.init_app(app)
    bootstrap.init_app(app)

    # import module
    from app.auth import authentication
    from app.catalog import main

    # register module
    app.register_blueprint(authentication)    
    app.register_blueprint(main)

    return app

