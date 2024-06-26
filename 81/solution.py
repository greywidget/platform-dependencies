from collections import namedtuple
from operator import attrgetter, lt, gt

"""
Mine was pretty close to this but I liked the PyBites use of:
key=attrgetter("polarity") for sorting the list.
"""


Tweet = namedtuple("Tweet", "text polarity")

# polarity < 0 = negative, > 0 = positive
# long strings and pep8: you can wrap strings in () to reduce line length
tweets = [
    Tweet(
        text="It's shocking that the vast majority of online banking "
        "systems have critical vulnerabilities leaving customer "
        "accounts unprotected.",
        polarity=-0.3333333333333333,
    ),
    Tweet(
        text="The most unbelievable aspect of the Star Trek universe "
        "is that every ship they meet has compatible video "
        "conferencing facilities.",
        polarity=0.125,
    ),
    Tweet(
        text="Excellent set of tips for managing a PostgreSQL cluster "
        "in production.",
        polarity=1.0,
    ),
    Tweet(
        text="This tutorial has a great line-by-line breakdown of how "
        "to train a pong RL agent in PyTorch.",
        polarity=0.8,
    ),
    Tweet(
        text="This is some masterful reporting by ... It's also an "
        "infuriating story. ... is trying to erase debt by preying "
        "on the city’s residents. The poorest get hit the worst. "
        "It’s shameful.",
        polarity=-0.19999999999999998,
    ),
]


def filter_tweets_on_polarity(tweets, keep_positive=True):
    """Filter the tweets by polarity score, receives keep_positive bool which
    determines what to keep. Returns a list of filtered tweets."""
    comp = gt if keep_positive else lt
    return [tweet for tweet in tweets if comp(tweet.polarity, 0)]


def order_tweets_by_polarity(tweets, positive_highest=True):
    """Sort the tweets by polarity, receives positive_highest which determines
    the order. Returns a list of ordered tweets."""
    return sorted(tweets, reverse=positive_highest, key=attrgetter("polarity"))
