from random import choice
from flask import session
from app.database.mongodb_connect import db

__all__ = ["random_wheel"]


class RandomWheel:

    def random_gift(self) -> int:
        if session.get("name_count", 0) in (2, 7, 10):
            gift = db.wheel_gift.find_one(
                {"special": True, "use": False},
                {"_id": 0, "id": 1},
            )
            return gift.get("id", 15)
        gift_data = list(
            db.wheel_gift.find(
                {"use": False},
                {"_id": 0, "id": 1},
            )
        )
        return int(choice(gift_data).get("id", 1))

    def random_name(self) -> int:
        current_count = session.get("name_count", 0) + 1
        session["name_count"] = current_count

        users_data = list(
            db.wheel_name.find(
                {"use": False},
                {"_id": 0, "id": 1},
            )
        )

        return int(choice(users_data).get("id", 1))


random_wheel = RandomWheel()
