from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SECRET_KEY'] = '123**%'
    db.init_app(app)

    from app import routes
    from app import models  

    app.register_blueprint(routes.main)

    return app

