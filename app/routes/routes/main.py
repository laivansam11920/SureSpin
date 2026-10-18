from flask import Blueprint, render_template

main_bp: Blueprint = Blueprint("main", __name__)

@main_bp.route("/users")
def users():
    return render_template("wheel_name.html")


@main_bp.route("/gifts")
def gifts():
    return render_template("wheel_gift.html")
