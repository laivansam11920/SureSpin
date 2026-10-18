from random import choice
from flask import session

from app.utils.return_list_from_txt import return_list

__all__ = ["random_wheel"]


class RandomWheel:

    list_gift: list
    list_names: list

    def __init__(self):
        self.list_gift, self.list_names = return_list()

    def random_gift(self) -> str:
        if session.get("name_count", 0) in (2, 5, 7, 9):
            return "Quà rất rất to"
        return choice(self.list_gift)

    def random_name(self) -> str:
        current_count = session.get("name_count", 0) + 1
        session["name_count"] = current_count
        return choice(self.list_names)


random_wheel = RandomWheel()
