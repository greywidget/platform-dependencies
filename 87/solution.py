"""
Better than my solution (which worked but I knew wasn't great) because:
1. Error checking is more succinct. I originally used:
if not (this and that)
which broke for strings as it was trying to use > and < with strings
2. The mapping is less convoluted
"""

from collections import OrderedDict

number_to_numeral_mapping = OrderedDict(
    {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
)


def romanize(decimal_number):
    if not isinstance(decimal_number, int) or not 0 < decimal_number < 4000:
        raise ValueError("Use an int in range 1-3999")

    result = ""
    for number, numeral in number_to_numeral_mapping.items():
        while decimal_number >= number:
            result += numeral
            decimal_number -= number

    return result


romanize(1234)
