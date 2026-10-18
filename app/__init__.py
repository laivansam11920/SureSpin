from flask import Flask
from app.routes import register_blueprints


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app
