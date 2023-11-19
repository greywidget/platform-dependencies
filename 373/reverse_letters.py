from string import ascii_letters


def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""
    letters_only = [char for char in string if char in ascii_letters]
    result = []
    for char in string:
        if char in ascii_letters:
            result.append(letters_only.pop())
        else:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    reverse_letters()
