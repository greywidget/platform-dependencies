"""
Oh, yeah PyBites solution is a lot simpler, just reverse and zip them
them. I was distracted by the Bite Text which mentioned OrderedDict
"""

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()


def get_belt(user_score):
    """new solution (see forum for old solution)"""
    for score, belt in zip(scores[::-1], belts[::-1]):
        if user_score >= score:
            return belt
