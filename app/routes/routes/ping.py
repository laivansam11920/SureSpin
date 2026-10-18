from flask import Blueprint

ping: Blueprint = Blueprint("ping", __name__)

@ping.route("/ping")
def ping_pong():
    return "pong"
