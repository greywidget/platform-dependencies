import itertools
import os
import urllib.request
from pathlib import Path

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = "dictionary.txt"
DICTIONARY = os.path.join(TMP, DICT)
if not Path(DICTIONARY).exists():
    urllib.request.urlretrieve(
        f"https://bites-data.s3.us-east-2.amazonaws.com/{DICT}", DICTIONARY
    )

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
    valid dictionary words. Use _get_permutations_draw and provided
    dictionary"""
    perms = _get_permutations_draw(draw)
    return [
        word for word in ("".join(item).lower() for item in perms) if word in dictionary
    ]


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
    use itertools.permutations (order of letters matters)"""
    for size in range(1, len(draw) + 1):
        for item in itertools.permutations(draw, size):
            yield item
