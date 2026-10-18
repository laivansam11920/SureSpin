from random import choice

__all__ = ['random_wheel']

class RandomWheel:

    list_gift: list
    list_names: list

    def __init__(self):
        with open("../../list_gift.txt", "r", encoding="utf-8") as f:
            self.list_gift = [line.strip() for line in f.readlines()]
        with open("../../list_name.txt", "r", encoding="utf-8") as f:
            self.list_names = [line.strip() for line in f.readlines()]

    def random_gift(self) -> str:
        return choice(self.list_gift)

    def random_name(self) -> str:
        return choice(self.list_names)

random_wheel = RandomWheel()
