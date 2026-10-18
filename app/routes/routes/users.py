from flask import Blueprint, jsonify

user_bp: Blueprint = Blueprint("user", __name__)


@user_bp.post("/delete_user")
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


@user_bp.get("/get_users")
def get_users():
    from app.database.mongodb_connect import db

    data = list(db.wheel_name.find({"use": False}, {"_id": 0}))

    return jsonify({"users": data})


@user_bp.post("/reset_users")
def reset_users():
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
