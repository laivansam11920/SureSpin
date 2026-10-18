from .routes import *
from flask import Flask, Blueprint


def register_blueprints(app: Flask):

    list_bp: list[Blueprint] = [
        main_bp,
    ]

    for bp in list_bp:
        app.register_blueprint(bp)
