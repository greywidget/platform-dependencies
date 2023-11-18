from string import ascii_lowercase


def validate_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram
    A pangram is a sentence containing every letter in the English alphabet.
    The input `sentence` should be a string containing only English letters.
    The function returns True if the sentence is a pangram, and False otherwise.
    """
    a_z = set(ascii_lowercase)
    stripped = set(sentence.lower().replace(" ", ""))
    return a_z == stripped


if __name__ == "__main__":
    validate_pangram()
