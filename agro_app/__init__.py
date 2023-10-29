from flask import Flask
import os
from . import api

def create_app() -> Flask:
    """Create the application."""

    app = Flask(__name__)

    with app.app_context():
        api.init_app(app)
        
    return app

app = create_app()
