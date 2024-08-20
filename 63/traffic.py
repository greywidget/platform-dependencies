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


def traffic_light_solution():
    """Pybites solution is quite nice, it uses tuple unpacking
    inside a list comprehension. Also zip"""
    colors = ["red", "green", "amber"]
    command = ["Stop", "Go", "Caution"]
    timings = (2, 2, 0.5)
    return cycle([State(*s) for s in zip(colors, command, timings)])


if __name__ == "__main__":
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f"{state.command}! The light is {state.color}")
        sleep(state.timeout)
