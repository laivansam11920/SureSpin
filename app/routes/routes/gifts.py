from flask import Blueprint, jsonify

gift_bp: Blueprint = Blueprint("gift", __name__)


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


@gift_bp.get("/get_gifts")
def get_gifts():
    from app.database.mongodb_connect import db

    data = list(db.wheel_gift.find({"use": False}, {"_id": 0}))

    return jsonify({"users": data})


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
