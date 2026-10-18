from flask import Blueprint, jsonify
from app.services.Random import RandomWheel

random_bp: Blueprint = Blueprint("random", __name__)


@random_bp.get("/random-users")
def random_name():
    return jsonify({"status": "success", "winnerId": RandomWheel.random_name()})


@random_bp.get("/random-gifts")
def random_gift():
    return jsonify({"status": "success", "winnerId": RandomWheel.random_gift()})
