import random

names = "Julian Bob PyBites Dante Martin Rodolfo".split()
aliases = "Pythonista Nerd Coder".split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = " | "


def generate_table(*args):
    for items in zip(*args):
        yield SEPARATOR.join([str(item) for item in items])
