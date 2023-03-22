from collections import namedtuple
from operator import attrgetter

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple("Player", "name scores")


def calculate_score(scores):
    """Based on a list of score ints (dice roll), calculate the
    total score only taking into account >= MIN_SCORE
    (= eyes of the dice roll).

    If one of the scores is not a valid dice roll (1-6)
    raise a ValueError.

    Returns int of the sum of the scores.
    """
    if all(isinstance(score, int) and 1 <= score <= 6 for score in scores):
        return sum(score for score in scores if score >= MIN_SCORE)

    raise ValueError("invalid score found")


def get_winner(players):
    """Given a list of Player namedtuples return the player
    with the highest score using calculate_score.

    If the length of the scores lists of the players passed in
    don't match up raise a ValueError.

    Returns a Player namedtuple of the winner.
    You can assume there is only one winner.

    For example - input:
      Player(name='player 1', scores=[1, 3, 2, 5])
      Player(name='player 2', scores=[1, 1, 1, 1])
      Player(name='player 3', scores=[4, 5, 1, 2])

    output:
      Player(name='player 3', scores=[4, 5, 1, 2])
    """

    first_score_len = len(players[0].scores)
    if not all(len(player.scores) == first_score_len for player in players):
        raise ValueError("Score lengths differ")

    return max(players, key=lambda x: calculate_score(x.scores))
