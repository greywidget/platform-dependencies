from string import ascii_letters, punctuation

DISCARD = punctuation + "".join([str(num) for num in range(10)])


# def extract_non_ascii_words(text):
#     """Filter a text returning a list of non-ascii words"""
#     text = "".join(letter for letter in text if letter not in DISCARD)

#     return [
#         word
#         for word in text.split()
#         if word.lower()
#         != ("".join(letter for letter in word.lower() if letter in ascii_letters))
#     ]


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""

    return [word for word in text.split() if not word.isascii()]
