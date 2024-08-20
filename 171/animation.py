from itertools import cycle
from time import sleep

SPINNER_STATES = ["-", "\\", "|", "/"]  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
    Takes seconds argument = time for the spinner to run.
    Does not return anything, only prints to stdout."""
    states = cycle(SPINNER_STATES)
    animation_count = int(round(seconds / STATE_TRANSITION_TIME))
    for _ in range(animation_count):
        print(next(states), end="\r", flush=True)
        sleep(STATE_TRANSITION_TIME)


if __name__ == "__main__":
    spinner(2)
