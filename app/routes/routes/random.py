from flask import Blueprint, jsonify

random_bp: Blueprint = Blueprint("random", __name__)


@random_bp.get("/random-users")
def random_name():
    from app.services.Random import random_wheel
    from flask import request

    total = int(request.args.get("total", 0))

    return jsonify({"status": "success", "winnerIndex": random_wheel.random_name()})


@random_bp.get("/random-gifts")
def random_gift():
    from app.services.Random import random_wheel
    from flask import request

    total = int(request.args.get("total", 0))

    return jsonify({"status": "success", "winnerIndex": random_wheel.random_gift()})
