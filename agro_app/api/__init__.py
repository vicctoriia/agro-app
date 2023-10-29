from flask import Blueprint, Flask
from .entrypoints import bp as agro_app_blueprint
from .database import init_db

def init_app(app: Flask) -> None:
    """Start the blueprints.

    :arg:
      Flask application
    """

    app.register_blueprint(agro_app_blueprint)
    init_db(app)
