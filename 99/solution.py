from itertools import cycle
from string import ascii_uppercase


def sequence_generator():
    numbers = cycle(range(1, len(ascii_uppercase) + 1))
    letters = cycle(ascii_uppercase)

    for number, letter in zip(numbers, letters):
        yield number
        yield letter
