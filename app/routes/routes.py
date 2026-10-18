from flask import Blueprint, render_template

main_bp: Blueprint = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return "Hello World!"
