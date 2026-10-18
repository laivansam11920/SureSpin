from flask import Blueprint, render_template, jsonify

main_bp: Blueprint = Blueprint("main", __name__)
random_bp: Blueprint = Blueprint("random", __name__)
user_bp: Blueprint = Blueprint("user", __name__)
gift_bp: Blueprint = Blueprint("gift", __name__)


@main_bp.route("/users")
def users():
    return render_template("wheel_name.html")


@main_bp.route("/gifts")
def gifts():
    return render_template("wheel_gift.html")


@random_bp.get("/random-users")
def random_name():
    from app.services.Random import random_wheel
    from flask import request

    total = int(request.args.get("total", 0))

    return jsonify(
        {"status": "success", "winnerIndex": random_wheel.random_name(total)}
    )


@random_bp.get("/random-gifts")
def random_gift():
    from app.services.Random import random_wheel
    from flask import request

    total = int(request.args.get("total", 0))

    return jsonify(
        {"status": "success", "winnerIndex": random_wheel.random_gift(total)}
    )


@user_bp.post("/user_del")
def delete_user():
    from app.database.mongodb_connect import db
    from flask import request

    data = request.get_json()

    db.wheel_name.update_one(
        {"id": data.get("id")},
        {"$set": {"use": True}},
    )

    return jsonify(
        {
            "status": "success",
            "message": "Đã xóa thành công",
        }
    )


@gift_bp.post("/delete_gift")
def delete_gift():
    from app.database.mongodb_connect import db
    from flask import request

    data = request.get_json()

    db.wheel_gift.update_one(
        {"id": data.get("id")},
        {"$set": {"use": True}},
    )

    return jsonify(
        {
            "status": "success",
            "message": "Đã xóa thành công",
        }
    )


@user_bp.get("/get_users")
def get_users():
    from app.database.mongodb_connect import db

    data = list(db.wheel_name.find({"use": False}, {"_id": 0}))

    return jsonify({"users": data})


@gift_bp.get("/get_gifts")
def get_gifts():
    from app.database.mongodb_connect import db

    data = list(db.wheel_gift.find({"use": False}, {"_id": 0}))

    return jsonify({"users": data})


@user_bp.post("/reset_user")
def reset_user():
    from app.database.mongodb_connect import db
    from flask import session

    db.wheel_name.update_many({"use": True}, {"$set": {"use": False}})
    session["name_count"] = 0

    data = list(db.wheel_name.find({"use": False}, {"_id": 0}))

    return jsonify(
        {
            "status": "success",
            "users": data,
        }
    )


@gift_bp.post("/reset_gifts")
def reset_gifts():
    from app.database.mongodb_connect import db

    db.wheel_gift.update_many({"use": True}, {"$set": {"use": False}})

    data = list(db.wheel_gift.find({"use": False}, {"_id": 0}))

    return jsonify(
        {
            "status": "success",
            "users": data,
        }
    )
