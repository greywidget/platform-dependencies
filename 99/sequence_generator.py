from itertools import cycle
from string import ascii_uppercase


def sequence_generator():
    values = zip(range(1, 27), ascii_uppercase)
    yield from cycle([item for t in values for item in t])
