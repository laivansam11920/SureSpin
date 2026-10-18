from flask import Flask
from app.routes import register_blueprints


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "123"
    register_blueprints(app)
    return app
