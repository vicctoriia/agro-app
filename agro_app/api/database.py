from flask import current_app
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    """IInicializando a conexão com o BD"""
    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

        db.init_app(app)

