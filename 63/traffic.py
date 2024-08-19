from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple("State", "color command timeout")

colors = cycle("red green amber".split())
commands = cycle("Stop Go Caution".split())
timeouts = cycle((2, 2, 0.5))


def traffic_light():
    """Returns an itertools.cycle iterator that
    when iterated over returns State namedtuples
    as shown in the Bite's description"""
    red = State("red", "Stop", 2)
    green = State("green", "Go", 2)
    amber = State("amber", "Caution", 0.5)

    return cycle((red, green, amber))


if __name__ == "__main__":
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f"{state.command}! The light is {state.color}")
        sleep(state.timeout)
