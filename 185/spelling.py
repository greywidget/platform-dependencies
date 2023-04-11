import os
from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Union
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, "dictionary.txt")
if not os.path.isfile(DICTIONARY):
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt", DICTIONARY
    )


@dataclass
class WordMatch:
    """Class for keeping track of a best Word Match"""

    suggested: str = None
    ratio: float = 0


def load_words():
    "return dict of words in DICTIONARY"
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: Union[set, None]) -> str:
    """Return a valid alternative word that best matches
    the entered misspelled word"""
    if words is None:
        words = load_words()

    word_match = WordMatch()

    s = SequenceMatcher(a=misspelled_word)

    for suggested in words:
        s.set_seq2(suggested)
        if (score := s.ratio()) > word_match.ratio:
            word_match.suggested = suggested
            word_match.ratio = score

    return word_match.suggested
