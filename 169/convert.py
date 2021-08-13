from operator import mul, truediv
def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """

    INCHES = "in"
    CMS = "cm"
    RATE = 2.54
    if not (isinstance(value, float) or isinstance(value, int)):
        raise TypeError("Value must be float or int")

    fmt = str(fmt).lower()
    if fmt not in [INCHES, CMS]:
        raise ValueError(f"fmt must be {INCHES} or {CMS}")

    op = mul if fmt == CMS else truediv

    return round(op(value, RATE), 4)