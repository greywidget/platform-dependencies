class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self._score = float("-inf")

    def __call__(self, num):
        self._score = max(self._score, num)
        return self._score
