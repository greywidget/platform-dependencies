def _is_ascii(word):
    """Helper to determine if a word consists of only ascii chars"""
    return not all(ord(char) < 128 for char in word)


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [word for word in text.split() if _is_ascii(word)]
