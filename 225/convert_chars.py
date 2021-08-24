PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
    Return the resulting string."""
    converted = []
    for char in text:
        if char.lower() in PYBITES:
            converted.append(char.swapcase())
        else:
            converted.append(char)

    return "".join(converted)
