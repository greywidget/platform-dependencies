def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
    an anagram of word1, ignore case and spacing.
    About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    return sorted(word1.replace(" ", "").lower()) == sorted(
        word2.replace(" ", "").lower()
    )


# That works, but here is the PyBites solution
# Also an interesting thing I picked up reading the forum is:
# str.casefold()
from collections import Counter


def _clean_word(word):
    return word.strip().replace(" ", "").lower()


def is_anagram2(word1, word2):
    word1, word2 = _clean_word(word1), _clean_word(word2)
    return Counter(word1) == Counter(word2)
