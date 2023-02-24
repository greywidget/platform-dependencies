def get_ordinal_suffix(number):
    """Receives a number int and returns it appended with its ordinal suffix,
    so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.

    Rules:
    https://en.wikipedia.org/wiki/Ordinal_indicator#English
    - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
    - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
    - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
    - As an exception to the above rules, all the "teen" numbers ending with
      11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
      pronounced one hundred [and] twelfth)
    - th is used for all other numbers (e.g. 9th, pronounced ninth).
    """
    sfx = {"1": "st", "2": "nd", "3": "rd"}

    num_str = str(number)
    if len(num_str) > 1 and ("11" <= num_str[-2:] <= "13"):
        return f"{num_str}th"
    return f"{num_str}{sfx.get(num_str[-1], 'th')}"


if __name__ == "__main__":
    print(get_ordinal_suffix(1111))
