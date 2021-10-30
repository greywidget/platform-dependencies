from collections import namedtuple

Roman = namedtuple("Roman", "thousands hundreds tens units")

roman = {
    "1": Roman("M", "C", "X", "I"),
    "2": Roman("MM", "CC", "XX", "II"),
    "3": Roman("MMM", "CCC", "XXX", "III"),
    "4": Roman("", "CD", "XL", "IV"),
    "5": Roman("", "D", "L", "V"),
    "6": Roman("", "DC", "LX", "VI"),
    "7": Roman("", "DCC", "LXX", "VII"),
    "8": Roman("", "DCCC", "LXXX", "VIII"),
    "9": Roman("", "CM", "XC", "IX"),
    "0": Roman("", "", "", ""),
    " ": Roman("", "", "", ""),
}


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not isinstance(decimal_number, int):
        raise ValueError("Number must be an integer")
    if not 0 < decimal_number < 4000:
        raise ValueError("Number must be in the range 0-4000 exclusive")

    decimal_char = f"{str(decimal_number):>4}"
    thousands, hundreds, tens, units = "", "", "", ""

    thousands = roman.get(decimal_char[0]).thousands
    hundreds = roman.get(decimal_char[1]).hundreds
    tens = roman.get(decimal_char[2]).tens
    units = roman.get(decimal_char[3]).units

    return f"{thousands}{hundreds}{tens}{units}"


if __name__ == "__main__":
    print(romanize(500))
