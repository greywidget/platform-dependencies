from random import choice

COLORS = "red blue green yellow brown purple".split()


class EggCreator:
    def __init__(self, limit) -> None:
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return choice(COLORS)
