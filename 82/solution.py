from enum import Enum

"""
Note the use of cls as the parm for the class method and 
the proper way to iterate the members...
"""

THUMBS_UP = "👍"  # in case you go f-string ...


class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f"{self.name} => {self.value * THUMBS_UP}"

    @classmethod
    def average(cls):
        return sum(s.value for s in cls) / len(cls)
