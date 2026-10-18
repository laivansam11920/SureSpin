from random import choice
from flask import session

from app.database.mongodb_connect import db
from configs import Config

__all__ = ["RandomWheel"]


class RandomWheel:

    @staticmethod
    def random_gift() -> int:
        if session.get("name_count", 0) in Config.LIST_ID_SPECIAL:
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

    @staticmethod
    def random_name() -> int:
        current_count = session.get("name_count", 0) + 1
        session["name_count"] = current_count

        users_data = list(
            db.wheel_name.find(
                {"use": False},
                {"_id": 0, "id": 1},
            )
        )

        return int(choice(users_data).get("id", 1))
