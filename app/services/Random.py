from random import randint
from flask import session
from app.database.mongodb_connect import db

__all__ = ["random_wheel"]


class RandomWheel:

    def random_gift(self, nums: int = 16) -> int:
        if session.get("name_count", 0) in (2, 7, 10):
            gift = db.wheel_gift.find_one(
                {"special": True, "use": False},
                {"_id": 0, "id": 1},
            )
            if gift and "id" in gift:
                return gift["id"]
            return 15
        return randint(1, nums - 3)

    def random_name(self, nums: int = 16) -> int:
        current_count = session.get("name_count", 0) + 1
        session["name_count"] = current_count
        return randint(1, nums)


random_wheel = RandomWheel()
